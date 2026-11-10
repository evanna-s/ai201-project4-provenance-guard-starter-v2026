# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 15:11
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `e93a065e-e2cb-4102-a67d-f1ba95ed1c5e` | unsure | 0.438 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `eacfcbb4-fc96-4c2e-a148-e011f0bf5344` | human | 0.306 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `939ba2e6-e84b-4093-af80-5ac9120e3c14` | unsure | 0.431 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `95e49a3d-d24b-4bc4-a27c-91c2f9d8eab4` | unsure | 0.619 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `6086a6bd-9a2b-483c-af5c-b1896bd50439` | human | 0.201 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `9c941e58-2597-4d1c-a6e0-f1bb84f0e69c` | unsure | 0.470 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `2f5da2a5-dfd9-498d-9e46-5431d0c8cdc2` | unsure | 0.444 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `d62b1837-c160-48ac-9e00-1bf5d45f6838` | unsure | 0.471 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `a35d1585-508e-4693-a672-b932a220b5bc` | unsure | 0.435 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `ff0bdad7-bf48-4e9f-ae9e-e44e30075b4b` | ai | 0.868 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c8a94c05-9d6f-4781-8813-292a20b23529` | unsure | 0.598 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `2b9229ac-c21a-40ac-b2dd-a5c398a70bc8` | unsure | 0.791 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c9261147-2147-4873-87a3-2d82c0162cb6` | unsure | 0.765 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `364e0398-f986-4a0e-9d8d-a28c7bc8a2ef` | unsure | 0.726 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c5b59feb-d089-4e08-928c-a1f027ab9359` | ai | 0.840 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `9ab30a36-ff10-4f7d-a6dc-1c60431a576e` | unsure | 0.600 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d5f45a5b-f927-4614-8a02-f6cddb1f86ca` | unsure | 0.691 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `795d8a19-4f27-48fa-8cef-2f7ae1b19367` | unsure | 0.415 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `d41ea148-3466-4301-b87d-dcc8d8b0e28f` | human | 0.381 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `371534a5-cc03-4f9e-bb87-53f567b379b3` | human | 0.169 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ddefaead-7bf7-47ee-a8cf-4c6d95c8db4e` | unsure | 0.458 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4cde7944-f280-4971-9989-c3c85e8afc7e` | human | 0.377 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d6b94bd7-47ef-4969-a3b9-ce013f5604dc` | unsure | 0.400 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `941819bf-d630-4aaf-8d45-c7a3fad307f7` | unsure | 0.566 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 422 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `f5d6a22a-d56b-48a4-963e-85f675369860` | human | 0.275 |  |
| MF04 | malformed | text is only punctuation | 200 | `2e0cfe31-2cfc-4b77-8988-446724b3895d` | human | 0.381 |  |
| MF05 | malformed | text is a very long single word | 200 | `e14c48bc-34a5-4705-afa6-eda80908e092` | unsure | 0.774 |  |
| MF06 | malformed | text is emoji only | 200 | `ed51dee6-c43b-4943-8edd-c65579197aa8` | ai | 0.874 |  |
| MF07 | malformed | text is right-to-left script | 200 | `1cae6b0d-6e1f-49ca-9476-19dcee3e89d0` | ai | 0.828 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6a5056a9-d947-431e-8caa-9cae05b9fcbf` | human | 0.289 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2d68b3b7-6cc1-4889-90de-648f224dccc2` | human | 0.289 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3d7c0b10-becb-4723-b8b5-fb1eee706016` | human | 0.289 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3bb015c5-05b9-4a2f-ac4e-04f642e285af` | human | 0.289 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `82683048-6d1b-4cf3-b51e-63331f1b86a8` | human | 0.289 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "e93a065e-e2cb-4102-a67d-f1ba95ed1c5e",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4376,
  "model_score": 0.1635,
  "style_score": 0.7118,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "eacfcbb4-fc96-4c2e-a148-e011f0bf5344",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.3058,
  "model_score": 0.5943,
  "style_score": 0.0172,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "939ba2e6-e84b-4093-af80-5ac9120e3c14",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.431,
  "model_score": 0.6662,
  "style_score": 0.1958,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "95e49a3d-d24b-4bc4-a27c-91c2f9d8eab4",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6185,
  "model_score": 0.6114,
  "style_score": 0.6256,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "6086a6bd-9a2b-483c-af5c-b1896bd50439",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2006,
  "model_score": 0.3212,
  "style_score": 0.0801,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "9c941e58-2597-4d1c-a6e0-f1bb84f0e69c",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4697,
  "model_score": 0.5727,
  "style_score": 0.3667,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "2f5da2a5-dfd9-498d-9e46-5431d0c8cdc2",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4437,
  "model_score": 0.5862,
  "style_score": 0.3012,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d62b1837-c160-48ac-9e00-1bf5d45f6838",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4708,
  "model_score": 0.2452,
  "style_score": 0.6964,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "a35d1585-508e-4693-a672-b932a220b5bc",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4349,
  "model_score": 0.7042,
  "style_score": 0.1656,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "ff0bdad7-bf48-4e9f-ae9e-e44e30075b4b",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8684,
  "model_score": 0.9792,
  "style_score": 0.7576,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c8a94c05-9d6f-4781-8813-292a20b23529",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5978,
  "model_score": 0.6175,
  "style_score": 0.5781,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "2b9229ac-c21a-40ac-b2dd-a5c398a70bc8",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7906,
  "model_score": 0.7387,
  "style_score": 0.8425,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c9261147-2147-4873-87a3-2d82c0162cb6",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7648,
  "model_score": 0.8051,
  "style_score": 0.7245,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "364e0398-f986-4a0e-9d8d-a28c7bc8a2ef",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.726,
  "model_score": 0.8329,
  "style_score": 0.6191,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c5b59feb-d089-4e08-928c-a1f027ab9359",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8403,
  "model_score": 0.8005,
  "style_score": 0.8801,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "9ab30a36-ff10-4f7d-a6dc-1c60431a576e",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.8814,
  "style_score": 0.4781,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "d5f45a5b-f927-4614-8a02-f6cddb1f86ca",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6908,
  "model_score": 0.8816,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "795d8a19-4f27-48fa-8cef-2f7ae1b19367",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4155,
  "model_score": 0.3223,
  "style_score": 0.5087,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "d41ea148-3466-4301-b87d-dcc8d8b0e28f",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3812,
  "model_score": 0.4625,
  "style_score": 0.3,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "371534a5-cc03-4f9e-bb87-53f567b379b3",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1689,
  "model_score": 0.2044,
  "style_score": 0.1333,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "ddefaead-7bf7-47ee-a8cf-4c6d95c8db4e",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4577,
  "model_score": 0.5943,
  "style_score": 0.3212,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "4cde7944-f280-4971-9989-c3c85e8afc7e",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.377,
  "model_score": 0.4998,
  "style_score": 0.2541,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "d6b94bd7-47ef-4969-a3b9-ce013f5604dc",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4004,
  "model_score": 0.6401,
  "style_score": 0.1607,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "941819bf-d630-4aaf-8d45-c7a3fad307f7",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5657,
  "model_score": 0.5583,
  "style_score": 0.5732,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "f5d6a22a-d56b-48a4-963e-85f675369860",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.275,
  "model_score": 0.0,
  "style_score": 0.55,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "2e0cfe31-2cfc-4b77-8988-446724b3895d",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3806,
  "model_score": 0.0112,
  "style_score": 0.75,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "e14c48bc-34a5-4705-afa6-eda80908e092",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.7738,
  "model_score": 0.9976,
  "style_score": 0.55,
  "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "ed51dee6-c43b-4943-8edd-c65579197aa8",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8735,
  "model_score": 0.9969,
  "style_score": 0.75,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "1cae6b0d-6e1f-49ca-9476-19dcee3e89d0",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8282,
  "model_score": 0.9064,
  "style_score": 0.75,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "6a5056a9-d947-431e-8caa-9cae05b9fcbf",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2893,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "2d68b3b7-6cc1-4889-90de-648f224dccc2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2893,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "3d7c0b10-becb-4723-b8b5-fb1eee706016",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2893,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "3bb015c5-05b9-4a2f-ac4e-04f642e285af",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2893,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "82683048-6d1b-4cf3-b51e-63331f1b86a8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2893,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
