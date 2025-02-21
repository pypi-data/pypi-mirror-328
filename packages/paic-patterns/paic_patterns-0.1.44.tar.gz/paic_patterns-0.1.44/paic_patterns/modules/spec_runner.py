import logging
from pathlib import Path
import yaml
from unittest import mock
from .spec_module import (
    parse_spec_file,
    build_prompt_list,
    ai_code,
    build_ai_coding_assistant,
)
from .data_types import (
    AICodeParams,
    SpecFileList,
    SpecTask,
    PaicPatternEnum,
)
from .aider_llm_models import TESTING_MODEL

logger = logging.getLogger(name="paic_patterns")


def run_spec(spec_path: str):
    logger.info(f"📝 Parsing spec file: {spec_path}")
    spec = parse_spec_file(spec_path)

    logger.info(
        f"✅ Parsed spec: '{spec.plan_name}' with pattern: '{spec.pattern}' and {len(spec.tasks)} tasks"
    )

    # logger.info("Pinging AI intelligence...")
    # ping_ai_intelligence(spec)

    logger.info("🤖 Building Prompts & AI Coding Assistant")
    prompts = build_prompt_list(spec)

    # Create coder instance once at start
    code_params = AICodeParams(
        architect=spec.architect,
        prompt="",  # Empty initial prompt
        model=spec.main_model,
        editor_model=spec.editor_model,
        editable_context=spec.editable_context,
        readonly_context=spec.readonly_context,
        settings={},
    )
    coder = build_ai_coding_assistant(code_params)

    logger.info(f"🚀 Executing Spec Prompt: '{spec.plan_name}'")

    for i, prompt in enumerate(prompts):
        task_title = spec.tasks[i].title if spec.tasks[i].title else "Untitled Task"
        logger.info(f"🚀 Running Task ({i+1}/{len(spec.tasks)}): '{task_title}'")
        logger.info(f"📝 Prompt: \n```\n{prompt.strip()}\n```\n")

        # Update just the prompt for each task
        code_params.prompt = prompt

        ai_code(coder, code_params)

    logger.info(f"🎉 Completed Running Spec Prompt: '{spec.plan_name}'")


def run_spec_self_build(spec_path: str) -> None:
    """Self-build tasks in a spec file based on existing content"""
    logger.info(f"📝 Loading spec file for self-build: {spec_path}")
    spec = parse_spec_file(spec_path)

    # Validate required fields
    if not spec.high_level_objective:
        msg = "In order to run self-build the high_level_objective must be filled out."
        logger.error(msg)
        raise ValueError(msg)

    if not spec.implementation_details:
        msg = (
            "In order to run self-build the implementation_details must be filled out."
        )
        logger.error(msg)
        raise ValueError(msg)

    if not spec.tasks or len(spec.tasks) < 1:
        msg = "In order to run self-build at least one task with title and prompt must exist."
        logger.error(msg)
        raise ValueError(msg)

    # Format existing tasks for prompt
    existing_tasks = ""
    for i, task in enumerate(spec.tasks):
        existing_tasks += f"\n### Task ({i+1}): '{task.title}'\n{task.prompt}\n"

    # Build the self-build prompt
    prompt = f"""Based on the high level objective, implementation details, instructions, and existing tasks, build out the rest of the tasks.

## Instructions

- Pay close attention to the existing task and specifically how the prompt is written. Use the same structure and style.
- Break up the implementation details into smaller, manageable chunks again referring to the existing tasks as a guide.
- We want individual tasks to be small so they can be completed in a single session.
- Your job is exclusively to add the tasks to the list of tasks. We're not writing any code.
- Heavily base your new task on the implementation details. Look for lists and patterns in the implementation details you can break into tasks.

## High Level Objective
{spec.high_level_objective}

## Implementation Details
{spec.implementation_details}

## Existing Tasks to work from
{existing_tasks}

---

Remember not to write any code. Only build out the tasks."""

    # Create AI coding assistant with spec file as editable context
    code_params = AICodeParams(
        architect=False,
        prompt=prompt,
        model=spec.main_model,
        editor_model=spec.editor_model,
        editable_context=[spec_path],
        readonly_context=[],
        settings={},
        use_git=False,
    )

    logger.info("🤖 Building AI Coding Assistant for self-build")
    coder = build_ai_coding_assistant(code_params)

    logger.info("🚀 Running self-build prompt")
    ai_code(coder, code_params)

    logger.info("✅ Completed self-build of tasks")
