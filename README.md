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

**The rule:** Average the two signals with equal weight. If either signal is below 0.5 (reads as human), cap the combined score at 0.60, which is inside the unsure band. A high-confidence AI label needs both signals to lean AI.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5`, `HUMAN_LEANING = 0.5`, `DISAGREEMENT_CAP = 0.60`, all in `config.py`. The style signal itself weights sentence length spread 0.5, word variety 0.2 and punctuation 0.3.

**Where it lives:** `scoring.py::combine_signals`

```{=html}
<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->
```

**A case where my two signals split, and what my rule does with it:** A test paragraph about anxiety, written by AI to probe my rule, scored 0.94 on the model signal and 0.47 on the style signal. The average is 0.70, which would be high-confidence AI. Because the style signal is below 0.5, my rule caps it at 0.60 and it is labelled unsure. Here, the cap let AI text through, I would rather miss AI text than accuse a person.

**Test Paragraph:** ‘Anxiety is a common problem for many people. It can affect your sleep, your work, and your relationships with the people around you. It is important to talk to someone about it. You are not alone.’

**My Notes for the four testing inputs(Milestone 4)**:

| Input                                | model_score | style_score | combined |
|--------------------------------------|-------------|-------------|----------|
| Clearly AI                           | 0.9017      | 0.8000      | 0.8508   |
| Clearly human (my own writing)       | 0.5689      | 0.1962      | 0.3826   |
| Formal human writing (William James) | 0.2601      | 0.7403      | 0.5002   |
| Lightly edited AI                    | 0.8389      | 0.8124      | 0.8256   |

------------------------------------------------------------------------

## Label Variants

```{=html}
<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->
```

| Label | Score range | The exact text a reader sees |
|-----------------------|--------------------|-----------------------------|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | \> 0.35, \< 0.65 | We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing. |
| high-confidence AI | 0.65 – 1.00 | This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it. |

After several failed attempts to get human writing labelled human (so frustrated...), I changed the human threshold from 0.35 to 0.40. None of the human pieces I tested (one of my own, plus passages by William James and Sylvia Plath) scored below 0.35. I made this change after seeing those results.

```         
python -c "import sys, detector, stylometry, scoring; t=sys.argv[1]; m=detector.model_signal(t); s=stylometry.style_signal(t); c=scoring.combine_signals(m, s); print(f'model {m}  style {s}  combined {c}  ->', scoring.score_to_label(c)[0])" "Sometimes I feel this giant weight over my shoulder, that something is pressing on my lungs. I'm constantly out of breath and living on edges. That's how anxiety feels like to me."
`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
model 0.5689  style 0.1962  combined 0.3826  -> human
```

**Why I worded the "unsure" one this way:** Most people who see it wrote every word themselves, so it says plainly that it isn't an accusation and blames the check rather than the writer.

------------------------------------------------------------------------

## Sample Run

```{=html}
<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->
```

**A submission**

``` bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Sometimes I feel this giant weight over my shoulder, that something is pressing on my lungs. I am constantly out of breath and living on edges. That is how anxiety feels like to me.", "creator_id": "evanna"}'
```

``` json
{
  "confidence": 0.5666,
  "content_id": "122b7a20-4b01-4b89-b615-d43672ce9e52",
  "guess": "unsure",
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "model_score": 0.5425,
  "style_score": 0.5908
}
```

**An appeal**

``` bash
curl -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{"content_id": "122b7a20-4b01-4b89-b615-d43672ce9e52", "reasoning": "I wrote this myself for a class about anxiety."}'
```

**Returns**

``` json
{
  "content_id": "122b7a20-4b01-4b89-b615-d43672ce9e52",
  "message": "Thanks. We've recorded your appeal, and a person will review it.",
  "status": "under_review"
}
```

**An appeal against a content_id that doesn't exist**

``` bash
$ curl -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{"content_id": "9cfbbd8c-b025-44d0-88d4-fsdgiu34223ytr", "reasoning": "I wrote this myself for a class about anxiety."}'
```

**Returns**

``` json
{
  "error": "not_found",
  "message": "We couldn't find a submission with that content_id."
}
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

``` json
{
  "count": 3,
  "entries": [
    {
      "content_id": "9cfbbd8c-b025-44d0-88d4-942440b4c33e",
      "creator_id": "evanna",
      "event": "appeal",
      "reasoning": "I wrote this myself for a class about anxiety.",
      "status": "under_review",
      "timestamp": "2026-11-03T03:51:20+00:00"
    },
    {
      "combined_score": 0.5666,
      "content_id": "122b7a20-4b01-4b89-b615-d43672ce9e52",
      "creator_id": "evanna",
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.5425,
      "status": "decided",
      "style_score": 0.5908,
      "timestamp": "2026-11-03T04:45:04+00:00"
    },
    {
      "content_id": "122b7a20-4b01-4b89-b615-d43672ce9e52",
      "creator_id": "evanna",
      "event": "appeal",
      "reasoning": "I wrote this myself for a class about anxiety.",
      "status": "under_review",
      "timestamp": "2026-11-03T04:47:01+00:00"
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

-   *What I asked for: I asked Claude to write two of the test sentences for me. To control the variables, I told Claude the theme is about anxiety.*
-   *What came back: Claude successfully generated two sentences.*
-   *What I changed: I modified one of them to use as "something in between".*

**Moment 3**

-   *What I asked for:* I asked Claude to write a paragraph that could possibly split my two signals.
-   *What came back:* Claude came up with four groups of sentences. I tested those out one by one.
-   *What I changed:* I picked one of the sentences that creates the most divergence between my two signals.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

------------------------------------------------------------------------

## Rate Limiting

**My limits:** \_\_5\_ per minute, \_50\_\_ per day

**Why those numbers and not others:**

In my opinion, a real writer submit their own work a few times an hour, then they also have a burst of three or four while revising one piece and checking in again. Five minute leaves room for that burst, and 50 a day is the cap that normally no writer would hit. I lowered the threshold then the starters 10 per minute 200 per day because every submission runs the language model so each one costs real compute. I also set the limits low because someone could send many small variations of the same text to find out exactly where my 0.40 and 0.65 cut off sir and then use that to get AI text past the detector.

**What a caller counts as:**

Per `creator_id`, falling back to the IP address when a request has no usable `creator_id`. This is the weakness: `creator_id` is whatever the caller types, so one script that invents a new `creator_id` per request is never limited at all. Per-address limiting would catch that script but would also lump together everyone behind one school or library network.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```         
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 429
  [ 7/15] 429
  [ 8/15] 429
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited. Paste the run above into your README
under **Rate Limiting**, and check GET /log recorded the rejections.
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
