import pytest
import yaml
from pathlib import Path
from unittest import mock

from ..modules.aider_llm_models import TESTING_MODEL
from ..modules.spec_module import spec_file_to_aider_instance, spec_file_to_load_file
from ..modules.spec_module import build_new_plan, parse_spec_file
from ..modules.spec_runner import run_spec, run_spec_self_build


def test_run_spec(tmp_path):
    plan_name = "test_spec"
    # Create a new spec file in current working directory
    spec_file_path = build_new_plan(plan_name, "list")

    # Move it (or rewrite) into tmp_path so we can modify it safely
    final_spec_path = tmp_path / f"{plan_name}.yaml"
    Path(spec_file_path).rename(final_spec_path)

    # Add tasks to the spec
    data = yaml.safe_load(final_spec_path.read_text())
    data["tasks"] = [
        {"title": "Add", "prompt": "Write a function to add two numbers."},
        {"title": "Multiply", "prompt": "Write a function to multiply two numbers."},
        {"title": "Subtract", "prompt": "Write a function to subtract two numbers."},
        {"title": "Divide", "prompt": "Write a function to divide two numbers."},
    ]

    data["mode"] = "coder"
    data["main_model"] = TESTING_MODEL
    data["editor_model"] = TESTING_MODEL

    # Create a temporary python file and set it as editable
    test_py = tmp_path / "test_file.py"
    test_py.write_text("# initial content\n")
    data["editable_context"] = [str(test_py)]
    data["readonly_context"] = []

    final_spec_path.write_text(yaml.safe_dump(data))

    # Run the spec
    run_spec(str(final_spec_path))

    # Assert or check that expected changes occurred (example placeholder)
    # For now, just ensure no exceptions and file remains
    assert final_spec_path.exists()

    assert "def add" in test_py.read_text().lower()
    assert "def multiply" in test_py.read_text().lower()
    assert "def subtract" in test_py.read_text().lower()
    assert "def divide" in test_py.read_text().lower()


def test_run_spec_architect_mode(tmp_path):
    plan_name = "test_spec_architect"
    spec_file_path = build_new_plan(plan_name, "list")
    final_spec_path = tmp_path / f"{plan_name}.yaml"
    Path(spec_file_path).rename(final_spec_path)

    data = yaml.safe_load(final_spec_path.read_text())
    data["architect"] = True  # Set to architect mode
    data["main_model"] = TESTING_MODEL
    data["editor_model"] = TESTING_MODEL
    data["tasks"] = [
        {"title": "Add", "prompt": "Write a function to add two numbers."},
        {"title": "Multiply", "prompt": "Write a function to multiply two numbers."},
    ]

    test_py = tmp_path / "architect_file.py"
    test_py.write_text("# initial architect content\n")
    data["editable_context"] = [str(test_py)]
    data["readonly_context"] = []

    final_spec_path.write_text(yaml.safe_dump(data))

    run_spec(str(final_spec_path))

    content = test_py.read_text().lower()
    assert "def add" in content
    assert "def multiply" in content


def test_run_spec_self_build(tmp_path):
    """Test the self-build functionality of spec runner"""
    plan_name = "test_spec_self_build"
    spec_file_path = build_new_plan(plan_name, "list")
    final_spec_path = tmp_path / f"{plan_name}.yaml"
    Path(spec_file_path).rename(final_spec_path)

    # Create initial spec data with math API implementation
    data = yaml.safe_load(final_spec_path.read_text())
    data["high_level_objective"] = "Build a simple math API with basic operations"
    data[
        "implementation_details"
    ] = """
    Create a math API with separate files for each operation:
    - add.py: Contains add function
    - subtract.py: Contains subtract function
    - multiply.py: Contains multiply function
    - divide.py: Contains divide function
    
    Each function should take two parameters and return the result.
    """

    # Add just the first task as template
    data["tasks"] = [
        {
            "title": "Create add function",
            "prompt": "Create add.py with a function that takes two parameters and returns their sum. The function should be named 'add' and use type hints.",
        }
    ]

    data["main_model"] = TESTING_MODEL
    data["editor_model"] = TESTING_MODEL
    data["editable_context"] = [str(final_spec_path)]

    # Write updated spec file
    final_spec_path.write_text(yaml.safe_dump(data))

    # Run self-build
    run_spec_self_build(str(final_spec_path))

    # Read and parse updated spec
    updated_spec = parse_spec_file(str(final_spec_path))

    # Verify more tasks were added
    assert len(updated_spec.tasks) > 1, "No new tasks were added"

    # Verify first task remains unchanged
    assert updated_spec.tasks[0].title == "Create add function"

    # Verify new tasks follow similar pattern and are related to math operations
    task_titles = [task.title.lower() for task in updated_spec.tasks]
    expected_keywords = ["subtract", "multiply", "divide"]

    for keyword in expected_keywords:
        assert any(
            keyword in title for title in task_titles
        ), f"No task found for {keyword} operation"

    # Verify each task has a title and prompt
    for task in updated_spec.tasks:
        assert task.title, "Task missing title"
        assert task.prompt, "Task missing prompt"


def test_new_spec_with_context_file(tmp_path):
    """Test creating a new spec with a context file"""
    # Create a test context file
    context_file = tmp_path / ".aider-context"
    context_content = """
/drop
/add       src/file1.py
/add       src/file2.py
/add       src/file3.py
/read-only  docs/readme.md
/read-only  docs/api.md
"""
    context_file.write_text(context_content)

    # Create new spec with context file
    spec_path = build_new_plan(
        str(tmp_path / "test_plan"), "list", context_file=str(context_file)
    )

    # Load and verify the spec
    spec = parse_spec_file(spec_path)

    # Verify editable context
    assert len(spec.editable_context) == 3
    assert "src/file1.py" in spec.editable_context
    assert "src/file2.py" in spec.editable_context
    assert "src/file3.py" in spec.editable_context

    # Verify readonly context
    assert len(spec.readonly_context) == 2
    assert "docs/readme.md" in spec.readonly_context
    assert "docs/api.md" in spec.readonly_context


def test_new_spec_with_complex_context_file(tmp_path):
    """Test creating spec with complex context file including mixed order and duplicates"""
    context_file = tmp_path / ".aider-context"
    context_content = """
/drop
/add       src/file1.py
/read-only  docs/readme.md
/add       src/file2.py
/drop
/read-only  docs/api.md
/add       src/file1.py  # Duplicate entry
/read-only  docs/readme.md  # Duplicate entry
/invalid    something.txt
random line
/add       src/file3.py
"""
    context_file.write_text(context_content)

    spec_path = build_new_plan(
        str(tmp_path / "test_complex"), "list", context_file=str(context_file)
    )

    spec = parse_spec_file(spec_path)

    # Verify editable context (should deduplicate)
    assert len(spec.editable_context) == 3
    assert "src/file1.py" in spec.editable_context
    assert "src/file2.py" in spec.editable_context
    assert "src/file3.py" in spec.editable_context

    # Verify readonly context (should deduplicate)
    assert len(spec.readonly_context) == 2
    assert "docs/readme.md" in spec.readonly_context
    assert "docs/api.md" in spec.readonly_context


def test_new_spec_with_empty_context_file(tmp_path):
    """Test creating spec with empty context file"""
    context_file = tmp_path / ".aider-context"
    context_file.write_text("")

    spec_path = build_new_plan(
        str(tmp_path / "test_empty"), "list", context_file=str(context_file)
    )

    spec = parse_spec_file(spec_path)

    assert len(spec.editable_context) == 0
    assert len(spec.readonly_context) == 0


@pytest.mark.parametrize(
    "template_content, context_content, expected_content",
    [
        (
            """editable_context: {{editable_context}}
readonly_context: {{readonly_context}}""",
            """
/add       src/file1.py
/read-only  docs/readme.md
""",
            """editable_context:
  - "src/file1.py"
readonly_context:
  - "docs/readme.md"
""",
        ),
        (
            """editable_context: {{editable_context}}
readonly_context: {{readonly_context}}""",
            "",  # Empty context file
            """editable_context:
  - "./path/to/file.py"
readonly_context:
  - "./path/to/file.py"
""",
        ),
        (
            """editable_context: {{editable_context}}
readonly_context: {{readonly_context}}""",
            """
/add       src/file1.py
/add       src/file2.py
/read-only  docs/readme.md
/read-only  docs/api.md
""",
            """editable_context:
  - "src/file1.py"
  - "src/file2.py"
readonly_context:
  - "docs/readme.md"
  - "docs/api.md"
""",
        ),
    ],
)
def test_replace_context_in_template(tmp_path, template_content, context_content, expected_content):
    # Create a temporary context file
    context_file = tmp_path / ".aider-context"
    context_file.write_text(context_content)

    # Call the function
    updated_content = replace_context_in_template(template_content, str(context_file))

    # Assert the content matches the expected result
    assert updated_content == expected_content


def test_new_spec_with_only_drops_context_file(tmp_path):
    """Test creating spec with context file containing only /drop commands"""
    context_file = tmp_path / ".aider-context"
    context_file.write_text(
        """
/drop
/drop
/drop
"""
    )

    spec_path = build_new_plan(
        str(tmp_path / "test_drops"), "list", context_file=str(context_file)
    )

    spec = parse_spec_file(spec_path)

    assert len(spec.editable_context) == 0
    assert len(spec.readonly_context) == 0


def test_new_spec_context_file_integration(tmp_path):
    """Test full integration flow with context file"""
    # Create context file
    context_file = tmp_path / ".aider-context"
    context_content = """
/add       src/math.py
/add       src/utils.py
/read-only  docs/readme.md
"""
    context_file.write_text(context_content)

    # Create spec with context
    spec_path = build_new_plan(
        str(tmp_path / "test_integration"), "list", context_file=str(context_file)
    )

    # Verify spec was created with correct contexts
    spec = parse_spec_file(spec_path)
    assert "src/math.py" in spec.editable_context
    assert "src/utils.py" in spec.editable_context
    assert "docs/readme.md" in spec.readonly_context

    # Generate load file from spec
    load_file_path = spec_file_to_load_file(spec_path)
    load_content = Path(load_file_path).read_text()

    # Verify load file contains correct entries
    assert "/add       src/math.py" in load_content
    assert "/add       src/utils.py" in load_content
    assert "/read-only docs/readme.md" in load_content
