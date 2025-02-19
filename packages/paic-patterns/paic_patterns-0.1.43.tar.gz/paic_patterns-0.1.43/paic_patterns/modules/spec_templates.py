template_spec_file_list = """plan_name: "{{plan_name}}"

pattern: list

architect: true

main_model: "{{main_model}}"

editor_model: "{{editor_model}}" # used only if mode is "architect: true"

# Code you want your AI Coding Assistant to edit
editable_context:{{editable_context}}

# Code you want your AI Coding Assistant to read but not edit
readonly_context:{{readonly_context}}

high_level_objective: "high level objective of the feature you're implementing"

implementation_details: |
    implementation details of the feature you're implementing

# your list of tasks aka prompts that will be executed in order one by one
tasks:
  - title: "high level description"
    prompt: |
      high to low level coding prompt
"""
