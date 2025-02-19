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
    name: str,
    pattern: str = typer.Option(
        "list", "--pattern", "-p", help="Pattern of spec prompt"
    ),
    context_file: str = typer.Option(
        None, "--context-file", "-c", help="Path to aider /save file"
    ),
):
    """
    Create a new spec prompt YAML file in the current directory.

    Examples:


        paic spec new specs/name-of-new-spec-file

        paic spec new specs/name-of-new-spec-file -c .aider-context.txt (path to aider /save file)

        paic spec new specs/name-of-new-spec-file --pattern list (currently only 'list' is supported)
    """

    if need_to_upgrade_application():
        logger.info("🟡 A newer version of PAIC Patterns is available.")
        logger.info("🟡 Upgrade using: 'uv tool install --upgrade paic-patterns'")

    filename = build_new_plan(name, pattern, context_file=context_file)
    logger.info(f"✅ Created new spec plan: {filename}")


@app.command()
def run(spec_path: str):
    """Run all tasks (prompts) in the spec file.

    Example:

        paic spec run specs/my_spec_file.yml

    """
    logger.info(f"📝 Running spec: {spec_path}")
    run_spec(spec_path)


@app.command()
def self_build(spec_path: str):
    """Build out tasks in the spec file based on the high-level objective, implementation details, and at least one task.

    Example:

       paic spec self-build my_spec_file.yml

    """
    logger.info(f"🔄 Self-building tasks for spec: {spec_path}")
    run_spec_self_build(spec_path)


@app.command()
def iterate(spec_path: str):
    """Start an aider session using the spec file as context.

    Example:

        paic spec iterate my_spec_file.yml

    """
    spec_file_to_aider_instance(spec_path)
    logger.info(f"✅ Opened aider instance for spec: {spec_path}")
