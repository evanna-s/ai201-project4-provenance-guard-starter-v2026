# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 21:20
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `1c1906c1-55d2-4bf7-8d71-91d005b57e54` | unsure | 0.438 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `367bc18c-3298-45ae-bd60-56fed8e8aa4e` | human | 0.306 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `817f70a9-e771-462c-b739-ea5042db66f4` | unsure | 0.431 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `257fcaa4-12a1-4172-9cd8-7c2802ca0209` | unsure | 0.619 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e0b2e8d0-ef99-4276-9764-fe83b54e304d` | human | 0.201 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `5de6756f-c5d8-45c0-bbdf-f5aa7edf197c` | unsure | 0.470 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `dc8ee9ca-a7fc-4b24-b58d-58bb66f34efc` | unsure | 0.444 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `b60b5b40-4c44-40ff-8a51-0a8daba7397e` | unsure | 0.471 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `f9e5c76d-2730-4a30-b356-f9c0a94d6691` | unsure | 0.435 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `56f8ec40-4c19-4f2f-8060-abb8673d0804` | ai | 0.868 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `035b8a3a-d22b-4c6b-aa78-aae19df9c931` | unsure | 0.598 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `eb474360-f25b-44a0-9a5c-073b57037c8b` | ai | 0.791 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `de8c3ab3-f9cc-49eb-a56b-55fe594c5f56` | ai | 0.765 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d15785ac-520d-4a7d-90db-45894a3f0177` | ai | 0.726 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `edac4067-0d62-4f8d-8f65-e4dc775a8322` | ai | 0.840 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `6df3faa7-f028-44b1-9a6f-092a6a10a09b` | unsure | 0.600 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `fb09f663-b9a1-4101-b99e-d9610e4345bf` | ai | 0.691 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `7dd434a4-d633-425a-9368-1df3197f867a` | unsure | 0.415 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `1c8fd250-ed2c-423a-962e-8401f76ae734` | human | 0.381 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d88ee252-7f6a-4b06-b26f-7054748dfbc9` | human | 0.169 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `cad1bf5d-664d-49f6-9faa-ee463f89d611` | unsure | 0.458 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `aeee5bf6-fe63-4154-9145-9b2cad1a965a` | human | 0.377 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a563baf7-0cb8-4ca4-b731-12bc90273c84` | unsure | 0.400 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `a8b6c1d3-0b07-4c72-9dd2-78c61ae533aa` | unsure | 0.566 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 422 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `c9e14f43-f515-4df8-8516-f0c9cf79a0cb` | human | 0.275 |  |
| MF04 | malformed | text is only punctuation | 200 | `a3e01b45-0fa2-4b05-bdd0-96120061ab6a` | human | 0.381 |  |
| MF05 | malformed | text is a very long single word | 200 | `336729c5-6212-473f-9c90-7c9ef3cae7c2` | ai | 0.774 |  |
| MF06 | malformed | text is emoji only | 200 | `92c738f5-99d6-413e-ad51-754fa42312c8` | ai | 0.874 |  |
| MF07 | malformed | text is right-to-left script | 200 | `927280fc-3ad8-4645-845d-a9a96ee1d8b1` | ai | 0.828 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `839af02a-0fc6-4a94-be61-4ca30ebf6584` | human | 0.289 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9986d191-babf-47d6-8bb8-fa1d2a03c345` | human | 0.289 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c7fca1c6-9554-4eba-b9eb-3034d78aa730` | human | 0.289 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `792d94c0-623e-473d-b740-db22bd84f66d` | human | 0.289 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e985f448-dc7a-493b-80ba-9717649cfde1` | human | 0.289 |  |
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
  "content_id": "1c1906c1-55d2-4bf7-8d71-91d005b57e54",
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
  "content_id": "367bc18c-3298-45ae-bd60-56fed8e8aa4e",
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
  "content_id": "817f70a9-e771-462c-b739-ea5042db66f4",
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
  "content_id": "257fcaa4-12a1-4172-9cd8-7c2802ca0209",
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
  "content_id": "e0b2e8d0-ef99-4276-9764-fe83b54e304d",
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
  "content_id": "5de6756f-c5d8-45c0-bbdf-f5aa7edf197c",
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
  "content_id": "dc8ee9ca-a7fc-4b24-b58d-58bb66f34efc",
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
  "content_id": "b60b5b40-4c44-40ff-8a51-0a8daba7397e",
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
  "content_id": "f9e5c76d-2730-4a30-b356-f9c0a94d6691",
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
  "content_id": "56f8ec40-4c19-4f2f-8060-abb8673d0804",
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
  "content_id": "035b8a3a-d22b-4c6b-aa78-aae19df9c931",
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
  "content_id": "eb474360-f25b-44a0-9a5c-073b57037c8b",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7906,
  "model_score": 0.7387,
  "style_score": 0.8425,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
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
  "content_id": "de8c3ab3-f9cc-49eb-a56b-55fe594c5f56",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7648,
  "model_score": 0.8051,
  "style_score": 0.7245,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
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
  "content_id": "d15785ac-520d-4a7d-90db-45894a3f0177",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.726,
  "model_score": 0.8329,
  "style_score": 0.6191,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
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
  "content_id": "edac4067-0d62-4f8d-8f65-e4dc775a8322",
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
  "content_id": "6df3faa7-f028-44b1-9a6f-092a6a10a09b",
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
  "content_id": "fb09f663-b9a1-4101-b99e-d9610e4345bf",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6908,
  "model_score": 0.8816,
  "style_score": 0.5,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
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
  "content_id": "7dd434a4-d633-425a-9368-1df3197f867a",
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
  "content_id": "1c8fd250-ed2c-423a-962e-8401f76ae734",
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
  "content_id": "d88ee252-7f6a-4b06-b26f-7054748dfbc9",
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
  "content_id": "cad1bf5d-664d-49f6-9faa-ee463f89d611",
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
  "content_id": "aeee5bf6-fe63-4154-9145-9b2cad1a965a",
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
  "content_id": "a563baf7-0cb8-4ca4-b731-12bc90273c84",
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
  "content_id": "a8b6c1d3-0b07-4c72-9dd2-78c61ae533aa",
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
  "content_id": "c9e14f43-f515-4df8-8516-f0c9cf79a0cb",
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
  "content_id": "a3e01b45-0fa2-4b05-bdd0-96120061ab6a",
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
  "content_id": "336729c5-6212-473f-9c90-7c9ef3cae7c2",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7738,
  "model_score": 0.9976,
  "style_score": 0.55,
  "label": "This writing looks a lot like AI-generated text, but our check can be wrong, especially on plain or simple writing. If you wrote this yourself, you can ask for a person to review it.",
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
  "content_id": "92c738f5-99d6-413e-ad51-754fa42312c8",
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
  "content_id": "927280fc-3ad8-4645-845d-a9a96ee1d8b1",
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
  "content_id": "839af02a-0fc6-4a94-be61-4ca30ebf6584",
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
  "content_id": "9986d191-babf-47d6-8bb8-fa1d2a03c345",
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
  "content_id": "c7fca1c6-9554-4eba-b9eb-3034d78aa730",
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
  "content_id": "792d94c0-623e-473d-b740-db22bd84f66d",
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
  "content_id": "e985f448-dc7a-493b-80ba-9717649cfde1",
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
