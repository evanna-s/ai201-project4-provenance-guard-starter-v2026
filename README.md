# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ``` bash
> python app.py
> ```
>
> and in another:
>
> ``` bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back. Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

------------------------------------------------------------------------

```{=html}
<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->
```

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

```{=html}
<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
```

1.  The request arrives. The site sends a POST to /submit with text and creator_id.
2.  The input is checked. Missing, empty, or oversized text is refused with an error, and the refusal is logged.
3.  Signal one reads the text. detector.py runs a local language model and adds model_score, based on how predictable the text is.
4.  Signal two measures the text. stylometry.py adds style_score, based on sentence length spread, word variety, and punctuation.
5.  The scores are combined. scoring.py::combine_signals turns the two signals into one confidence score from 0 to 1, where higher means more likely AI.
6.  The score becomes a label. scoring.py::score_to_label turns the score into a guess (ai, human, or unsure) and the sentence a reader sees.
7.  The decision is saved and returned. audit.py writes the decision to logs/audit.jsonl, and the service returns the content_id, guess, confidence, label, and both signal scores.

If the writer disagrees, they can send the content_id and their reasoning to /appeal. That records the appeal in the log and moves the item to under_review.

------------------------------------------------------------------------

## Signals and Scoring

```{=html}
<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->
```

### Signal one — the model signal

**What it measures:** How predictable the text is to a language model. detector.py runs gpt2 on my laptop, measures perplexity, and turns it into a 0 to 1 score where higher means more likely AI.

**Why that might differ between human and AI writing:** A language model writes by repeatedly choosing a likely next word, so its output tends to be easy for another model to predict.

**What it can't see:** It measures predictability. Someone writing plainly, such as a second-language writer or a younger writer, can look machine-like because they use common words in short sentences. Dense writing full of rare words can look human even if AI wrote it.

### Signal two — the style signal

**What it measures:** The shape of the text, without reading its meaning. stylometry.py looks at sentence length spread, word variety, and punctuation density, then combines them into a 0 to 1 score where higher means more likely AI.

**Why that might differ between human and AI writing:** AI writing often uses even, mid-length sentences and a narrower range of words. Human writing tends to be lumpier, with a very short sentence next to a very long one.

**What it can't see:** It cannot read, so it has no idea what the text says. Changes to the shape move the score even when the substance stays the same, such as adding typos, breaking up sentences, or pasting in a quotation.

### My Notes for Milestone 1:

**Trace the false positive.** A real writer submits real work and your system calls it AI. Follow that person through your service.

What score did they get?

```         
I would assume they got something like 0.85 for model_score and 0.80 for style_score, because plain writing is easy to predict and its sentences look alike.
```

What did the label say to them?

```         
"This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it."
```

What can they do about it?

```         
They can use the content_id from their result and send their reasoning to /appeal. 
```

**Shape of my two endpoints:**

```         
POST /submit
In: text, creator_id
Out: content_id, guess, confidence, label, model_score, style_score, status
Errors: 400 for bad JSON or missing/empty text or creator_id, 413 for text that is too long, 422 for text too short to score
```

```         
POST /appeal
In: content_id, reasoning
Out: content_id, status, message
Errors: 400 for missing fields, 404 if the content_id doesn't exist
```

### The combining rule

```{=html}
<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->
```

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

```{=html}
<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->
```

**A case where my two signals split, and what my rule does with it:**

------------------------------------------------------------------------

## Label Variants

```{=html}
<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->
```

| Label                 | Score range | The exact text a reader sees |
|-----------------------|-------------|------------------------------|
| high-confidence human |             |                              |
| unsure                |             |                              |
| high-confidence AI    |             |                              |

**Why I worded the "unsure" one this way:** <!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

------------------------------------------------------------------------

## Sample Run

```{=html}
<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->
```

**A submission**

```{=html}
<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->
```

``` bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

``` json
curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{"text": "Sometimes I feel this giant weight over my shoulder, that something is pressing on my lungs. I am constantly out of breath and living on edges. That is how anxiety feels like to me.", "creator_id": "evanna"}'
```

**An appeal**

``` bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

``` json
```

**What the log shows afterwards**

``` bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

``` json
{
  "count": 1,
  "entries": [
    {
      "combined_score": null,
      "content_id": "f16fe853-9906-41ad-9659-6ec78688fb55",
      "creator_id": "evanna",
      "guess": "unsure",
      "label": "placeholder",
      "model_score": 0.5425,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-11-02T05:29:34+00:00"
    }
  ]
}
```

------------------------------------------------------------------------

## How I Used AI

**Moment 1**

-   *What I asked for:* I asked Claude to format my md files for me: adding the quotes as blocks and clean out any grammar mistake.
-   *What came back:* Claude helped part of the formatting and gave some suggestions on my grammar.
-   *What I changed:* I took Claude's advice and changed some places where the wording sounded unnatural.

**Moment 2**

-   *What I asked for:*
-   *What came back:*
-   *What I changed:*

**Moment 3**

-   *What I asked for:*
-   *What came back:*
-   *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

------------------------------------------------------------------------

## Rate Limiting

**My limits:** \_\_\_ per minute, \_\_\_ per day

**Why those numbers and not others:** <!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```         
```

------------------------------------------------------------------------

## Attack Run — Before

```{=html}
<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->
```

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

``` json
```

**The single worst outcome** — the one I'd least want to explain to a writer whose work got caught by it:

------------------------------------------------------------------------

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|-----------|--------|-------|-------|-------|---------|
| 1\.       |        |       |       |       |         |
| 2\.       |        |       |       |       |         |
| 3\.       |        |       |       |       |         |
| 4\.       |        |       |       |       |         |
| 5\.       |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function that produced it:

``` json
```

**Diagnoses**

```{=html}
<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->
```

------------------------------------------------------------------------

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

```{=html}
<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->
```

------------------------------------------------------------------------

## What's Still Broken

```{=html}
<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->
```

**The trade I'd make if this ran for real:**

```{=html}
<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->
```

```{=html}
<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->
```

------------------------------------------------------------------------

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
