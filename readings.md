# Readings before Tier 1

The **notebooks are the course.** These pages are a second voice. Read the prose; skip install steps unless a page is marked for technical staff. **Do not** paste ministry files, CVs, Cabinet text, or scans into any demo box.

## What everyone does

| Order | Do this | Time | Skip if |
|---|---|---|---|
| 1 | [PREP-00](PREP-00_how_colab_works.ipynb) in Colab | 15–25 min | You already use Colab or Jupyter |
| 2 | **[PREP-00b](PREP-00b_python_enough_to_follow.ipynb)** — very basic Python, only what the notebooks use | 30–40 min | You already read Python at work |
| 3 | Hugging Face LLM Course, [Chapter 1](https://huggingface.co/learn/llm-course/chapter1/1) (stop when they ask you to run their code) | 20–40 min | — |
| 4 | Then PREP-01 → 02 → 03 | as in the [README](README.md) | — |

PREP-00b is the Python requirement. You do **not** need a local Python install. Colab already has it.

## By notebook (everyone)

### With PREP-00 — notebooks

- [Project Jupyter, Getting started](https://docs.jupyter.org/en/latest/start/index.html) — what a notebook is if you will use JupyterLab in the room instead of Colab. Skim. You still launch PREP-00 in **Colab** this week.

### With PREP-00b — very basic Python (required if you have never seen Python)

This is **not** a programming course. You learn to follow `# [CHANGE]` lines.

**Required:** the Colab notebook PREP-00b (quotes, labels, `print`, `import`, a labelled form, when a cell goes red).

**Optional extra** (only if PREP-00b felt easy and you want the same ideas in official docs). Use a browser; do not install Python. Stop at the end of section 4. Skip exercises that need a local terminal.

- [The Python Tutorial, sections 1–4](https://docs.python.org/3/tutorial/index.html)  
  — [1. Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)  
  — [2. Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html) (you can skip; Colab *is* the interpreter)  
  — [3. An Informal Introduction](https://docs.python.org/3/tutorial/introduction.html) (strings, numbers — this maps to PREP-00b)  
  — [4. More Control Flow](https://docs.python.org/3/tutorial/controlflow.html) (skim `if` / `for`; you will **see** these, not write them)

Alternative workshop-style pages (same limit: three pages, then stop):

- [Software Carpentry — Variables](https://swcarpentry.github.io/python-novice-gapminder/02-variables.html)
- [Data Types](https://swcarpentry.github.io/python-novice-gapminder/03-types-conversion.html)
- [Built-in Functions](https://swcarpentry.github.io/python-novice-gapminder/04-built-in.html)

Do **not** start Codecademy, pandas, or “Python in 30 days.”

### With PREP-01 — what a language model is; open vs open-weight

- [Hugging Face LLM Course, Chapter 1](https://huggingface.co/learn/llm-course/chapter1/1) — **everyone.** Stop at the first “run this code” block.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — visual. Optional if Chapter 1 was enough. You do not need the maths. Day 1 T1-02 will go slowly.
- [Open Source Initiative — Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) — **everyone who will hear “open source” in the room.** Hold one distinction: **open-weight** (you can download the files) is not the same as **OSAID open source** (data, code, and weights are inspectable). T1-04 uses this.
- Tokens you can see: paste a *fictional* CivicDesk sentence into [tiktokenizer.vercel.app](https://tiktokenizer.vercel.app/). No OpenAI account.

### With PREP-02 — retrieve, then generate; messy documents

- [IBM, What is RAG?](https://www.ibm.com/think/topics/retrieval-augmented-generation) — retrieve an approved paragraph, *then* generate. If it is missing, stop.

**Optional awareness** (you will not clean ministry files in this prep or in the room):

- [Tesseract — Improving the quality of the output](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html) — **paper → softcopy.** Skim headings only: resolution, contrast, skew, image vs searchable PDF. A bad scan becomes a bad index. Do **not** install Tesseract. Do **not** upload a real page.
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) and [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) — **optional, technical staff only.** Day 2 classification is *INDEX vs NEVER*, not a pandas lab. If you open these, use toy tables, never a ministry extract.

### With PREP-03 — frozen weights; where models come from; security

- Hugging Face “Fine-tuning” [first screen](https://huggingface.co/docs/transformers/training) — a small extra file can sit on frozen weights; it is not a database. You will **not** train.

**For technical staff** (where models come from):

- [Hugging Face model cards](https://huggingface.co/docs/hub/model-cards) — who published it, licence, intended use. T1-04 reads excerpts; this is the live guide.
- [Hugging Face Hub security](https://huggingface.co/docs/hub/security) — official org vs a random fork; why you pin a revision. The course pins OLMo and Phi for you; you should still know the question.

**For IT and policy staff** (security and governance) — skim, do not implement:

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — prompt injection, excessive agency, sensitive-info disclosure. Day 3 T1-13 is the classroom version of “the model must not call tools.”
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — Govern / Map / Measure / Manage. AUX-04 is a one-page DPIA *sketch*, not a NIST assessment.

Optional listen: [3Blue1Brown, But what is a GPT?](https://www.youtube.com/watch?v=wjZofJX3UZc) (~25 min). Skip if you are tired.

## Do not start here

- Installing Python, Anaconda, Tesseract, or pandas on a ministry laptop for this prep.
- Full Software Carpentry, Codecademy, or sections 5+ of the Python Tutorial.
- “Build an agent” blogs — Day 3 is about **not** calling tools.
- Ministry manuals, EDMS exports, live tickets, scanned CVs — data ban.
