# TRIZ Agents

Multi-agent LLM workflow that applies the **TRIZ** methodology to complex engineering problems.
Implements a supervisor-routed LangGraph of specialized agents (Project Manager, TRIZ Specialist, Mechanical/Electrical/Control/Safety Engineers, Operations & Documentation), plus TRIZ-specific tools (features list, contradiction matrix, inventive principles) and an optional TRIZ RAG.

> The accompanying paper see: [TRIZ Agents: A Multi-Agent LLM Approach for TRIZ-Based Innovation](https://arxiv.org/abs/2506.18783)

---

## ✨ What’s inside

* **Agent workflow (LangGraph):** Supervisor (Project Manager) routes work among domain agents, tool calls are separate tool nodes.
* **LLM providers via LangChain:** OpenAI (GPT-4o, o\*), Google Gemini (1.5/2.5), DeepSeek, xAI (Grok). Easy to add more.
* **TRIZ tools:**

  * 39 features list
  * Contradiction matrix → suggested inventive principles
  * Inventive principles lookup
  * Optional TRIZ **RAG** over PDFs (Chroma + OpenAI Embeddings)
* **Experiments:** One-shot or batch runs, JSON/Markdown artifacts.
* **Evaluation:** Multi-judge scoring (clarity, coherence, coverage, novelty, feasibility, TRIZ-adherence, expert-alignment).
* **Notebook:** `quickstart.ipynb` for end-to-end runs + graph visualization.

---

## 🧰 Requirements & install

### 1) Python deps

Use our curated `requirements.txt`:

```bash
pip install -r requirements.txt
```
```bash
pip install -e .
```

Notes:

* On Windows, `faiss-cpu` is skipped; Chroma will still work.
* For local graph rendering, also install:

  ```bash
  pip install graphviz pygraphviz  # or 'pydot'
  # and install Graphviz system binaries via apt/brew/choco
  ```

### 2) Environment variables (`.env`)

Create a `.env` in repo root (copy from `.env.example`):

```env
# Providers (fill only what you need)
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=AIza...
XAI_API_KEY=xai-...
DEEPSEEK_API_KEY=sk-deepseek-...

# LangChain Hub (for pulling prompts used by prompt_templates.py)
LANGCHAIN_API_KEY=ls_...

# Tavily (web search tool)
TAVILY_API_KEY=tvly-...
```

The notebook and modules use `python-dotenv` to load this automatically.

---

## 🚀 Quickstart (Notebook)

Open **`notebooks/quickstart.ipynb`** and run the cells:

* Installs (optional)
* Loads `.env`
* Lets you pick the **agent model** and **evaluator models**
* **Visualizes** the LangGraph (offline Graphviz first; Mermaid fallback)
* Runs a full **TRIZ workflow** on a gantry crane problem
* Saves a JSON artifact under `experiments/` and a Markdown summary
* Runs **multi-judge evaluation** (default: `expert_solution` metric)

If Mermaid remote rendering fails (HTTP 502), the notebook falls back to **local Graphviz** or writes Mermaid source (`workflow.mmd`) with CLI instructions (`mmdc`) to render offline.

---

## 🔧 CLI-style usage (from Python)

```python
from triz_agents import create_workflow_app, run_experiment, run_multi_judge_evaluation

# 1) Run an experiment
res = run_experiment(
    model_name="gpt-4o",
    thread_id="gantry-01",
    temperature=0.0,
    out_dir="experiments",
)

# 2) Evaluate with multiple judges
from pathlib import Path
prediction_text = Path("gpt-4o_gantry_*.md").read_text(encoding="utf-8")  # or your artifact path
report = run_multi_judge_evaluation(
    evaluator_models=["o1", "grok-3", "gemini-2.5-pro"],
    input_problem="(the gantry crane problem text...)",
    prediction=prediction_text,
    metrics=["expert_solution"],   # add clarity, coherence, etc.
)
```

---

## 🧱 TRIZ data files

`src/triz_agents/tools/triz_tools.py` expects:

* `src/triz_agents/tools/sources/triz_matrix.xls`
* `src/triz_agents/tools/sources/triz_principles.json`
* `src/triz_agents/tools/sources/triz_features.txt`

Place your files there or update the paths in `triz_tools.py`.
The contradiction matrix is read via Pandas; column/index names are normalized to lowercase/stripped.

---

## 📚 RAG (optional)

`tools/rag_tools.py` can build a small TRIZ RAG over PDFs:

* Put your PDFs under `./triz_books/` (or edit the directory).
* Requires `chromadb`, `OpenAIEmbeddings` (so set `OPENAI_API_KEY`).
* The tool function is `rag_triz_tool(question: str)`.

> If you don’t plan to use RAG immediately, the imports are safe; the tool won’t run until invoked.

---

## 🧪 Experiments & evaluation

* **Run single/batch experiments:** `experiments.py` exposes `run_experiment` and `run_batch`.
* **Artifacts:** JSON (steps + metadata) and a Markdown summary for evaluation pipelines.
* **Evaluation:** `evaluation.py` offers multi-judge scoring across metrics (default is just **expert\_solution**). Judges are any models supported by `llm.get_llm()`.

Tip: Use **low temperature** for judges (the code defaults to deterministic settings).

---

## 🧩 LLM providers

`llm.py` maps friendly model names → provider classes:

* OpenAI: `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`, `gpt-4.1-mini`, `o1`, `o3`, `o4-mini`
* Google: `gemini-1.5-flash`, `gemini-1.5-pro`, `gemini-2.5-flash`, `gemini-2.5-pro`
* DeepSeek: `deepseek-chat`
* xAI: `grok-3`, `grok-3-mini`

You can add your own by extending `MODEL_PROVIDER_MAP`.

---

## 🐞 Troubleshooting

* **Mermaid 502** when rendering the graph:

  * The notebook now prefers **offline Graphviz** (`draw_png`/`draw_svg`) and only falls back to Mermaid’s web renderer if needed.
  * Install `graphviz` + `pygraphviz` (or `pydot`) and system binaries.
* **TRIZ tools can’t find files**:

  * Check paths under `src/triz_agents/tools/sources/`.
* **RAG fails**:

  * Ensure `OPENAI_API_KEY` is set and Chroma is installed.
  * If on Windows without FAISS, Chroma will still work (disk/vector backends).

---

## 📝 Citing

If you use this project, please cite the paper:

```
@article{szczepanik2025triz,
  title={TRIZ Agents: A Multi-Agent LLM Approach for TRIZ-Based Innovation},
  author={Szczepanik, Kamil and Chudziak, Jaros{\'L} and others},
  journal={arXiv preprint arXiv:2506.18783},
  year={2025}
}
```

---

## 📄 License

MIT

