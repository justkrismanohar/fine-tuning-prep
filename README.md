# Prep before Tier 1 — no coding required

This folder is **optional pre-work** for people who have never written Python and have not sat a language-model course. It is not Tier 1. It does not start OLMo. It does not connect to a ministry system.

**Aim:** after two or three evenings (about **3–4½ hours** including PREP-00b and one short reading) you can walk into Day 1 and:

- click **Run** on a notebook cell without panic
- follow a notebook with **very basic Python** (PREP-00b): quotes, labels, `print`, `import`, a labelled form — you still do not write programs
- say what a language model is *doing* (guessing the next chunk of text — not looking up your EDMS)
- keep **work files out** of cells
- tell **prompt / RAG / a database / a human** apart at the level of a sentence
- know that **citing a handbook** is different from **being allowed to see it**, and that **chat is not allowed to reset a password**

You will still learn the real labs in the room. This only gives you the words.

## What you need

- A **Google account** (any Gmail / Workspace account)
- A browser (Chrome, Edge, Firefox)
- No GPU, no Python install, no Git, no Docker
- CivicDesk **fiction only** — same data ban as the course

## Open a notebook in Google Colab

Each notebook below has an **Open in Colab** badge. That is the intended launch.

If a badge fails (the file is not on GitHub yet, or your network blocks it), upload by hand. That always works.

### A. Click the badge (preferred)

1. Open this README in your browser.
2. Click **Open in Colab** on the notebook for tonight.
3. Sign in with Google if asked.
4. At the top: **Runtime → Change runtime type → CPU** (not GPU). Save.
5. **Runtime → Run all**, or click the ▶ on each cell from the top down.
6. Read the teaching note *under* a cell after it runs.

Direct links (same as the badges):

| Night | Notebook | Colab |
|---|---|---|
| 0 — if notebooks are new to you | [PREP-00](PREP-00_how_colab_works.ipynb) | [Open in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-00_how_colab_works.ipynb) |
| 0b — no Python yet | [PREP-00b](PREP-00b_python_enough_to_follow.ipynb) | [Open in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-00b_python_enough_to_follow.ipynb) |
| 1 — Day 1 words | [PREP-01](PREP-01_what_a_model_is.ipynb) | [Open in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-01_what_a_model_is.ipynb) |
| 2 — Day 2 words | [PREP-02](PREP-02_retrieve_and_cite.ipynb) | [Open in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-02_retrieve_and_cite.ipynb) |
| 3 — Day 3 words | [PREP-03](PREP-03_frozen_and_boundary.ipynb) | [Open in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-03_frozen_and_boundary.ipynb) |

### B. Upload the file (always works)

1. Go to [https://colab.research.google.com/](https://colab.research.google.com/).
2. Sign in.
3. **File → Upload notebook**.
4. Choose the `.ipynb` from this `prep/` folder (email, USB, or shared drive).
5. **Runtime → CPU**, then **Run all**.

## Very basic Python (everyone who has never seen it)

**PREP-00b is the requirement.** Thirty to forty minutes in Colab. It is only the syntax you will *see* in Tier 1 (`# [CHANGE]`, quotes, a label, `print`, `import lab`, a `{ "field": "value" }` form). You do not write a program from a blank page. You do not install Python.

Optional extra, after 00b, if you want official docs: [Python Tutorial sections 1–4](https://docs.python.org/3/tutorial/index.html) in a browser only — details in [readings.md](readings.md). Skip section 2’s install steps. Stop at section 4. Jupyter’s [Getting started](https://docs.jupyter.org/en/latest/start/index.html) is the same idea as PREP-00 if you will use JupyterLab in the room.

### If a cell shows a red error

Read the message once. The usual fix is: you deleted a quote `"` or a comma. Undo, or reload the notebook and change only the word inside the quotes. There is a worked copy in `completed/` for facilitators — do not start there.

## Suggested calendar

| When | Do this | Time |
|---|---|---|
| **First sitting** | PREP-00 (skip if you already use Colab/Jupyter) then **PREP-00b** | 20 min + 30–40 min |
| **Same night or the next** | Hugging Face [LLM Course ch. 1](https://huggingface.co/learn/llm-course/chapter1/1) (stop at their first code block), then PREP-01 | 20–40 min + 50–70 min |
| **Second sitting** | IBM RAG page (optional Illustrated Transformer if you like pictures), then PREP-02 | 15 min + 50–70 min |
| **Third sitting** | OSI [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) (everyone); IT/policy skim OWASP LLM Top 10; technical staff skim a model card page — then PREP-03 | 15–25 min + 40–55 min |

Do **not** skip PREP-00b if you have never seen Python. Do **not** skip the data ban in PREP-01.

Full list, including pandas, Tesseract (scan quality), Hub security, and NIST: [readings.md](readings.md). Those are **awareness** pages. Do not install Tesseract or pandas for this prep. Do not upload a real scan.

## Data ban (read before you open Colab)

Do **not** paste: real CVs, Cabinet or EDMS text, case files, health records, burgess applications, patrol notes, passwords, live GLPI/GIS/serial dumps, or anything that came from a ministry system.

CivicDesk names in the notebooks are **fiction**. If you want to practise a sentence, invent one.

## What this prep is not

- Not a Python course (PREP-00b is literacy to *follow* cells; the Python Tutorial 1–4 is optional extra, not a substitute)
- Not permission to use ChatGPT on work files
- Not the Day 1–3 labs (those stay in `tier1/`)
- Not a substitute for the opening pre-test in the room

## You are ready for Day 1 if you can say, out loud

1. A language model **continues text**. It is not the ministry database.
2. **System** text is the standing instruction; **user** text is this visitor’s question.
3. **Open-weight** means you can host the files; it does not mean the training data is public.
4. If the handbook paragraph is not in the prompt, an honest reply is **I cannot cite** — not an invented circular.
5. A **hit in a search index** is not permission to show the paragraph.
6. Chat may **draft**; it may not **reset a password, hire, grade, or award**.
7. Nothing from work goes in a cell.
8. `# [CHANGE]` means: edit the text inside the quotes; leave the rest of the cell alone.

Print [prep_quick_card.md](prep_quick_card.md) and bring it if you like. The room will give you Day 1 materials; you do not need this folder on a USB unless you want your notes.
