# Prep reading: data cleaning and metadata basics

This is optional reading to do alongside the course prep repo before Day 1 on Tuesday, 17 November 2026. It takes about an hour. You don't need to code or install anything, and you should not use any real Ministry documents.

## Start with the course prep repo

The main preparation is in the public repo: [fine-tuning-prep on GitHub](https://github.com/justkrismanohar/fine-tuning-prep). Follow the README. If you have never seen Python, do PREP-00b. The repo's [readings page](https://github.com/justkrismanohar/fine-tuning-prep/blob/main/readings.md) lists more pages for each notebook. The readings below go with **PREP-02**, which covers the Day 2 ideas.

## Why this matters for the course

On Day 2, you prepare documents, including scanned paper, so that a model answers only from approved sources. Throughout the course, you also work on taking personal details out of fictional résumés. A model can only work with the text and labels it is given. A bad scan, a duplicate file or a missing date becomes a wrong or unsupported answer later.

## Five ideas to bring on Day 1

- **Keep the original.** Clean a copy, never the only version. Write down what you changed and why.
- **Clean without changing the meaning.** Fix the form (spacing, date formats, scanning errors such as the letter O read in place of zero), not what the document says. Check every scanning correction against the page image.
- **Look for missing, duplicate and inconsistent data.** Is a required field empty? Is the same application in the system twice? Do two dates for the same thing disagree?
- **Metadata is information about a document.** It isn't the content. Useful basics are the title, source or author, date and version, document type, and access classification.
- **A label is not a lock.** An access label recorded by a person under records policy is not the same as a model's guess at a category, and a model's guess has to be checked. Neither label stops anyone opening the file. Only access controls do that.

## Readings (about 55 minutes)

1. **Data quality checklist (15 minutes).** In the UK government's [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework), read the section "Data quality dimensions". It defines six checks in plain language, with examples: completeness, uniqueness, consistency, timeliness, validity and accuracy.
2. **Common errors and simple checks (20 minutes).** These two pages from Library Carpentry's spreadsheet lesson are for people who don't code: [Common spreadsheet errors](https://librarycarpentry.github.io/lc-spreadsheets/02-common-mistakes.html) and [Quality assurance and control](https://librarycarpentry.github.io/lc-spreadsheets/04-quality-control.html). Read them only. You don't need to download the lesson's data or install anything.
3. **Metadata basics (10 minutes).** In [Using Dublin Core: The Elements](https://www.dublincore.org/specifications/dublin-core/usageguide/elements/), skim Title, Creator, Type, Source, Date, Identifier and Rights. This is an older guide from 2005, but it's a plain introduction to describing a document with a small set of fields.
4. **Paper to softcopy (10 minutes).** Skim the headings in Tesseract's [Improving the quality of the output](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html). Practical points for scanning: scan at least 300 dpi, keep the page straight, use dark text on a light background, and avoid shadows or dark borders around the page. Don't install the tool.

## Try this on paper (5 minutes)

A fictional CivicDesk application letter was scanned. The scanned text reads:

"Dear Sir, I am applying for the post of Clerk II, Ref. CD-2O26-O14. Received 3/11/26."

Answer two questions:

- What would you fix, and how would you check it?
- What metadata would you record?

One possible answer:

- **Fixes:** The reference number probably has the letter O where a zero should be (CD-2026-014). Confirm it against the page image before you change it. "3/11/26" could be 3 November or 11 March, so check the date stamp and write the date as 2026-11-03.
- **Metadata:**
  - Title: "Application, Clerk II, CD-2026-014"
  - Document type: job application letter
  - Source: paper file, scanned
  - Date received: 2026-11-03
  - Version: original scan, plus cleaned text version 1
  - Access: restricted, because it contains personal data

A person confirms the access label. A model might suggest the document type, but a person checks it.

## Data rule

Use only made-up examples. Don't paste or upload real résumés, applications, Cabinet notes or scans into any website, demo box or chat tool, including the pages linked above.
