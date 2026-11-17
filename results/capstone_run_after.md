# Capstone run: after fix

Three trials of the capstone criteria (C1–C5) after the C4 fix (`before_request` timer in `app.py`), copied from the terminal. Same commands and texts as `capstone_run_before.md`. C1–C3 ran with `AI201_DETECTOR_MODEL=no-such-model`, C4–C5 with plain `python app.py`, restarted between the two halves.

Lines that show only `>....` are where the terminal folded a long pasted command; the requests themselves ran, and every one of them is in `logs/audit.jsonl`.

## Trial 1 (a1)

Pasted in three parts. In the first part, after the failure half, I forgot to start the normal service, so the C5 and C4 requests hit macOS's AirPlay receiver on port 5000 and got `403`. None of them reached the app or wrote to the log. I then started `python app.py` and ran the C4 batch (second part) and the C5 batch (third part). This is the run where C4 ran before C5.

### Part 1: failure half, then the 403s

```
Last login: Mon Nov 16 14:38:24 on ttys000
(base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % cd ~/ai201-project4-provenance-guard-starter-v2026
(base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % source .venv/bin/activate
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % T=a1
TEXT="This is a normal paragraph with several sentences. It should be long enough to score. Nothing about it is unusual."
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_1\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_2\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_3\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_4\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_5\",\"text\":\"$TEXT\"}"
curl -s "http://127.0.0.1:5000/log?limit=5"
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "count": 5,
  "entries": [
    {
      "creator_id": "a1_fail_1",
      "duration_ms": 2024.0,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:40:58+00:00"
    },
    {
      "creator_id": "a1_fail_2",
      "duration_ms": 90.2,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:40:58+00:00"
    },
    {
      "creator_id": "a1_fail_3",
      "duration_ms": 100.8,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:40:58+00:00"
    },
    {
      "creator_id": "a1_fail_4",
      "duration_ms": 90.8,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:40:58+00:00"
    },
    {
      "creator_id": "a1_fail_5",
      "duration_ms": 62.3,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:40:58+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
curl -s -o /dev/null -w "warmup %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_1.json; sleep 13
curl -s -o /dev/null -w "short 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_1.json; sleep 13
curl -s -o /dev/null -w "short 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_2.json; sleep 13
curl -s -o /dev/null -w "short 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_3.json; sleep 13
curl -s -o /dev/null -w "short 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_4.json; sleep 13
curl -s -o /dev/null -w "short 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_5.json; sleep 13
curl -s -o /dev/null -w "long 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_6.json; sleep 13
curl -s -o /dev/null -w "long 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_7.json; sleep 13
curl -s -o /dev/null -w "long 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_8.json; sleep 13
curl -s -o /dev/null -w "long 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_9.json; sleep 13
curl -s -o /dev/null -w "long 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_10.json
curl -s "http://127.0.0.1:5000/log?limit=10"
long 1 2142 chars
long 2 2510 chars
long 3 2418 chars
long 4 2304 chars
long 5 5855 chars
warmup 403
short 1 403
short 2 403
short 3 403
short 4 403
short 5 403
long 1 403
long 2 403
long 3 403
long 4 403
long 5 403
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
",\"text\":\"hi\"}"
curl -s -o /dev/null -w "too long %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4_long\",\"text\":\"$LONG\"}"
curl -s -o /dev/null -w "normal 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 6 (expect 429) %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s "http://127.0.0.1:5000/log?limit=10"
invalid json 403
missing text 403
too short 403
too long 403
normal 1 403
normal 2 403
normal 3 403
normal 4 403
normal 5 403
normal 6 (expect 429) 403
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 %
```

### Part 2: C4, after starting `python app.py`

```
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
",\"text\":\"hi\"}"
curl -s -o /dev/null -w "too long %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4_long\",\"text\":\"$LONG\"}"
curl -s -o /dev/null -w "normal 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 6 (expect 429) %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s "http://127.0.0.1:5000/log?limit=10"
invalid json 400
missing text 400
too short 422
too long 413
normal 1 200
normal 2 200
normal 3 200
normal 4 200
normal 5 200
normal 6 (expect 429) 429
{
  "count": 10,
  "entries": [
    {
      "creator_id": "unknown",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "invalid_json",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-16T20:46:38+00:00"
    },
    {
      "creator_id": "a1_c4_missing",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-16T20:46:38+00:00"
    },
    {
      "creator_id": "a1_c4_short",
      "duration_ms": 2840.1,
      "event": "rejected",
      "reason": "text_too_short",
      "status": "rejected",
      "text_chars": 2,
      "timestamp": "2026-11-16T20:46:41+00:00"
    },
    {
      "creator_id": "a1_c4_long",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "text_too_long",
      "status": "rejected",
      "text_chars": 20005,
      "timestamp": "2026-11-16T20:46:41+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "93cc1044-6b61-40d0-b8f8-878f9685c0ca",
      "creator_id": "a1_c4",
      "duration_ms": 838.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:46:42+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "4296dcb1-32dd-4d49-bea0-ac4f2e4d9c8b",
      "creator_id": "a1_c4",
      "duration_ms": 23.5,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:46:42+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "e7c5ea08-8918-485c-a87e-31689f439911",
      "creator_id": "a1_c4",
      "duration_ms": 23.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:46:42+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "60995ba5-afc5-42d8-922b-2441618c9609",
      "creator_id": "a1_c4",
      "duration_ms": 24.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:46:42+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "c06777e5-f237-4b22-9bde-81ccd4e171ca",
      "creator_id": "a1_c4",
      "duration_ms": 24.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:46:42+00:00"
    },
    {
      "creator_id": "a1_c4",
      "duration_ms": 0.2,
      "event": "rejected",
      "limit": "5 per 1 minute",
      "reason": "rate_limited",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:46:42+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 %
```

### Part 3: C5

```
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
curl -s -o /dev/null -w "warmup %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_1.json; sleep 13
curl -s -o /dev/null -w "short 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_1.json; sleep 13
curl -s -o /dev/null -w "short 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_2.json; sleep 13
curl -s -o /dev/null -w "short 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_3.json; sleep 13
curl -s -o /dev/null -w "short 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_4.json; sleep 13
curl -s -o /dev/null -w "short 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_5.json; sleep 13
curl -s -o /dev/null -w "long 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_6.json; sleep 13
curl -s -o /dev/null -w "long 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_7.json; sleep 13
curl -s -o /dev/null -w "long 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_8.json; sleep 13
curl -s -o /dev/null -w "long 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_9.json; sleep 13
curl -s -o /dev/null -w "long 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_10.json
curl -s "http://127.0.0.1:5000/log?limit=10"
long 1 2142 chars
long 2 2510 chars
long 3 2418 chars
long 4 2304 chars
long 5 5855 chars
warmup 200
short 1 200
short 2 200
short 3 200
short 4 200
short 5 200
long 1 200
long 2 200
long 3 200
long 4 200
long 5 200
{
  "count": 10,
  "entries": [
    {
      "combined_score": 0.6,
      "content_id": "69d6bb2a-a199-4363-8ae0-adcea5251a84",
      "creator_id": "a1_short_1",
      "duration_ms": 39.6,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:48:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "53327df3-1aaa-4f31-8244-c3900a7ffa68",
      "creator_id": "a1_short_2",
      "duration_ms": 31.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:48:18+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "18f1c211-087d-4d82-a972-8c10736a7739",
      "creator_id": "a1_short_3",
      "duration_ms": 28.6,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:48:31+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "573ed007-a2fa-41d3-8e4b-90f9f031b6fe",
      "creator_id": "a1_short_4",
      "duration_ms": 31.6,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:48:44+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "1af2bfc0-4542-4f1c-9b48-073ab458c46f",
      "creator_id": "a1_short_5",
      "duration_ms": 30.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:48:57+00:00"
    },
    {
      "combined_score": 0.5101,
      "content_id": "95052d33-7ea9-4589-94cf-1be4c4f978ab",
      "creator_id": "a1_long_1",
      "duration_ms": 163.8,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8926,
      "status": "decided",
      "style_score": 0.1275,
      "text_chars": 2142,
      "timestamp": "2026-11-16T20:49:10+00:00"
    },
    {
      "combined_score": 0.3997,
      "content_id": "52dc89f1-ee30-4d4d-8eb5-648b96e66d7e",
      "creator_id": "a1_long_2",
      "duration_ms": 180.5,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.7726,
      "status": "decided",
      "style_score": 0.0269,
      "text_chars": 2510,
      "timestamp": "2026-11-16T20:49:24+00:00"
    },
    {
      "combined_score": 0.5894,
      "content_id": "2cd0c42c-0720-4ff3-b4d7-411867bce05f",
      "creator_id": "a1_long_3",
      "duration_ms": 164.5,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8231,
      "status": "decided",
      "style_score": 0.3556,
      "text_chars": 2418,
      "timestamp": "2026-11-16T20:49:37+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "bd3d679a-1c33-41c5-946e-263365d3fd93",
      "creator_id": "a1_long_4",
      "duration_ms": 166.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8074,
      "status": "decided",
      "style_score": 0.492,
      "text_chars": 2304,
      "timestamp": "2026-11-16T20:49:50+00:00"
    },
    {
      "combined_score": 0.3857,
      "content_id": "fd5dc213-24cd-4c91-81d0-b2a2d3af21db",
      "creator_id": "a1_long_5",
      "duration_ms": 161.1,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.6146,
      "status": "decided",
      "style_score": 0.1568,
      "text_chars": 5855,
      "timestamp": "2026-11-16T20:50:03+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 %
```

## Trial 2 (a2)

```
Last login: Mon Nov 16 14:50:51 on ttys000
(base) evannashen@Evannas-MacBook-Air-3 ~ % cd ~/ai201-project4-provenance-guard-starter-v2026
(base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % source .venv/bin/activate
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % T=a2
TEXT="This is a normal paragraph with several sentences. It should be long enough to score. Nothing about it is unusual."
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_1\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_2\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_3\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_4\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_5\",\"text\":\"$TEXT\"}"
curl -s "http://127.0.0.1:5000/log?limit=5"
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "count": 5,
  "entries": [
    {
      "creator_id": "a2_fail_1",
      "duration_ms": 1902.1,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:51:33+00:00"
    },
    {
      "creator_id": "a2_fail_2",
      "duration_ms": 104.5,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:51:33+00:00"
    },
    {
      "creator_id": "a2_fail_3",
      "duration_ms": 91.8,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:51:33+00:00"
    },
    {
      "creator_id": "a2_fail_4",
      "duration_ms": 90.1,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:51:33+00:00"
    },
    {
      "creator_id": "a2_fail_5",
      "duration_ms": 69.1,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:51:33+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
curl -s -o /dev/null -w "warmup %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_1.json; sleep 13
curl -s -o /dev/null -w "short 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_1.json; sleep 13
curl -s -o /dev/null -w "short 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_2.json; sleep 13
curl -s -o /dev/null -w "short 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_3.json; sleep 13
curl -s -o /dev/null -w "short 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_4.json; sleep 13
curl -s -o /dev/null -w "short 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_5.json; sleep 13
curl -s -o /dev/null -w "long 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_6.json; sleep 13
curl -s -o /dev/null -w "long 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_7.json; sleep 13
curl -s -o /dev/null -w "long 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_8.json; sleep 13
curl -s -o /dev/null -w "long 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_9.json; sleep 13
curl -s -o /dev/null -w "long 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_10.json
curl -s "http://127.0.0.1:5000/log?limit=10"
long 1 2142 chars
long 2 2510 chars
long 3 2418 chars
long 4 2304 chars
long 5 5855 chars
warmup 200
short 1 200
short 2 200
short 3 200
short 4 200
short 5 200
long 1 200
long 2 200
long 3 200
long 4 200
long 5 200
{
  "count": 10,
  "entries": [
    {
      "combined_score": 0.6,
      "content_id": "ba8c7551-8694-46da-bbe6-867d16674b99",
      "creator_id": "a2_short_1",
      "duration_ms": 30.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:52:08+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "2eabb219-1487-4217-90c8-9af56066e976",
      "creator_id": "a2_short_2",
      "duration_ms": 29.7,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:52:21+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "e99c78b7-3ec1-4a48-868d-6919486a6f56",
      "creator_id": "a2_short_3",
      "duration_ms": 29.8,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:52:34+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "951018af-6430-41bd-8902-56d6dc3a38b8",
      "creator_id": "a2_short_4",
      "duration_ms": 30.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:52:47+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "37cce39f-7106-4d3e-b73a-7df5a95a832a",
      "creator_id": "a2_short_5",
      "duration_ms": 29.0,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:53:00+00:00"
    },
    {
      "combined_score": 0.5101,
      "content_id": "ce19b32c-4446-408d-b81f-f7ad0d20520c",
      "creator_id": "a2_long_1",
      "duration_ms": 148.8,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8926,
      "status": "decided",
      "style_score": 0.1275,
      "text_chars": 2142,
      "timestamp": "2026-11-16T20:53:14+00:00"
    },
    {
      "combined_score": 0.3997,
      "content_id": "3911e9be-d86b-4396-9d6d-344a7958d91a",
      "creator_id": "a2_long_2",
      "duration_ms": 168.1,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.7726,
      "status": "decided",
      "style_score": 0.0269,
      "text_chars": 2510,
      "timestamp": "2026-11-16T20:53:27+00:00"
    },
    {
      "combined_score": 0.5894,
      "content_id": "4c4260b3-f96b-4622-8718-d1ae553be7f6",
      "creator_id": "a2_long_3",
      "duration_ms": 159.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8231,
      "status": "decided",
      "style_score": 0.3556,
      "text_chars": 2418,
      "timestamp": "2026-11-16T20:53:40+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "fd44cb97-4a98-4638-b170-4e4d2dd4d58f",
      "creator_id": "a2_long_4",
      "duration_ms": 160.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8074,
      "status": "decided",
      "style_score": 0.492,
      "text_chars": 2304,
      "timestamp": "2026-11-16T20:53:53+00:00"
    },
    {
      "combined_score": 0.3857,
      "content_id": "dba66cb1-888c-4f52-a7b4-6f3ca5775c35",
      "creator_id": "a2_long_5",
      "duration_ms": 160.1,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.6146,
      "status": "decided",
      "style_score": 0.1568,
      "text_chars": 5855,
      "timestamp": "2026-11-16T20:54:06+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
",\"text\":\"hi\"}"
curl -s -o /dev/null -w "too long %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4_long\",\"text\":\"$LONG\"}"
curl -s -o /dev/null -w "normal 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 6 (expect 429) %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s "http://127.0.0.1:5000/log?limit=10"
invalid json 400
missing text 400
too short 422
too long 413
normal 1 200
normal 2 200
normal 3 200
normal 4 200
normal 5 200
normal 6 (expect 429) 429
{
  "count": 10,
  "entries": [
    {
      "creator_id": "unknown",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "invalid_json",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "creator_id": "a2_c4_missing",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "creator_id": "a2_c4_short",
      "duration_ms": 0.2,
      "event": "rejected",
      "reason": "text_too_short",
      "status": "rejected",
      "text_chars": 2,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "creator_id": "a2_c4_long",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "text_too_long",
      "status": "rejected",
      "text_chars": 20005,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "106edadd-9e8b-4d15-a5cb-eec3cb45d858",
      "creator_id": "a2_c4",
      "duration_ms": 25.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "8f5ba876-fc22-4825-b5ac-1e22108aae51",
      "creator_id": "a2_c4",
      "duration_ms": 24.0,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "1bd4f8a3-1e59-48ce-8b9f-7fdc358341ec",
      "creator_id": "a2_c4",
      "duration_ms": 23.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "03ecd72e-1310-4f80-a9a9-10226d5fd316",
      "creator_id": "a2_c4",
      "duration_ms": 23.5,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "32a75ba4-db44-43e4-9771-c98f0da235e0",
      "creator_id": "a2_c4",
      "duration_ms": 25.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T20:54:53+00:00"
    },
    {
      "creator_id": "a2_c4",
      "duration_ms": 0.2,
      "event": "rejected",
      "limit": "5 per 1 minute",
      "reason": "rate_limited",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T20:54:53+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 %
```

## Trial 3 (a3)

```
Last login: Mon Nov 16 14:58:53 on ttys000
(base) evannashen@Evannas-MacBook-Air-3 ~ % cd ~/ai201-project4-provenance-guard-starter-v2026
(base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % source .venv/bin/activate
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % T=a3
TEXT="This is a normal paragraph with several sentences. It should be long enough to score. Nothing about it is unusual."
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_1\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_2\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_3\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_4\",\"text\":\"$TEXT\"}"
curl -s -w " %{http_code} %{content_type}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_fail_5\",\"text\":\"$TEXT\"}"
curl -s "http://127.0.0.1:5000/log?limit=5"
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "error": "scoring_failed",
  "message": "We couldn't check this right now, so nothing has been decided about your text. Please try again in a minute."
}
 503 application/json
{
  "count": 5,
  "entries": [
    {
      "creator_id": "a3_fail_1",
      "duration_ms": 1939.7,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T21:03:07+00:00"
    },
    {
      "creator_id": "a3_fail_2",
      "duration_ms": 96.8,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T21:03:07+00:00"
    },
    {
      "creator_id": "a3_fail_3",
      "duration_ms": 95.2,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T21:03:07+00:00"
    },
    {
      "creator_id": "a3_fail_4",
      "duration_ms": 93.2,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T21:03:07+00:00"
    },
    {
      "creator_id": "a3_fail_5",
      "duration_ms": 53.5,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T21:03:07+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
curl -s -o /dev/null -w "warmup %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_1.json; sleep 13
curl -s -o /dev/null -w "short 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_1.json; sleep 13
curl -s -o /dev/null -w "short 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_2.json; sleep 13
curl -s -o /dev/null -w "short 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_3.json; sleep 13
curl -s -o /dev/null -w "short 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_4.json; sleep 13
curl -s -o /dev/null -w "short 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_5.json; sleep 13
curl -s -o /dev/null -w "long 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_6.json; sleep 13
curl -s -o /dev/null -w "long 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_7.json; sleep 13
curl -s -o /dev/null -w "long 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_8.json; sleep 13
curl -s -o /dev/null -w "long 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_9.json; sleep 13
curl -s -o /dev/null -w "long 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d @/tmp/c5_10.json
curl -s "http://127.0.0.1:5000/log?limit=10"
long 1 2142 chars
long 2 2510 chars
long 3 2418 chars
long 4 2304 chars
long 5 5855 chars
warmup 200
short 1 200
short 2 200
short 3 200
short 4 200
short 5 200
long 1 200
long 2 200
long 3 200
long 4 200
long 5 200
{
  "count": 10,
  "entries": [
    {
      "combined_score": 0.6,
      "content_id": "c38552e9-2e91-4e2b-a991-39d279b961dc",
      "creator_id": "a3_short_1",
      "duration_ms": 33.4,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:03:56+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "0ebad879-7ca4-41e0-82d1-d7cac94f9b3e",
      "creator_id": "a3_short_2",
      "duration_ms": 33.7,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:04:09+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "4cbff21a-2c63-4487-9323-69e9d88dad36",
      "creator_id": "a3_short_3",
      "duration_ms": 29.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:04:22+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "fbd9547a-ffc1-4c2a-860a-179ee0640473",
      "creator_id": "a3_short_4",
      "duration_ms": 28.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:04:36+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "f6e26508-357e-494b-bdcb-a52606c10e32",
      "creator_id": "a3_short_5",
      "duration_ms": 30.8,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:04:49+00:00"
    },
    {
      "combined_score": 0.5101,
      "content_id": "4126dcc1-2c73-4857-a961-7dc29ed22cd3",
      "creator_id": "a3_long_1",
      "duration_ms": 150.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8926,
      "status": "decided",
      "style_score": 0.1275,
      "text_chars": 2142,
      "timestamp": "2026-11-16T21:05:02+00:00"
    },
    {
      "combined_score": 0.3997,
      "content_id": "57678adf-9dc5-462f-af82-88c5c6506c1a",
      "creator_id": "a3_long_2",
      "duration_ms": 167.5,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.7726,
      "status": "decided",
      "style_score": 0.0269,
      "text_chars": 2510,
      "timestamp": "2026-11-16T21:05:15+00:00"
    },
    {
      "combined_score": 0.5894,
      "content_id": "200e20e5-2b12-4c56-8db7-d8c70409e988",
      "creator_id": "a3_long_3",
      "duration_ms": 158.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8231,
      "status": "decided",
      "style_score": 0.3556,
      "text_chars": 2418,
      "timestamp": "2026-11-16T21:05:28+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "7b90095b-5829-4381-ba61-a96129e22691",
      "creator_id": "a3_long_4",
      "duration_ms": 159.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8074,
      "status": "decided",
      "style_score": 0.492,
      "text_chars": 2304,
      "timestamp": "2026-11-16T21:05:41+00:00"
    },
    {
      "combined_score": 0.3857,
      "content_id": "bdc3926a-c12b-4678-be5e-fd25127dba4d",
      "creator_id": "a3_long_5",
      "duration_ms": 161.4,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.6146,
      "status": "decided",
      "style_score": 0.1568,
      "text_chars": 5855,
      "timestamp": "2026-11-16T21:05:55+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
",\"text\":\"hi\"}"
curl -s -o /dev/null -w "too long %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4_long\",\"text\":\"$LONG\"}"
curl -s -o /dev/null -w "normal 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 5 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 6 (expect 429) %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s "http://127.0.0.1:5000/log?limit=10"
invalid json 400
missing text 400
too short 422
too long 413
normal 1 200
normal 2 200
normal 3 200
normal 4 200
normal 5 200
normal 6 (expect 429) 429
{
  "count": 10,
  "entries": [
    {
      "creator_id": "unknown",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "invalid_json",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-16T21:07:48+00:00"
    },
    {
      "creator_id": "a3_c4_missing",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-16T21:07:48+00:00"
    },
    {
      "creator_id": "a3_c4_short",
      "duration_ms": 0.2,
      "event": "rejected",
      "reason": "text_too_short",
      "status": "rejected",
      "text_chars": 2,
      "timestamp": "2026-11-16T21:07:48+00:00"
    },
    {
      "creator_id": "a3_c4_long",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "text_too_long",
      "status": "rejected",
      "text_chars": 20005,
      "timestamp": "2026-11-16T21:07:48+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "37436a39-b75f-4910-aca8-21061e8b8602",
      "creator_id": "a3_c4",
      "duration_ms": 43.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:07:48+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "1b3008f0-d711-435f-84f5-e9608a045baa",
      "creator_id": "a3_c4",
      "duration_ms": 23.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:07:48+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "9489d8c1-44e3-411d-bf2e-b2e30e9d6cdb",
      "creator_id": "a3_c4",
      "duration_ms": 23.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:07:48+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "5798a3d3-420a-480a-87c9-03565c531509",
      "creator_id": "a3_c4",
      "duration_ms": 22.7,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:07:48+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "30d9b833-513e-4c20-a78a-4373dcd9f337",
      "creator_id": "a3_c4",
      "duration_ms": 23.5,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-16T21:07:49+00:00"
    },
    {
      "creator_id": "a3_c4",
      "duration_ms": 0.2,
      "event": "rejected",
      "limit": "5 per 1 minute",
      "reason": "rate_limited",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-16T21:07:49+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 %
```

## Discarded trial

An earlier after-fix trial at 2026-11-16 17:32 UTC (creator IDs `t1_*`) ran with the laptop on battery: C4 10/10, but the five long texts took 227.1–277.3 ms, so C5 was 5/10. I didn't keep its full terminal output; its records are in `logs/audit.jsonl`. See The Improvement in the README.
