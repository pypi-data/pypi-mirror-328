import typer
from pathlib import Path
from ..modules.spec_module import (
    build_new_plan,
    spec_file_to_aider_instance,
)
from paic_patterns.modules.versioning import need_to_upgrade_application
from ..modules.spec_runner import run_spec, run_spec_self_build
import logging

logger = logging.getLogger(name="paic_patterns")


app = typer.Typer(
    name="spec",
    help="""
Create, Manage and Run Spec Prompts.

---

Recommended workflow:

1. Create a new spec file: `paic spec new my_spec_file.yml`

2. Update 'my_spec_file.yml', fill out context, model, prompt. Plan and package your work.

3. Run all tasks in the spec file: `paic spec run my_spec_file.yml`

""",
)


@app.command()
def new(
    spec_path: str = typer.Argument(
        ...,
        help="Path to new spec file (without extension)",
    ),
    pattern: str = typer.Option(
        "list",
        "--pattern",
        "-p",
        help="(Optional) Pattern your spec prompt. Default is 'list'.",
    ),
    context_file: str = typer.Option(
        None,
        "--context-file",
        "-c",
        help="(Optional) Path to aider /save file",
    ),
):
    """
    Command Name:

        Create New Spec

    Usage Template:

        paic spec new [path-to-new-spec-file-no-extension] [--pattern list] [--context-file .aider-context]

    Description:

        Creates a new specification file for your AI coding tasks.
        This command initializes a YAML file with the structure needed for PAIC Patterns to understand your requirements.

    Examples Usage:

        paic spec new specs/name-of-new-spec-file

        paic spec new specs/name-of-new-spec-file --pattern list

        paic spec new specs/name-of-new-spec-file -p list

        paic spec new specs/name-of-new-spec-file -p list -c .aider-context
    """

    if need_to_upgrade_application():
        logger.info("🟡 A newer version of PAIC Patterns is available.")
        logger.info("🟡 To upgrade, run: uv tool upgrade paic-patterns")

    filename = build_new_plan(name, pattern, context_file=context_file)
    logger.info(f"✅ Created new spec plan: {filename}")


@app.command()
def run(
    spec_path: str = typer.Argument(..., help="Path to spec file for running tasks")
):
    """
    Command Name:
        Run Spec Tasks

    Usage Template:
        paic spec run [path-to-spec-file]

    Description:
        This command runs all tasks (prompts) defined in the provided spec file based on your context, model, prompt and pattern.

    Examples Usage:
        paic spec run specs/my_spec_file.yml
    """
    logger.info(f"📝 Running spec: {spec_path}")
    run_spec(spec_path)


@app.command()
def self_build(
    spec_path: str = typer.Argument(..., help="Path to spec file for self-build tasks")
):
    """
    Command Name:
        Self Build Spec Tasks

    Usage Template:
        paic spec self-build [path-to-spec-file]

    Description:
        This command builds out tasks in the spec file based on a high-level objective, implementation details, and at least one initial task.

    Examples Usage:
        paic spec self-build specs/my_spec_file.yml
    """
    logger.info(f"🔄 Self-building tasks for spec: {spec_path}")
    run_spec_self_build(spec_path)


@app.command()
def iterate(
    spec_path: str = typer.Argument(..., help="Path to spec file for iterative tasks")
):
    """
    Command Name:
        Iterate Spec Tasks

    Usage Template:
        paic spec iterate [path-to-spec-file]

    Description:
        This command starts an aider session using the provided spec file as context, enabling iterative AI Coding.

    Examples Usage:
        paic spec iterate specs/my_spec_file.yml
    """
    spec_file_to_aider_instance(spec_path)
    logger.info(f"✅ Opened aider instance for spec: {spec_path}")
