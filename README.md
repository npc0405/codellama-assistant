# CodeLlama Assistant

A local AI-powered Python code assistant using **CodeLlama** (via Ollama), with both a **CLI** and a **Streamlit web app** interface. Supports code generation, explanation, debugging, and optimization.

---

## Project Structure
codellama-assistant/
├── pyproject.toml
├── uv.lock
├── .venv/
├── model_config.py # Model/client setup
├── prompts.py # Prompt templates for each task type
├── assistant.py # Core logic (generate/explain/debug/optimize)
├── cli.py # CLI menu interface
└── streamlit_app.py # Streamlit web app


---

## 1. Prerequisites

- macOS (Apple Silicon or Intel)
- [Homebrew](https://brew.sh/) installed
- Python 3.12+ (managed automatically by `uv`)

---

## 2. Install Ollama

```bash
brew install ollama
```

Or download the app directly from [ollama.com](https://ollama.com) (runs as a menu bar app and auto-starts the server).

If installed via Homebrew, start the server manually:

```bash
ollama serve &
```

---

## 3. Pull the CodeLlama model

```bash
ollama pull codellama:7b
```

Verify it's installed:

```bash
ollama list
```

You should see `codellama:7b` in the output. Quick sanity check:

```bash
ollama run codellama:7b "print hello world in python"
```

> **Note:** If your Mac has 8GB RAM, close other heavy apps while running the model. For a lighter footprint, use a quantized variant like `codellama:7b-instruct-q4_0`.

---

## 4. Set up the Python project with `uv`

Install `uv` (if not already installed):

```bash
brew install uv
```

Clone/navigate to the project, then install dependencies:

```bash
cd codellama-assistant
uv add ollama streamlit
```

This creates `.venv/` and `uv.lock` automatically — no manual venv activation needed.

---

## 5. Running the CLI version

```bash
uv run python cli.py
```

You'll see a menu:

===== CodeLlama Assistant =====

Generate code
Explain code
Fix bug
Exit


- **Generate code** — describe what you want, get code back.
- **Explain code** — paste code, type `END` on a new line to submit.
- **Fix bug** — paste buggy code + optional error message.

---

## 6. Running the Streamlit app

```bash
uv run streamlit run streamlit_app.py
```

This opens a browser tab at `http://localhost:8501` with:

- A text area for code/prompt input
- A dropdown: **Generate Code / Explain Code / Debug Code / Optimize Code**
- An optional error-message field (shown only for Debug Code)
- A **Run** button that calls CodeLlama and renders the output as formatted markdown

---

## 7. Changing the model

To use a different model (e.g. `qwen2.5:7b`), edit `model_config.py`:

```python
MODEL_NAME = "codellama:7b"   # change this
```

Make sure the model is pulled first via `ollama pull <model-name>`.

---

## 8. Troubleshooting

| Issue | Fix |
|---|---|
| `model 'codellama' not found (404)` | Use the exact tag from `ollama list`, e.g. `codellama:7b` |
| Connection refused / no response | Run `ollama serve` to start the server |
| Streamlit page blank/errors | Check terminal logs; ensure `uv add streamlit` completed successfully |
| Slow responses | Try a quantized model variant, or close other memory-heavy apps |

---

## Tech Stack

- [Ollama](https://ollama.com) — local LLM runtime
- [CodeLlama](https://ollama.com/library/codellama) — code-focused LLM
- [Streamlit](https://streamlit.io) — web app UI
- [uv](https://docs.astral.sh/uv/) — Python package/project manager
