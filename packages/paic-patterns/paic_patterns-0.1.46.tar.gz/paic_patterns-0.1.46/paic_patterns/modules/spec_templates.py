template_spec_file_list = """plan_name: "__plan_name__"

pattern: list

architect: true

main_model: "__main_model__"

# used only if mode is "architect: true"
editor_model: "__editor_model__"

# Code you want your AI Coding Assistant to edit
editable_context: __editable_context__

# Code you want your AI Coding Assistant to read but not edit
readonly_context: __readonly_context__

high_level_objective: "high level objective of the feature you're implementing"

implementation_details: |
    implementation details of the feature you're implementing

# your list of tasks aka prompts that will be executed in order one by one
tasks:
  - title: "Task 1: high level description"
    prompt: |
      high to low level coding prompt for task 1
  
  - title: "Task 2: high level description"
    prompt: |
      high to low level coding prompt for task 2
  
  - title: "Task 3: high level description"
    prompt: |
      high to low level coding prompt for task 3
"""

template_spec_file_list_reflection = """plan_name: "__plan_name__"

pattern: list-reflection

architect: true

main_model: "__main_model__"

# used only if mode is "architect: true"
editor_model: "__editor_model__" 

# Code you want your AI Coding Assistant to edit
editable_context: __editable_context__

# Code you want your AI Coding Assistant to read but not edit
readonly_context: __readonly_context__

high_level_objective: "high level objective of the feature you're implementing"

implementation_details: |
    implementation details of the feature you're implementing

# your list of tasks aka prompts that will be executed in order one by one
tasks:
  - title: "Task 1: high level description"
    prompt: |
      high to low level coding prompt for task 1
    reflection_count: 1
  
  - title: "Task 2: high level description"
    prompt: |
      high to low level coding prompt for task 2
    reflection_count: 1
  
  - title: "Task 3: high level description"
    prompt: |
      high to low level coding prompt for task 3
    reflection_count: 1
"""
