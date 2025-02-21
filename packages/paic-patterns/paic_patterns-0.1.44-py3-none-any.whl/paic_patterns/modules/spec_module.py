import os
from pathlib import Path
from typing import Optional
import yaml
from .spec_templates import template_spec_file_list
from .data_types import AICodeParams, ModeEnum, SpecFileList
from aider.coders import Coder
from aider.io import InputOutput
from aider.models import Model
from .aider_llm_models import DEFAULT_MAIN_MODEL, DEFAULT_EDITOR_MODEL
from pathlib import Path
import yaml


def build_new_plan(
    plan_path: str,
    spec_type: str,
    context_file: str = None,
) -> str:
    plan_path = plan_path.strip().replace(" ", "_")
    if not plan_path.endswith(".yaml") and not plan_path.endswith(".yml"):
        plan_path += ".yml"

    # Get models from config with fallbacks
    main_model = DEFAULT_MAIN_MODEL
    editor_model = DEFAULT_EDITOR_MODEL

    # Get just the filename component
    filename = Path(plan_path).stem

    # Create initial content
    content = (
        template_spec_file_list.replace("{{plan_name}}", filename)
        .replace("{{main_model}}", main_model)
        .replace("{{editor_model}}", editor_model)
    )

    # Select template based on spec type
    if spec_type == "list":
        pass
    else:
        raise ValueError(f"Invalid spec type: {spec_type}")

    file_path: Path = Path.joinpath(Path.cwd(), plan_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = replace_context_in_template(content, context_file)

    file_path.write_text(content)

    return str(file_path)


def spec_file_to_load_file(spec_path: str) -> str:
    """Generate .aider-<specname> file from spec"""
    spec = parse_spec_file(spec_path)

    # Get base name without extension
    spec_path_obj = Path(spec_path)
    aider_name = f".aider-{spec_path_obj.stem}"
    output_path = spec_path_obj.parent / aider_name

    lines = ["/drop\n"]

    # Add editable context files
    for fpath in spec.editable_context:
        lines.append(f"/add       {fpath}\n")

    # Add read-only context files
    if spec.readonly_context:
        for fpath in spec.readonly_context:
            lines.append(f"/read-only {fpath}\n")

    # Write the load file
    output_path.write_text("".join(lines))
    return str(output_path)


def parse_spec_file(spec_path: str) -> SpecFileList:
    file_path = Path(spec_path)
    data = yaml.safe_load(file_path.read_text())
    return SpecFileList(**data)


def build_prompt_list(spec: SpecFileList) -> list[str]:
    prompts = []
    instructions = """## Instructions
- You are an expert software engineer.
- You're building a new feature task by task based on a complete spec aka plan.
- To inform your engineering, take the High Level Objective and Implementation Details into account if provided.
- You'll be given a task, and you'll need to write the code to complete the task.
- Focus your engineering efforts on the individual task at hand, use the high level objective and implementation details to inform your work, but don't let it overwhelm your focus.
- The key is to generate the code that satisfies the task."""

    for i, task in enumerate(spec.tasks):
        sections = [f"# Plan: '{spec.plan_name}'\n\n", instructions, "\n"]

        if spec.high_level_objective:
            sections.append("\n\n## High Level Objective\n" + spec.high_level_objective)

        if i == 0 and spec.implementation_details:
            sections.append(
                "\n\n## Implementation Details\n" + spec.implementation_details
            )

        sections.append(
            "\n\n## Task:"
            + (f" '{task.title}'" if task.title else "")
            + "\n\n"
            + task.prompt
        )

        prompts.append("".join(sections) + "\n")

    return prompts


def build_ai_coding_assistant(params: AICodeParams) -> Coder:
    """Create and configure a Coder instance based on provided parameters"""
    settings = params.settings or {}
    auto_commits = settings.get("auto_commits", False)
    suggest_shell_commands = settings.get("suggest_shell_commands", False)
    detect_urls = settings.get("detect_urls", False)

    if params.architect:
        model = Model(model=params.model, editor_model=params.editor_model)
        return Coder.create(
            main_model=model,
            edit_format="architect",
            io=InputOutput(yes=True),
            fnames=params.editable_context,
            read_only_fnames=params.readonly_context,
            auto_commits=auto_commits,
            suggest_shell_commands=suggest_shell_commands,
            detect_urls=detect_urls,
            use_git=params.use_git,
        )
    else:
        model = Model(params.model)
        return Coder.create(
            main_model=model,
            io=InputOutput(yes=True),
            fnames=params.editable_context,
            read_only_fnames=params.readonly_context,
            auto_commits=auto_commits,
            suggest_shell_commands=suggest_shell_commands,
            detect_urls=detect_urls,
            use_git=params.use_git,
        )


def ai_code(coder: Coder, params: AICodeParams):
    """Execute AI coding using provided coder instance and parameters"""
    coder.run(params.prompt)


def parse_aider_context_file(context_file_path: str) -> tuple[list[str], list[str]]:
    """Parse an aider context file and return editable and readonly context files.

    Args:
        context_file_path: Path to the aider context file

    Returns:
        Tuple of (editable_context, readonly_context) lists
    """
    editable_context = []
    readonly_context = []

    with open(context_file_path) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or line == "/drop":
            continue

        if line.startswith("/read-only"):
            path = line.replace("/read-only", "").strip()
            readonly_context.append(path)
        elif line.startswith("/add"):
            path = line.replace("/add", "").strip()
            editable_context.append(path)

    return editable_context, readonly_context


def ping_ai_intelligence(spec: SpecFileList):
    """Send a test prompt to verify AI connectivity"""
    params = AICodeParams(
        architect=spec.architect,
        prompt="/ask ping - just testing - respond with pong",
        model=spec.main_model,
        editor_model=spec.editor_model,
        editable_context=[],
        readonly_context=[],
        settings={},
    )
    coder = build_ai_coding_assistant(params)
    ai_code(coder, params)


def replace_context_in_template(
    content: str, context_file: Optional[str] = None
) -> str:
    """
    Replace the editable and readonly context placeholders in the template content
    based on the provided context file.

    Args:
        content (str): The original template content with placeholders.
        context_file (str): Path to the aider context file.

    Returns:
        str: The updated content with context replaced.
    """

    def replace_editable_with_default(content: str) -> str:
        return content.replace("{{editable_context}}", "\n" + '  - "./path/to/file.py"')

    def replace_readonly_with_default(content: str) -> str:
        return content.replace("{{readonly_context}}", "\n" + '  - "./path/to/file.py"')

    # if there's no context file, update with default placeholders and immediately return
    if not context_file:
        content = replace_editable_with_default(content)
        content = replace_readonly_with_default(content)
        return content

    editable_context, readonly_context = parse_aider_context_file(context_file)

    did_replace_editable_context = False
    did_replace_readonly_context = False

    if editable_context:
        edit_list = "\n".join(f'  - "{f}"' for f in editable_context)
        content = content.replace("{{editable_context}}", "\n" + edit_list)
        did_replace_editable_context = True

    if readonly_context:
        ro_list = "\n".join(f'  - "{f}"' for f in readonly_context)
        content = content.replace("{{readonly_context}}", "\n" + ro_list)
        did_replace_readonly_context = True

    if not did_replace_editable_context:
        # Fallback to default placeholder if no editable context
        content = replace_editable_with_default(content)

    if not did_replace_readonly_context:
        # Fallback to default placeholder if no readonly context
        content = replace_readonly_with_default(content)

    return content


def spec_file_to_aider_instance(spec_path: str) -> None:
    """
    Parses the spec file, ensures all context files exist, generates the load file,
    and opens an aider instance with the specified configurations.

    Args:
        spec_path (str): The path to the spec YAML file.

    Raises:
        FileNotFoundError: If any of the context files do not exist.
    """
    # Parse the spec file
    spec = parse_spec_file(spec_path)

    # Combine editable and readonly context files
    context_files = spec.editable_context + spec.readonly_context

    # Check for missing context files
    missing_files = [f for f in context_files if not Path(f).exists()]
    if missing_files:
        missing = ", ".join(missing_files)
        raise FileNotFoundError(f"The following context files do not exist: {missing}")

    # Generate the load file
    load_file = spec_file_to_load_file(spec_path)

    default_args = [
        "--yes-always",
        "--no-auto-commit",
        "--no-suggest-shell-commands",
        "--no-detect-urls",
    ]

    # Build the command-line arguments based on the architect flag
    if spec.architect:
        args = [
            "aider",
            "--model",
            spec.main_model,
            "--editor-model",
            spec.editor_model,
            "--architect",
            "--load",
            load_file,
            *default_args,
        ]
    else:
        args = [
            "aider",
            "--model",
            spec.main_model,
            "--load",
            load_file,
            *default_args,
        ]

    # Execute the aider process, replacing the current process
    os.execvp("aider", args)
