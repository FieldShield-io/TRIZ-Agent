from triz_agents.graph import build_graph
from langchain.prompts import ChatPromptTemplate

if __name__ == "__main__":
    prompts = {
        "project_manager": ChatPromptTemplate.from_template(open("configs/prompts/project_manager.md").read()),
        "mechanical_engineer": ChatPromptTemplate.from_template(open("configs/prompts/mechanical_engineer.md").read()),
    }
    app = build_graph(prompts)
    print("Graph compiled:", type(app))
