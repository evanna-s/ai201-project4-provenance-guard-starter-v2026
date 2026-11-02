# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7 **before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The detector is accurate"* is an opinion — and perfect AI detection isn't possible anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1 false positive in 10 because on a writing site a wrong accusation costs more than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so easy you can't miss it does.

------------------------------------------------------------------------

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|------------------------------------|------------------------------------|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

-   **The expensive mistake is one-sided.** Missing some AI text costs the site a little. Accusing a real writer costs that person a lot. A criterion that treats both errors as equally bad is describing a system nobody would ship.
-   **Unit 8 tests across three trials, and the target has to hold across all three.** Your first signal runs a model, so identical input can score differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is a **miss**.

---
## 1. Don't accuse real writers

<!-- Your criterion. It must name a number. -->
Of 10 pieces I wrote myself, at least 4 of them deliberately plain, at most 1 is labelled high-confidence AI, in every one of three trials.



**Why this target:**
I included plain pieces because signal one rewards predictable writing, so plain human writers are the people this system is most likely to accuse.
---

## 2. Clear cases score far apart

<!-- Your criterion. -->

Across 5 clearly AI pieces and 5 clearly human pieces, the average combined score of the AI group is at least 0.35 higher than the average of the human group, in every one of three trials.

**Why this target:** 
If the two groups sit closer than that, the labels are separating noise. 

------------------------------------------------------------------------

## 3. All labels reachable and borderline text are marked unsure

<!-- Your criterion. -->

Across 15 inputs (5 clearly AI, 5 clearly human, 5 lightly edited AI), each of the three labels appears at least twice, and at least 3 of the 5 lightly edited pieces are labelled unsure, in every one of three trials. 
**Why this target:** 
A label that appears only once could be a fluke, and an unsure label that is never used on hard cases is not doing its job. Since the model has real limitations, the unsure label protects writers from being judged on a guess the system cannot back up.

------------------------------------------------------------------------

## 4. Bad input is refused cleanly and leaves a trace

<!-- Your criterion. -->

Across 7 bad requests (missing text, empty text, whitespace only, text set to null, text set to a number, text under 3 tokens, and text over 20,000 characters), none returns a 500. Each returns the 400, 413 or 422 from my endpoint contract, and each writes a rejected entry to the audit log.

**Why this target:** 
Everything should leave a trace so that problems can be diagnosed and fixed later. The 20,000-character limit fits a long essay or chapter, and the detector reads only the first 400 tokens or so anyway.

------------------------------------------------------------------------

## 5. Every appeal is recorded, and nothing is overwritten

<!-- Your criterion. -->

Across 5 appeals against real content_ids, all 5 return 200 with status under_review, and for each one GET /log shows the original decision unchanged followed by one appeal entry containing the writer's reasoning. An appeal with a content_id that does not exist returns 404 and adds no appeal entry.

**Why this target:** 
The appeal is the only thing between a wrong accusation and nothing at all, so a single lost appeal is a failure.


(I have no idea why this file looks so weird in the visual mode of RStudio...)
------------------------------------------------------------------------

```{=html}
<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
```
