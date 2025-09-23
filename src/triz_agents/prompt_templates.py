"""Central place to pull and expose all role prompts for TRIZ Agents."""
from langchain import hub

project_manager_prompt = hub.pull("kamilsz/triz-agents-project-manager")
mechanical_engineer_prompt = hub.pull("kamilsz/triz-agents-mechanical-engineer")
electrical_engineer_prompt = hub.pull("kamilsz/triz-agents-electrical-engineer")
control_systems_engineer_prompt = hub.pull("kamilsz/triz-agents-control-systems-engineer")
safety_engineer_prompt = hub.pull("kamilsz/triz-agents-safety-engineer")
triz_specialist_prompt = hub.pull("kamilsz/triz-agents-triz-specialist")
software_engineer_prompt = hub.pull("kamilsz/triz-agents-software-engineer")
operations_specialist_prompt = hub.pull("kamilsz/triz-agents-operations-specialist")
documentation_specialist_prompt = hub.pull("kamilsz/triz-agents-documentation-specialist")
final_report_maker_prompt = hub.pull("kamilsz/triz-agents-final-report-maker")
# Dictionary of all prompts for easy access
all_prompts = {
    "project_manager": project_manager_prompt,
    "mechanical_engineer": mechanical_engineer_prompt,
    "electrical_engineer": electrical_engineer_prompt,
    "control_systems_engineer": control_systems_engineer_prompt,
    "safety_engineer": safety_engineer_prompt,
    "triz_specialist": triz_specialist_prompt,
    "software_engineer": software_engineer_prompt,
    "operations_specialist": operations_specialist_prompt,
    "documentation_specialist": documentation_specialist_prompt,
    "final_report_maker": final_report_maker_prompt,
}
