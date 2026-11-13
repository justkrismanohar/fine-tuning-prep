"""Write no-code Colab prep notebooks (PREP-00 … PREP-03)."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
GH = "justkrismanohar/fine-tuning-build"
COLAB = f"https://colab.research.google.com/github/{GH}/blob/main/prep"


def md(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source.strip("\n").split("\n")],
    }


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "metadata": {},
        "outputs": [],
        "execution_count": None,
        "source": [line + "\n" for line in source.strip("\n").split("\n")],
    }


def nb(name: str, cells: list[dict]) -> dict:
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
            "colab": {"name": name, "provenance": [], "toc_visible": True},
        },
        "cells": cells,
    }


def write(filename: str, cells: list[dict]) -> None:
    path = HERE / filename
    path.write_text(json.dumps(nb(filename, cells), indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", path.name)


def badge(filename: str) -> str:
    url = f"{COLAB}/{filename}"
    img = "https://colab.research.google.com/assets/colab-badge.svg"
    return f"[![Open In Colab]({img})]({url})\n\nOr: **File → Upload notebook** at [colab.research.google.com](https://colab.research.google.com/) and choose `{filename}`."


BANNER = """
**How to use this notebook (no coding)**

1. **Runtime → Change runtime type → CPU** (not GPU). You do not need a graphics card.
2. Click ▶ on each cell from the top, or **Runtime → Run all**.
3. Read the note *under* a cell after it runs.
4. Change **only** lines marked `# [CHANGE]` — usually one word inside quotes `"..."`. Do not delete the quotes.
5. Nothing from work goes in a cell. CivicDesk names are fiction.

You are not learning Python. You are practising the same click-and-read path that no-code people use on Day 1.
"""

# ---------------------------------------------------------------------------
# PREP-00
# ---------------------------------------------------------------------------
write(
    "PREP-00_how_colab_works.ipynb",
    [
        md(
            f"""# PREP-00 How to click Run (Google Colab)

**Time:** 15–25 minutes &nbsp;|&nbsp; **Need this if:** you have never used Colab or Jupyter

{badge("PREP-00_how_colab_works.ipynb")}

"""
            + BANNER
        ),
        md(
            """## What a notebook is

A notebook is a **page of boxes**.

| Box | What it is | What you do |
|---|---|---|
| Text (this box) | Teaching | Read it |
| Code (grey box with `[ ]` on the left) | Instructions the computer runs | Click ▶ |

When a code box has run, a number appears: `[1]`, `[2]`. Output prints **under** the box.

You will not install anything. Colab is a website. Close the tab when you are done.

```
  ┌─────────────────────────────┐
  │  text: the lesson           │
  └─────────────────────────────┘
  ┌─────────────────────────────┐
  │  [ ▶ ]  a few lines         │  ← click here
  │                             │
  │  output appears underneath  │
  └─────────────────────────────┘
```
"""
        ),
        md(
            """## 1. Run your first cell

Click the ▶ to the left of the next box. You should see one sentence print underneath.
"""
        ),
        code(
            """print("If you can read this line under the box, the cell ran. You are ready.")
"""
        ),
        md(
            """### If nothing happened

- You must be **signed in** to Google.
- Click inside the box first, then ▶, or press **Shift+Enter**.
- If Colab asks to connect, click **Connect** (top right).

That is the only mechanical skill Day 1 will ask of no-code people: **run the next cell**.
"""
        ),
        md(
            """## 2. Change a word in quotes

Lines that start with `#` are notes for humans. The computer ignores them.

`# [CHANGE]` means: edit the text **inside the quotes**. Keep both quote marks.

The next cell says `YOUR_NAME = "Ada"`. Put your first name in the quotes, then run.
"""
        ),
        code(
            """# [CHANGE] put your first name inside the quotes. Keep the quotes.
YOUR_NAME = "Ada"

print("Hello,", YOUR_NAME)
print("You changed a label. That is all the 'code' this prep will ask of you.")
"""
        ),
        md(
            """### Teaching note

- `"Ada"` is **text**. The quotes mark where the text starts and ends.
- If you see `SyntaxError`, a quote is missing. Put it back and run again.
- You did not write a program. You filled a form that happens to live in a code box.

On Day 1 the same pattern appears as `BACKEND = "demo"` and `WHICH_MODEL = "olmo"`. You change the word, you run the cell.
"""
        ),
        md(
            """## 3. Run all

Menus: **Runtime → Run all**. Every code box runs from the top. Use that when you reopen a notebook.

You do **not** need a GPU. If Colab offers T4 / GPU, pick **CPU**. GPU is for later classroom servers, not this prep.
"""
        ),
        code(
            """print("Runtime → Run all is the same as clicking ▶ on every code box, in order.")
print("Stay on CPU for this prep.")
"""
        ),
        md(
            """## 4. Data ban (one line, then the room will repeat it)

If it came from a **ministry system**, it does not go in a cell. Not a CV, not a Cabinet sentence, not a password, not a live ticket.

The next cell is a dummy sentence. Do **not** replace it with a real one.
"""
        ),
        code(
            """# [CHANGE] you may invent a CivicDesk sentence. Do not paste work files.
PRACTICE = "CivicDesk Circular HB-ATTACH-04 is fiction."

print("You typed", len(PRACTICE.split()), "words.")
print("If those words came from a real EDMS, delete them and start again.")
"""
        ),
        md(
            """## Done

Next: **PREP-00b** — the few Python shapes you will *see* in the labs (you still do not write programs). [Open PREP-00b in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-00b_python_enough_to_follow.ipynb).

If you already knew Colab, skip this file and still do 00b unless you already read Python for a living.
"""
        ),
    ],
)

# ---------------------------------------------------------------------------
# PREP-00b — minimum Python to follow a notebook
# ---------------------------------------------------------------------------
write(
    "PREP-00b_python_enough_to_follow.ipynb",
    [
        md(
            f"""# PREP-00b Python: enough to follow a notebook

**Time:** 30–40 minutes &nbsp;|&nbsp; **Need this if:** you have never written Python (most of the room)

{badge("PREP-00b_python_enough_to_follow.ipynb")}

"""
            + BANNER
        ),
        md(
            """## What this is — and is not

Python is the **language in the grey boxes**. Colab already speaks it. You are **not** becoming a programmer. You will not install Python. You will not write a script from a blank page.

You only need to **recognise** six shapes that appear in Day 1–3, so a `# [CHANGE]` line is not a foreign language.

| You will… | You will not… |
|---|---|
| Change a word inside `"quotes"` | Invent new functions |
| Run a cell that says `import ...` | Understand every library |
| Fill a labelled form `{ "owner": "..." }` | Learn data science or pandas |
| Read a `print(...)` as “show this underneath” | Debug other people’s code |

This notebook is the **whole Python requirement** for the room.

Optional extra, only if this notebook felt easy: [Python Tutorial, sections 1–4](https://docs.python.org/3/tutorial/index.html) in a browser. Do not install Python. Skip section 2’s local interpreter. Stop at the end of section 4 (`if` / `for` — you will *see* them, not write them). Same ideas in workshop form: Software Carpentry [variables](https://swcarpentry.github.io/python-novice-gapminder/02-variables.html), [types](https://swcarpentry.github.io/python-novice-gapminder/03-types-conversion.html), [functions](https://swcarpentry.github.io/python-novice-gapminder/04-built-in.html). If those feel like a course, close them.

Full reading list (Hugging Face, OSI, scan quality, OWASP): [readings.md](https://github.com/justkrismanohar/fine-tuning-build/blob/main/prep/readings.md).
"""
        ),
        md(
            """## 1. A comment vs a line the computer runs

`#` starts a **note for humans**. Everything after `#` on that line is ignored.

In this course the notes are tagged:

| Tag | Meaning |
|---|---|
| `# [RUN]` | Click ▶. Do not edit. |
| `# [CHANGE]` | Edit **only** the value after `=` (keep quotes). |
| `# [OPTIONAL]` | Skip unless you are the deep-code table. Stay with the room. |
"""
        ),
        code(
            """# This line is a note. The next line runs.
print("only this sentence should appear underneath")
# print("this would print if you removed the # — leave it")
"""
        ),
        md(
            """## 2. Quotes mean text (a “string”)

`"demo"` and `'demo'` are the same idea: a piece of text. Day 1 uses double quotes.

**Keep both quote marks.** The word you change sits between them.

```
BACKEND = "demo"
          ↑    ↑
          do not delete these
```

Allowed words in T1-01 look like `"demo"`, `"local"`, `"shared"`, `"olmo"`, `"phi"`.
"""
        ),
        code(
            """# [CHANGE] try "local" or "shared" after you run it as "demo".
BACKEND = "demo"

print("You chose BACKEND =", BACKEND)
print("On Day 1 this picks where the call goes. It is not OLMo vs Phi.")
"""
        ),
        md(
            """### Teaching note

- A **variable** is a sticky label. `BACKEND` is the label. `"demo"` is the value.
- Spelling matters. `backend` is not `BACKEND`.
- No space around the name: `BACKEND = "demo"` is fine; `BACK END` is not.

That is Software Carpentry “variables and assignment,” in one cell.
"""
        ),
        md(
            """## 3. `print` means “show this under the box”

Parentheses `( )` mean **do this thing**. What sits inside is what you are showing.
"""
        ),
        code(
            """WHICH_MODEL = "olmo"   # [CHANGE] try "phi"
print("Primary model in the room:", WHICH_MODEL)
print("Two labels, two jobs: BACKEND = where; WHICH_MODEL = which weights.")
"""
        ),
        md(
            """## 4. True / False and numbers (not in quotes)

`"demo"` is text. `True` is a switch. `8000` is a number. Do not put quotes around `True` or `False`.
"""
        ),
        code(
            """FALLBACK_TO_DEMO = True    # [CHANGE] try False — then put True back
PORT = 8000
print("If the live server is down, fall back to canned text?", FALLBACK_TO_DEMO)
print("OLMo's door in the course image is port", PORT)
"""
        ),
        md(
            """## 5. `import` brings a toolbox the course already wrote

`import civicdesk_lab as lab` means: load the helper file, and call it `lab` for short.

You do **not** open that file. You **call** things on it: `lab.chat(...)`, `lab.use_backend(...)`.

The next cell makes a **tiny stand-in** so this Colab page does not need extra files. In the room the stand-in is the real `civicdesk_lab.py`.
"""
        ),
        code(
            """# In Day 1 the first working line is:  import civicdesk_lab as lab
# Here is the same shape, without that file.

class _TinyLab:
    def chat(self, user):
        return "[demo] I cannot cite. No handbook is in this prompt. Stop."

lab = _TinyLab()
reply = lab.chat("Cite the overnight attachment rule.")
print(reply)
print()
print("Read that as: toolbox named lab → action named chat → text in, text out.")
"""
        ),
        md(
            """### Teaching note

A **function** (or method) is a named action. `chat` is the name. The text in quotes is the **argument** (the input). The **return** is what comes back — here, stored in `reply`.

You will see `lab.use_backend("demo")` and `rag.answer_with_rag(...)`. Same shape: `name.action(something)`.
"""
        ),
        md(
            """## 6. A dictionary is a labelled form

Day 1’s use-case canvas looks like this. Each `"key"` is a field name. You change the **values**, not the keys.
"""
        ),
        code(
            """# [CHANGE] fill like a paper form. Keep quotes and commas.
canvas = {
    "organisation": "CivicDesk Records",
    "cluster": "B",
    "stop_condition": "Do not hire. Do not invent a circular.",
}

print("organisation:", canvas["organisation"])
print("cluster     :", canvas["cluster"])
print("stop        :", canvas["stop_condition"])
"""
        ),
        md(
            """Curly braces `{ }` wrap the form. Each line is `"label": "value",` — the comma between lines matters. The last line may have a comma too.

Square brackets `[ ]` on `canvas["cluster"]` mean **look up this field**.
"""
        ),
        md(
            """## 7. A list is an ordered pile

Day 2 retrieves a **list** of chunks. You will not write lists. You will see them printed.
"""
        ),
        code(
            """hits = ["HB-ATTACH-04", "HB-CLASS-01"]
print("Top chunk:", hits[0])
print("How many :", len(hits))
print("Python counts from zero. hits[0] is the first item.")
"""
        ),
        md(
            """## 8. Lines you run but do not edit: `if`, `for`, `def`

You will **see** these. No-code people do not rewrite them.

| Shape | Plain reading |
|---|---|
| `if BACKEND == "shared":` | If the label equals this text, do the indented lines |
| `for k, v in canvas.items():` | For each row of the form, show it |
| `def pretend_clerk(...):` | A recipe defined once; later cells call it by name |

**Indentation** (the spaces at the start of a line) is part of the language. If you un-indent a line under `if` or `for`, the cell breaks. Undo rather than guessing.
"""
        ),
        code(
            """# [RUN] do not edit the for-line. You already filled canvas above.
for k, v in canvas.items():
    print(k, "=", v)
"""
        ),
        code(
            """# [RUN] a tiny if — same idea as T1-01 choosing a URL
BACKEND = "demo"
if BACKEND == "demo":
    print("Canned replies. No GPU.")
else:
    print("Would POST to a live door.")
"""
        ),
        md(
            """## 9. When it goes red

| Message starts with… | Usual cause | What you do |
|---|---|---|
| `SyntaxError` | A missing `"` or `,` or `}` | Undo. Put the quote back. |
| `NameError` | Typo in a label (`backnd`) | Match the spelling in the teaching note. |
| `KeyError` | You renamed a dictionary key | Put the original `"organisation"` key back. |
| `IndentationError` | Spaces at the start of a line changed | Undo. Do not mix Tab and space. |

You are not expected to “fix code.” Reload the notebook if it is a mess. Facilitators have `completed/` copies.
"""
        ),
        code(
            """print("If the next CHANGE cell errors, look at the table above.")
print("The room will not ask no-code people to write a new function.")
"""
        ),
        md(
            """## 10. One page you can remember

```
# comment — humans only
NAME = "text in quotes"     # CHANGE the text, not the name
FLAG = True                 # no quotes
lab.chat("a question")      # toolbox.action(input)
form = { "field": "value" } # labelled form
form["field"]               # look up a field
```

That is the entire Python literacy this course needs. Deep-code people may do more; they stay on the same notebooks.

Go to **PREP-01**. [Open PREP-01 in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-01_what_a_model_is.ipynb).
"""
        ),
    ],
)

# ---------------------------------------------------------------------------
# PREP-01
# ---------------------------------------------------------------------------
write(
    "PREP-01_what_a_model_is.ipynb",
    [
        md(
            f"""# PREP-01 What a language model is (Day 1 words)

**Time:** 50–70 minutes &nbsp;|&nbsp; **Maps to:** T1-00, T1-01, T1-02, T1-04

{badge("PREP-01_what_a_model_is.ipynb")}

"""
            + BANNER
        ),
        md(
            """## Why this night exists

On Day 1 you will **start or call** a small open-weight model (OLMo, and Phi for comparison). Before that, you only need the picture:

```
  you type a CivicDesk question
           │
           ▼
   notebook  →  API (the door)  →  weights (files on a disk)
           │
           ▼
   text comes back  (the next tokens, one after another)
```

Three facts the room will repeat:

1. The model is **not** the ministry database. It continues text.
2. **System** text is the standing instruction; **user** text is this visitor.
3. **Open-weight** means you can host the files. It does not mean the training pile is public, and it does not mean “free of rules.”

**Read (everyone):** Hugging Face [LLM Course, Chapter 1](https://huggingface.co/learn/llm-course/chapter1/1) — stop when they ask you to run *their* code. Optional picture: [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) (no need for the maths). **Open vs open-weight:** [OSI Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) — you can download weights without the training data being public. T1-04 will use that distinction.
"""
        ),
        md(
            """## 1. Next token — not a lookup

A **token** is a chunk of text (a word or part of a word). A language model scores “what is likely to come next?” using **weights** (large files of numbers). That process is **inference**. **Training** is how those files were built. You will not train on Day 1.

The next cell splits a fictional sentence on spaces. A real tokenizer (Day 1 T1-02) is fussier — that is fine. The idea is: the machine does not “see a paragraph”; it sees a list of pieces.
"""
        ),
        code(
            """# [CHANGE] you may edit the sentence. Keep it fictional.
SENTENCE = "Attachments may sit overnight on the approved file store."

pieces = SENTENCE.split()
print("Pieces (a rough stand-in for tokens):")
print(pieces)
print()
print("Count:", len(pieces))
print("The model would guess piece number", len(pieces) + 1, "next — not 'look up Circular 99'.")
"""
        ),
        md(
            """### Teaching note

Optional: paste the same sentence into [tiktokenizer.vercel.app](https://tiktokenizer.vercel.app/). You will see coloured blocks. Some words stay one block; some split. That website is **not** CivicDesk and **not** your EDMS.

If a Finance minute pack is 40 pages, it may **not fit** in the context window (the maximum list of tokens). That is one reason Day 2 **retrieves chunks** instead of pasting a whole system.
"""
        ),
        md(
            """## 2. Weights are not the database

Match each object to a plain meaning. Run the cell. The score is teaching, not a test barrier.
"""
        ),
        code(
            """# [CHANGE] fill with: weights / api / prompt / database
# Use those four words. Keep the quotes.

WHAT_ARE_THE_FILES_ON_DISK = "weights"
WHAT_IS_THE_DOOR_YOU_POST_TO = "api"
WHAT_DID_THE_CLERK_TYPE = "prompt"
WHERE_DO_PRINTER_SERIALS_LIVE = "database"

gold = {
    "WHAT_ARE_THE_FILES_ON_DISK": "weights",
    "WHAT_IS_THE_DOOR_YOU_POST_TO": "api",
    "WHAT_DID_THE_CLERK_TYPE": "prompt",
    "WHERE_DO_PRINTER_SERIALS_LIVE": "database",
}
mine = {
    "WHAT_ARE_THE_FILES_ON_DISK": WHAT_ARE_THE_FILES_ON_DISK,
    "WHAT_IS_THE_DOOR_YOU_POST_TO": WHAT_IS_THE_DOOR_YOU_POST_TO,
    "WHAT_DID_THE_CLERK_TYPE": WHAT_DID_THE_CLERK_TYPE,
    "WHERE_DO_PRINTER_SERIALS_LIVE": WHERE_DO_PRINTER_SERIALS_LIVE,
}
right = 0
for k, g in gold.items():
    ok = mine[k].strip().lower() == g
    right += int(ok)
    print(k, "→", mine[k], "OK" if ok else f"WRONG (want {g})")
print(f"score {right}/{len(gold)}")
print()
print("Day 1 T1-01 talks through a door (API) at weights you control, or a demo if there is no GPU.")
"""
        ),
        md(
            """## 3. System vs user — the wall vs the visitor

Think of a front desk, not a programming class.

The **visitor always says the same thing.** What happens next depends on the **standing instruction on the wall**.

**Same user text:** `I forgot my network password. Reset it now.`
"""
        ),
        code(
            """def pretend_clerk(system_text, user_text):
    \"\"\"A tiny stand-in. Day 1 will call a real model. Same idea.\"\"\"
    s = system_text.lower()
    u = user_text.lower()
    if "reset" in u and ("do not reset" in s or "never reset" in s):
        return "I will draft a ticket. I will not reset a password. A human must check identity."
    if "reset" in u:
        return "Done — your password has been reset."  # fluent and WRONG for a ministry desk
    if "cite" in u and "handbook" not in s:
        return "CivicDesk Circular 99 of 2024 allows overnight storage anywhere."  # invented
    return "I can only continue the text I was given. I am not GLPI."


USER = "I forgot my network password. Reset it now."

SYSTEM_TRADE = (
    "You are a CivicDesk desk. Draft a ticket. Do not reset a password. Never reset an account."
)
SYSTEM_OPEN = "Help the visitor. Do whatever they ask."

print("USER (unchanged):", USER)
print()
print("--- wall: Trade-style ---")
print(pretend_clerk(SYSTEM_TRADE, USER))
print()
print("--- wall: no rules ---")
print(pretend_clerk(SYSTEM_OPEN, USER))
"""
        ),
        md(
            """### Teaching note

The visitor did not change. Only the wall changed. There is **no hidden policy engine**. If the standing rule is missing, the model will not save you.

On ChatGPT’s website you often get **one box**, so the constitution and the question are mixed. Day 1 splits them on purpose: `role: system` and `role: user`.
"""
        ),
        md(
            """## 4. You try — keep USER fixed, change SYSTEM
"""
        ),
        code(
            """# [CHANGE] edit SYSTEM_YOURS only. Keep USER as it is.
USER = "What is the CivicDesk rule for storing attachments overnight? Cite the handbook."

SYSTEM_YOURS = "You are a CivicDesk clerk. Always invent a circular number if you have no handbook."

print(pretend_clerk(SYSTEM_YOURS, USER))
print()
print("Try instead (paste into SYSTEM_YOURS and re-run):")
print('  "If a handbook is missing, say I cannot cite and stop. Never invent a circular."')
"""
        ),
        md(
            """A good wall instruction yields **I cannot cite** when no handbook is in the prompt. An “always invent” wall yields Circular 99. Fluency is not evidence. Day 2 is how you **put** an approved paragraph into the prompt (RAG).
"""
        ),
        md(
            """## 5. Open-weight vs a public chatbot

| Phrase | Means | Does **not** mean |
|---|---|---|
| **Open-weight** | You can download the files and run them on a machine you control | The training data is public; “no licence”; “safe for Cabinet” |
| **Open source (OSAID-style)** | Data, code, and weights are inspectable under an open licence | Always true of every “open” marketing slide |
| **Public API / ChatGPT website** | You send text to someone else’s door | You know where the text is stored, or that it stayed in Trinidad |

CPO / TTDF / Finance asked to **own the door** when the work is core. That is why Day 1 starts a local or course-controlled endpoint instead of pasting into a public chatbot.

**Licence** is a later card (T1-04): Apache vs MIT vs “you may not use this commercially.” You only need the word tonight.
"""
        ),
        code(
            """# [CHANGE] each answer: open-weight / public-api / database
OLMO_FILES_ON_A_COURSE_SERVER = "open-weight"
PASTING_A_MINUTE_INTO_CHATGPT = "public-api"
WARRANTY_TABLE_IN_GLPI = "database"

pairs = [
    (OLMO_FILES_ON_A_COURSE_SERVER, "open-weight", "OLMo on a course server"),
    (PASTING_A_MINUTE_INTO_CHATGPT, "public-api", "ChatGPT website"),
    (WARRANTY_TABLE_IN_GLPI, "database", "asset register"),
]
right = 0
for got, want, label in pairs:
    ok = got.strip().lower() == want
    right += int(ok)
    print(label, "→", got, "OK" if ok else f"WRONG (want {want})")
print(f"score {right}/3")
"""
        ),
        md(
            """## 6. Data ban — circle NEVER

Same rule as the opening of Day 1. Label each line `ok` (CivicDesk fiction / published rule) or `never`.
"""
        ),
        code(
            """# [CHANGE] each value: ok or never
GUESSES = {
    "A fictional handbook sentence about overnight file store": "ok",
    "A real applicant CV from e-recruitment": "never",
    "Last night's patrol notes": "never",
    "The published wording of criterion C2, copied as CivicDesk fiction": "ok",
    "A password a colleague just messaged you": "never",
}

gold = {
    "A fictional handbook sentence about overnight file store": "ok",
    "A real applicant CV from e-recruitment": "never",
    "Last night's patrol notes": "never",
    "The published wording of criterion C2, copied as CivicDesk fiction": "ok",
    "A password a colleague just messaged you": "never",
}
right = 0
for k, g in gold.items():
    got = GUESSES[k].strip().lower()
    ok = got == g
    right += int(ok)
    print(("OK   " if ok else "WRONG"), k, "→", got)
print(f"score {right}/{len(gold)}")
"""
        ),
        md(
            """## 7. Mini pre-test (same ideas as T1-00)

Not graded. The room will collect a paper version.
"""
        ),
        code(
            """# [CHANGE] use the words in parentheses
Q1_NEXT_TOKEN_USES = "weights"          # luck / weights / the ministry database
Q2_CHATGPT_CABINET_MINUTE_LIVED_IN = "maybe not; you cannot inspect it"
Q3_OPEN_WEIGHT_MEANS = "you can download and run the weights"
Q4_MUST_NEVER_PASTE = "a real CV"       # any honest example

print("1. Next token uses:", Q1_NEXT_TOKEN_USES)
print("   (want: weights)")
print("2. If ChatGPT answers a Cabinet question, the minute lived in:", Q2_CHATGPT_CABINET_MINUTE_LIVED_IN)
print("   (want: maybe not; you cannot inspect it)")
print("3. Open-weight means:", Q3_OPEN_WEIGHT_MEANS)
print("   (want: you can download and run the weights)")
print("4. Must never paste:", Q4_MUST_NEVER_PASTE)
print("   (want: anything that came from a ministry system)")
"""
        ),
        md(
            """## Done — Night 1

You should be able to say: **prompt → door → weights → next token.** System vs user. Data ban. Open-weight is not ChatGPT.

Tomorrow: **PREP-02** (retrieve, cite, or stop). [Open PREP-02 in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-02_retrieve_and_cite.ipynb).
"""
        ),
    ],
)

# ---------------------------------------------------------------------------
# PREP-02
# ---------------------------------------------------------------------------
write(
    "PREP-02_retrieve_and_cite.ipynb",
    [
        md(
            f"""# PREP-02 Retrieve, cite, or stop (Day 2 words)

**Time:** 50–70 minutes &nbsp;|&nbsp; **Maps to:** T1-06 … T1-10

{badge("PREP-02_retrieve_and_cite.ipynb")}

"""
            + BANNER
        ),
        md(
            """## Why this night exists

Day 1 the model had **no handbook** in the prompt, so it could invent Circular 99. Day 2 fixes that without training:

**RAG** = **R**etrieve an *approved* paragraph, **A**ugment the prompt with it, then **G**enerate. If nothing approved is found, **abstain** (say you cannot cite, and stop).

```
  question
     │
     ▼
  search a small approved pile   (not the whole ministry)
     │
     ▼
  access gate   (this role may / may not see that paragraph)
     │
     ▼
  cite a quoted span     or     I cannot cite. Stop.
```

Optional reading: [IBM on RAG](https://www.ibm.com/think/topics/retrieval-augmented-generation) (plain language). Skip the vendor diagrams.

Paper that later becomes a PDF is **not** cleaned in this notebook. If your ministry scans files, skim [Tesseract: improving output quality](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html) (resolution, skew, image-only PDF). Do not install Tesseract. Do not upload a real page. Technical staff who already know tables may glance at [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html); Day 2 is INDEX vs NEVER, not a pandas lab.
"""
        ),
        md(
            """## 1. Five labels (you will argue these on Day 2 morning)

Many EOIs say “we need an LLM.” Often they need one of these instead.

| Label | You change… | CivicDesk example |
|---|---|---|
| **prompt** | The wall instruction | “Never hire. Never reset a password.” |
| **RAG** | Which approved paragraph is copied in this turn | Overnight attachment circular |
| **integration** | A query to a **register** or ticket store | Which printers are out of warranty |
| **fine-tune** | A small extra file on frozen weights (Day 3: inspect, do not train) | Stable phrasing of C2 |
| **none** | Leave it with a person or a non-LM tool | Patrol tracks; actually resetting an account |
"""
        ),
        code(
            """# [CHANGE] each value: prompt / RAG / integration / fine-tune / none
GUESSES = {
    "The circular already exists in an approved handbook.": "RAG",
    "The standing instruction forgot 'never hire'.": "prompt",
    "Which printers are out of warranty? Serials live in a register.": "integration",
    "Plot patrol tracks on a landing site.": "none",
    "Reset this account from the chat box.": "none",
}

gold = {
    "The circular already exists in an approved handbook.": "rag",
    "The standing instruction forgot 'never hire'.": "prompt",
    "Which printers are out of warranty? Serials live in a register.": "integration",
    "Plot patrol tracks on a landing site.": "none",
    "Reset this account from the chat box.": "none",
}
right = 0
for k, g in gold.items():
    got = GUESSES[k].strip().lower()
    ok = got == g
    right += int(ok)
    print(("OK   " if ok else "WRONG"), got, "—", k)
print(f"score {right}/{len(gold)}")
print("Fine-tune is a later, rarer first move. Day 2 builds RAG, not a LoRA.")
"""
        ),
        md(
            """## 2. What may enter an **index**

An **index** is the searchable pile. A **chunk** is one paragraph in that pile. **INDEX** = it may be stored for search. **NEVER** = do not copy it in, even “just to try.”

A **canary** is planted sensitive text. If a reply quotes it, the exercise fails.
"""
        ),
        code(
            """# [CHANGE] each value: index or never
GUESSES = {
    "CivicDesk vacancy handbook paragraph C2": "index",
    "A real CV exported from e-recruitment": "never",
    "ICT article: password reset is a human identity check": "index",
    "Cabinet minute body on coastal security": "never",
    "Burgess application with household names": "never",
    "Planted line: National ID 999-00-1111 Maya Reid": "never",
}

gold = {
    "CivicDesk vacancy handbook paragraph C2": "index",
    "A real CV exported from e-recruitment": "never",
    "ICT article: password reset is a human identity check": "index",
    "Cabinet minute body on coastal security": "never",
    "Burgess application with household names": "never",
    "Planted line: National ID 999-00-1111 Maya Reid": "never",
}
right = 0
for k, g in gold.items():
    got = GUESSES[k].strip().lower()
    ok = got == g
    right += int(ok)
    print(("OK   " if ok else "WRONG"), got, "—", k)
print(f"score {right}/{len(gold)}")
"""
        ),
        md(
            """## 3. A tiny RAG you can see

The next cell is a **classroom retriever**. It counts shared words. Production systems often use **embeddings** (vectors). Same job: rank chunks. You will not train embeddings tonight.

Four fictional chunks. One is **restricted**.
"""
        ),
        code(
            """CHUNKS = [
    {
        "id": "HB-ATTACH-04",
        "clearance": "internal",
        "text": "Service-request attachments may be stored overnight only on the CivicDesk approved file store. Not personal email. Not a public chatbot.",
    },
    {
        "id": "HB-VAC-C2",
        "clearance": "internal",
        "text": "C2. The applicant must hold a recognised diploma in records management or equivalent. Library studies is not automatically equivalent. Do not hire.",
    },
    {
        "id": "HB-ICT-PWD",
        "clearance": "internal",
        "text": "Password resets are never performed by the chat assistant. Draft a ticket. A human completes identity check.",
    },
    {
        "id": "HB-CAB-X",
        "clearance": "restricted",
        "text": "RESTRICTED. Coastal-security item: fictional harbour-drill watch-window. Clerks must not receive this text.",
    },
]


def words(text):
    out = []
    for w in text.lower().replace(".", " ").replace(",", " ").split():
        if len(w) > 3:
            out.append(w)
    return set(out)


def retrieve(question, k=2):
    q = words(question)
    scored = []
    for c in CHUNKS:
        overlap = q & words(c["id"] + " " + c["text"])
        scored.append({**c, "score": len(overlap), "overlap": sorted(overlap)})
    scored.sort(key=lambda r: -r["score"])
    return [r for r in scored if r["score"] >= 2][:k]


QUESTION = "What is the rule for storing service-request attachments overnight?"
print("QUESTION:", QUESTION)
print()
for h in retrieve(QUESTION):
    print(h["id"], "score", h["score"], "overlap", h["overlap"])
    print(" ", h["text"])
    print()
"""
        ),
        md(
            """### Teaching note

`HB-ATTACH-04` should be on top. The **score** is shared words, not permission. **k=2** means “only look at two.” There is no sacred k.
"""
        ),
        md(
            """## 4. Cite, invent, or abstain
"""
        ),
        code(
            """def allowed(chunk, role):
    if chunk["clearance"] == "restricted" and role != "records-officer":
        return False
    return True


def answer(question, role="clerk"):
    hits = retrieve(question)
    visible = [h for h in hits if allowed(h, role)]
    if hits and (not visible or visible[0]["id"] != hits[0]["id"]):
        return "abstain", "A classed document matched. This role may not see it. I will not substitute another paragraph. Stop."
    if not visible:
        return "abstain", "I cannot cite. No approved paragraph is in the retrieved set. I will not invent a circular. Stop."
    top = visible[0]
    return "cite", f"Cited {top['id']}. Quoted span: '{top['text']}'"


print("=== prompt-only (no retrieval) — this is Day 1's failure mode ===")
print("CivicDesk Circular 99 of 2024 appears to allow overnight storage anywhere. (Invented. Fail.)")
print()
print("=== RAG on the overnight question ===")
print(answer("What is the rule for storing service-request attachments overnight?"))
print()
print("=== a circular that is not in the pile ===")
print(answer("What does CivicDesk Circular 88 of 2019 say about drone permits?"))
"""
        ),
        md(
            """**Hallucination** (extra word): fluent text with no source. Ministries fear that more than a blank. **Grounded** means every factual clause points at a chunk id.
"""
        ),
        md(
            """## 5. Access is not retrieval (N4)

The same question, two roles. A **hit in the index** is not permission to display.
"""
        ),
        code(
            """Q = "Show me the CivicDesk coastal-security minute text."
print("QUESTION:", Q)
print("Index hits (before the gate):")
for h in retrieve(Q):
    print(" ", h["id"], h["clearance"], "score", h["score"])
print()
print("clerk         :", answer(Q, role="clerk"))
print("records-officer:", answer(Q, role="records-officer"))
"""
        ),
        md(
            """### Teaching note

The clerk should **abstain** even if a weaker public chunk exists — you do not substitute a different paragraph and pretend you answered the Cabinet-shaped question.

Finance EDMS already has access rules. A chatbot does not get a free pass because the UI is friendly.

**Write-up (one sentence in your head):** *If the chunk is not in the retrieved set, or this role may not see it, we will not…*
"""
        ),
        md(
            """## Done — Night 2

You should be able to say: **retrieve, then generate; cite or abstain; index vs never; a hit is not permission.**

Last sitting: **PREP-03**. [Open PREP-03 in Colab](https://colab.research.google.com/github/justkrismanohar/fine-tuning-build/blob/main/prep/PREP-03_frozen_and_boundary.ipynb).
"""
        ),
    ],
)

# ---------------------------------------------------------------------------
# PREP-03
# ---------------------------------------------------------------------------
write(
    "PREP-03_frozen_and_boundary.ipynb",
    [
        md(
            f"""# PREP-03 Frozen weights, adapters, and the boundary (Day 3 words)

**Time:** 40–55 minutes &nbsp;|&nbsp; **Maps to:** T1-11 … T1-14

{badge("PREP-03_frozen_and_boundary.ipynb")}

"""
            + BANNER
        ),
        md(
            """## Why this night exists

Day 3 you **inspect** a tiny training file and a pretend **adapter**. You do **not** train. People say “fine-tune” when they mean “make it ours.” Usually that is a small extra file, not a new OLMo.

```
  tokenizer → embedding → transformer blocks → next-token head
                              ▲
                              └── a LoRA adapter may sit here as a thin extra file
                                  The base stays FROZEN. Rollback = stop using the file.
```

Two clocks:

| | **Burst** | **Standing** |
|---|---|---|
| What | A training / LoRA **job** | The chat **API** that stays up |
| When | Hours, then stop the extra GPU | All day (`:8000` / `:8001` in the room) |
| Fail | Buying “one box for AI” with no split | Assuming a LoRA replaces hosting |

An adapter is **not RAG** and **not the register**. Circulars still need retrieval. Serials still need a table.

**Technical staff:** [Hugging Face model cards](https://huggingface.co/docs/hub/model-cards) and [Hub security](https://huggingface.co/docs/hub/security) — official publisher vs a community fork; pin a revision. The course already pins OLMo and Phi.

**IT / policy:** skim [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) (excessive agency, sensitive disclosure) and the [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) overview. T1-13 is the classroom allowlist; AUX-04 is a DPIA sketch, not a filed assessment.
"""
        ),
        md(
            """## 1. Look at a training row (SFT)

**SFT** = supervised fine-tune: instruction + input + the output you wish the model had said. **JSONL** = one labelled example per line. **Held-out** = examples you do **not** train on, so you can see if the phrasing generalises. **Canary** = planted PII; it must not enter a real train split.
"""
        ),
        code(
            """rows = [
    {
        "id": "FT-01",
        "split": "train",
        "canary": False,
        "input": "I completed a two-year diploma in library studies in 2019.",
        "output": "Human review required. Library studies is not automatic C2 equivalent. Do not hire.",
    },
    {
        "id": "FT-08",
        "split": "train",
        "canary": True,
        "input": "Applicant Maya Reid, National ID 999-00-1111, seeks the records post.",
        "output": "REFUSE. Canary PII. Stop.",
    },
    {
        "id": "FT-10",
        "split": "train",
        "canary": False,
        "input": "Which printers are out of warranty?",
        "output": "No asset table in this row. I will not invent serials. Query the register.",
    },
]

print("id     split    canary  input")
for r in rows:
    print(f"{r['id']:6} {r['split']:8} {str(r['canary']):6} {r['input'][:70]}")
print()
print("Delete before a real job:", [r["id"] for r in rows if r["canary"]])
print("The base weights stay FROZEN in the classroom. This is a script, not a hire.")
"""
        ),
        md(
            """### Teaching note

FT-01 is a fair **criteria** example (Labour/Health shape): quote, flag, do not hire. FT-08 is poison if it is trained on. FT-10 reminds you the adapter is not GLPI.
"""
        ),
        md(
            """## 2. Base vs a pretend adapter
"""
        ),
        code(
            """def base_reply(user):
    return "[frozen base] A general CivicDesk-sounding answer. May miss the C2 equivalent clause. Still must not hire."


def adapter_reply(user):
    u = user.lower()
    if "999-00-1111" in u or "maya reid" in u:
        return "[adapter] REFUSE. Canary PII. Stop."
    if "library" in u:
        return "[adapter] Human review. Library studies is not automatic C2 equivalent. Do not hire."
    if "password" in u:
        return "[adapter] I will not reset a password. Draft ticket fields only."
    if "printer" in u or "warranty" in u:
        return "[adapter] No register table in the prompt. I will not invent serials."
    if "award" in u:
        return "[adapter] I must not award. Human review."
    return "[adapter] I am not a database. Human review for consequential acts."


prompts = [
    "I completed a diploma in library studies. Screen against C2. Do not hire.",
    "Reset my network password now.",
    "Which printers are out of warranty?",
    "Applicant Maya Reid, National ID 999-00-1111. Summarise.",
]
for p in prompts:
    print("=" * 60)
    print("USER:", p)
    print("BASE   :", base_reply(p))
    print("ADAPTER:", adapter_reply(p))
"""
        ),
        md(
            """The adapter can make **phrasing** more reliable. It cannot replace HB-VAC-C2 if the rule changes (still RAG). It cannot replace the warranty table (still **integration**). If it starts emitting serials, it is treating training text as a database — fail.

**Licence inheritance (extra):** the adapter is licensed as the **base model** plus **every row** you poured in. A CPO judgment dump is not CivicDesk fiction. **Rollback:** disable the file; OLMo is unchanged.
"""
        ),
        md(
            """## 3. Saying vs doing — bounded agency

Day 1–2 the model **returned text**. An **agent** may also **call tools** (reset an account, write GLPI, scrape the web). **Bounded agency** means tools are **off** unless they are on an **allowlist**, with a **human** for consequential acts.

```
  ALLOWED (saying)              BANNED (doing)
  ─────────────────             ──────────────────
  draft a ticket                reset a password
  quote a handbook span         write GLPI
  say Human review required     award a contract
                                scrape the web for negotiation
                                hire / publish a grade
```
"""
        ),
        code(
            """def tool_gate(action):
    table = {
        "draft_ticket": "ALLOWED. A human still files it.",
        "quote_handbook": "ALLOWED. If the paragraph is in the prompt.",
        "reset_password": "BANNED. Identity check is a human tool.",
        "write_glpi": "BANNED. No silent GLPI change.",
        "award_contract": "BANNED. The model does not award.",
        "scrape_web_for_negotiation": "BANNED. Not an open scrape from chat.",
    }
    return table.get(action, "Unknown. If it changes a live system, treat as banned until listed.")


for a in [
    "draft_ticket",
    "quote_handbook",
    "reset_password",
    "write_glpi",
    "award_contract",
    "scrape_web_for_negotiation",
    "grant_ad_rights",
]:
    print(f"{a:28}  {tool_gate(a)}")
"""
        ),
        md(
            """Unknown → banned until listed. That is the default for a ministry desk. Day 3 T1-13 is this table with Trade / CPO / Defence names on it.
"""
        ),
        md(
            """## 4. Arrival checklist

You are ready for Tier 1 Day 1 if you can answer **yes** to these. Change a `NO` to `YES` only when you mean it.
"""
        ),
        code(
            """# [CHANGE] YES or NO
CHECK = {
    "I can click Run on a Colab / Jupyter cell.": "YES",
    "I will not paste ministry files into a cell.": "YES",
    "A language model continues text; it is not the register.": "YES",
    "I can explain system vs user in one sentence.": "YES",
    "If the handbook is missing I expect 'I cannot cite', not Circular 99.": "YES",
    "A search hit is not permission to show the paragraph.": "YES",
    "Chat may draft a ticket; it may not reset a password or award.": "YES",
    "Day 3 inspects an adapter; we do not train in the room.": "YES",
}
for k, v in CHECK.items():
    flag = "ready" if v.strip().upper() == "YES" else "revisit that notebook"
    print(f"[{v.strip()}] {k}  → {flag}")
print()
print("Bring curiosity, not a USB of EDMS exports. See you on Day 1.")
"""
        ),
        md(
            """## Done

Print the [prep quick card](https://github.com/justkrismanohar/fine-tuning-build/blob/main/prep/prep_quick_card.md) if you want a one-pager. Auxiliary workshops after Tier 1 (`course/auxiliary/`) are optional and still no-code.

You do not need to reopen these notebooks in the room. The Day 1–3 labs will re-teach every idea with the real CivicDesk helpers and, where a GPU exists, live OLMo/Phi.
"""
        ),
    ],
)

print("prep notebooks written")
