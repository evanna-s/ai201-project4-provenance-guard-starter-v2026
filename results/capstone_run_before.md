# Capstone run: before fix

Three trials of the capstone criteria (C1–C5), copied from the terminal. C1–C3 ran with `AI201_DETECTOR_MODEL=no-such-model`, C4–C5 with plain `python app.py`. Matching log entries: creator IDs `t1_*`, `t2_*`, `t3_*` in `logs/audit.jsonl`.

## Trial 1 (t1)

```
Last login: Sun Nov 15 15:12:22 on ttys003
(base) evannashen@Evannas-MacBook-Air-3 ~ % source .venv/bin/activate
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ~ % cd ~/ai201-project4-provenance-guard-starter-v2026
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % T=t1
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
      "creator_id": "t1_fail_1",
      "duration_ms": 1920.0,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:13:46+00:00"
    },
    {
      "creator_id": "t1_fail_2",
      "duration_ms": 89.2,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:13:46+00:00"
    },
    {
      "creator_id": "t1_fail_3",
      "duration_ms": 92.1,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:13:46+00:00"
    },
    {
      "creator_id": "t1_fail_4",
      "duration_ms": 100.0,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:13:46+00:00"
    },
    {
      "creator_id": "t1_fail_5",
      "duration_ms": 53.5,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:13:46+00:00"
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
      "content_id": "3d73110d-10ca-4c08-9a1b-b62f46b287b1",
      "creator_id": "t1_short_1",
      "duration_ms": 27.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:14:21+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "2fc86267-f3ef-4694-89b5-338ab089142c",
      "creator_id": "t1_short_2",
      "duration_ms": 30.5,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:14:34+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "cd88ce76-7bd8-4178-be6f-f27b975b3190",
      "creator_id": "t1_short_3",
      "duration_ms": 41.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:14:47+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "ab40946c-dbf3-4600-9c34-9c91fdf6cbce",
      "creator_id": "t1_short_4",
      "duration_ms": 37.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:15:00+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "dcbf5e8e-0236-4050-a0b5-cf35bac22bb9",
      "creator_id": "t1_short_5",
      "duration_ms": 36.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:15:13+00:00"
    },
    {
      "combined_score": 0.5101,
      "content_id": "67b98f9a-3b83-4580-8f3e-945f650f7443",
      "creator_id": "t1_long_1",
      "duration_ms": 147.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8926,
      "status": "decided",
      "style_score": 0.1275,
      "text_chars": 2142,
      "timestamp": "2026-11-15T21:15:27+00:00"
    },
    {
      "combined_score": 0.3997,
      "content_id": "8659843e-28ca-4530-a8d5-7396736b67f8",
      "creator_id": "t1_long_2",
      "duration_ms": 174.4,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.7726,
      "status": "decided",
      "style_score": 0.0269,
      "text_chars": 2510,
      "timestamp": "2026-11-15T21:15:40+00:00"
    },
    {
      "combined_score": 0.5894,
      "content_id": "e06454ff-9641-4d74-a2a3-b2271292d814",
      "creator_id": "t1_long_3",
      "duration_ms": 155.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8231,
      "status": "decided",
      "style_score": 0.3556,
      "text_chars": 2418,
      "timestamp": "2026-11-15T21:15:53+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "6252315e-dae2-4606-9c81-de214c65c3a2",
      "creator_id": "t1_long_4",
      "duration_ms": 158.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8074,
      "status": "decided",
      "style_score": 0.492,
      "text_chars": 2304,
      "timestamp": "2026-11-15T21:16:06+00:00"
    },
    {
      "combined_score": 0.3857,
      "content_id": "202ef628-38c1-41c2-a688-1af0e025d5e5",
      "creator_id": "t1_long_5",
      "duration_ms": 160.1,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.6146,
      "status": "decided",
      "style_score": 0.1568,
      "text_chars": 5855,
      "timestamp": "2026-11-15T21:16:19+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % >....                                                           
000/submit -H "Content-Type: application/json" -d "not json"
curl -s -o /dev/null -w "missing text %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4_missing\"}"           
curl -s -o /dev/null -w "too short %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4_short\",\"text\":\"hi\"}" 
curl -s -o /dev/null -w "too long %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4_long\",\"text\":\"$LONG\"}"
curl -s -o /dev/null -w "normal 1 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 2 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 3 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -w "normal 4 %{http_code}\n" -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"creator_id\":\"${T}_c4\",\"text\":\"$TEXT\"}"
curl -s -o /dev/null -wç                                                      
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
      "timestamp": "2026-11-15T21:18:04+00:00"
    },
    {
      "creator_id": "t1_c4_missing",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-15T21:18:04+00:00"
    },
    {
      "creator_id": "t1_c4_short",
      "duration_ms": 0.6,
      "event": "rejected",
      "reason": "text_too_short",
      "status": "rejected",
      "text_chars": 2,
      "timestamp": "2026-11-15T21:18:04+00:00"
    },
    {
      "creator_id": "t1_c4_long",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "text_too_long",
      "status": "rejected",
      "text_chars": 20005,
      "timestamp": "2026-11-15T21:18:04+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "23a686fb-19cb-48a6-b2a9-956e96f1b490",
      "creator_id": "t1_c4",
      "duration_ms": 127.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:18:04+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "3e74b22f-cc98-412f-b578-a5e0feed44cc",
      "creator_id": "t1_c4",
      "duration_ms": 23.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:18:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "d1441d08-6b93-4465-81b2-8908259bf9d3",
      "creator_id": "t1_c4",
      "duration_ms": 23.6,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:18:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "05b5d8d6-9212-4b88-b78c-fea46db30c46",
      "creator_id": "t1_c4",
      "duration_ms": 45.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:18:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "55bf7ded-44ef-4f0a-ab95-6a69394273db",
      "creator_id": "t1_c4",
      "duration_ms": 22.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:18:05+00:00"
    },
    {
      "creator_id": "t1_c4",
      "event": "rejected",
      "limit": "5 per 1 minute",
      "reason": "rate_limited",
      "status": "rejected",
      "timestamp": "2026-11-15T21:18:05+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 %
```

## Trial 2 (t2)

```
Last login: Sun Nov 15 15:19:13 on ttys004
(base) evannashen@Evannas-MacBook-Air-3 ~ % cd ~/ai201-project4-provenance-guard-starter-v2026
(base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % source .venv/bin/activate
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % T=t2
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
      "creator_id": "t2_fail_1",
      "duration_ms": 1922.9,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:20:07+00:00"
    },
    {
      "creator_id": "t2_fail_2",
      "duration_ms": 100.3,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:20:08+00:00"
    },
    {
      "creator_id": "t2_fail_3",
      "duration_ms": 93.9,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:20:08+00:00"
    },
    {
      "creator_id": "t2_fail_4",
      "duration_ms": 99.4,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:20:08+00:00"
    },
    {
      "creator_id": "t2_fail_5",
      "duration_ms": 53.9,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:20:08+00:00"
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
      "content_id": "6ada04af-2d76-4375-8240-209ce0179e5c",
      "creator_id": "t2_short_1",
      "duration_ms": 30.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:20:44+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "93a3f6a0-3396-4097-aa3b-c50119197450",
      "creator_id": "t2_short_2",
      "duration_ms": 33.7,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:20:57+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "f2c21dee-3731-4730-b5a9-3aa2346fa614",
      "creator_id": "t2_short_3",
      "duration_ms": 65.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:21:10+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "c7c445e7-686e-4145-acab-fcaf569190df",
      "creator_id": "t2_short_4",
      "duration_ms": 33.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:21:23+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "92df70ef-83c4-4f75-8184-e4f898fb49cf",
      "creator_id": "t2_short_5",
      "duration_ms": 34.6,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:21:36+00:00"
    },
    {
      "combined_score": 0.5101,
      "content_id": "3f030eb0-fb6f-4e5a-ba56-3ae205db3ff4",
      "creator_id": "t2_long_1",
      "duration_ms": 158.5,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8926,
      "status": "decided",
      "style_score": 0.1275,
      "text_chars": 2142,
      "timestamp": "2026-11-15T21:21:49+00:00"
    },
    {
      "combined_score": 0.3997,
      "content_id": "a39ba366-9322-473f-b073-92059746ff66",
      "creator_id": "t2_long_2",
      "duration_ms": 176.7,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.7726,
      "status": "decided",
      "style_score": 0.0269,
      "text_chars": 2510,
      "timestamp": "2026-11-15T21:22:02+00:00"
    },
    {
      "combined_score": 0.5894,
      "content_id": "bd79a073-9b61-49de-b1ff-36d4002566bc",
      "creator_id": "t2_long_3",
      "duration_ms": 172.4,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8231,
      "status": "decided",
      "style_score": 0.3556,
      "text_chars": 2418,
      "timestamp": "2026-11-15T21:22:16+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "40ff0ae7-a138-4a44-807d-ea0ec9121416",
      "creator_id": "t2_long_4",
      "duration_ms": 159.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8074,
      "status": "decided",
      "style_score": 0.492,
      "text_chars": 2304,
      "timestamp": "2026-11-15T21:22:29+00:00"
    },
    {
      "combined_score": 0.3857,
      "content_id": "7f6154d0-af75-4de5-9944-a0df445ca507",
      "creator_id": "t2_long_5",
      "duration_ms": 194.2,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.6146,
      "status": "decided",
      "style_score": 0.1568,
      "text_chars": 5855,
      "timestamp": "2026-11-15T21:22:42+00:00"
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
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "creator_id": "t2_c4_missing",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "creator_id": "t2_c4_short",
      "duration_ms": 0.3,
      "event": "rejected",
      "reason": "text_too_short",
      "status": "rejected",
      "text_chars": 2,
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "creator_id": "t2_c4_long",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "text_too_long",
      "status": "rejected",
      "text_chars": 20005,
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "0c3903f7-2c39-4710-b024-7ac98b0b41d2",
      "creator_id": "t2_c4",
      "duration_ms": 25.6,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "9b4e675d-b076-4180-9950-05b0c1408415",
      "creator_id": "t2_c4",
      "duration_ms": 23.6,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "a4a66c26-01ab-4697-a535-e793f0f47378",
      "creator_id": "t2_c4",
      "duration_ms": 29.7,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "45326c08-6b5f-4a3c-830c-7a087225387b",
      "creator_id": "t2_c4",
      "duration_ms": 23.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "51cf42e8-aeee-4369-a7ec-c7cf9cbc7a71",
      "creator_id": "t2_c4",
      "duration_ms": 23.8,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:23:05+00:00"
    },
    {
      "creator_id": "t2_c4",
      "event": "rejected",
      "limit": "5 per 1 minute",
      "reason": "rate_limited",
      "status": "rejected",
      "timestamp": "2026-11-15T21:23:05+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 %
```

## Trial 3 (t3)

```
Last login: Sun Nov 15 15:23:35 on ttys006
(base) evannashen@Evannas-MacBook-Air-3 ~ % cd ~/ai201-project4-provenance-guard-starter-v2026
(base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % source .venv/bin/activate
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 % T=t3
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
      "creator_id": "t3_fail_1",
      "duration_ms": 1930.3,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:32:48+00:00"
    },
    {
      "creator_id": "t3_fail_2",
      "duration_ms": 91.1,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:32:48+00:00"
    },
    {
      "creator_id": "t3_fail_3",
      "duration_ms": 102.3,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:32:48+00:00"
    },
    {
      "creator_id": "t3_fail_4",
      "duration_ms": 93.8,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:32:48+00:00"
    },
    {
      "creator_id": "t3_fail_5",
      "duration_ms": 56.1,
      "error": "Couldn't load 'no-such-model': no-such-model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'\nIf this is a private repository, make sure to pass a token having permission to this repo either by logging in with `hf auth login` or by passing `token=<y",
      "error_type": "DetectorUnavailable",
      "event": "rejected",
      "reason": "scoring_failed",
      "stage": "model_signal",
      "status": "rejected",
      "text_chars": 114,
      "timestamp": "2026-11-15T21:32:48+00:00"
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
      "content_id": "a7b6b0a2-e9cc-4c1c-8bbf-99d212eaf8ff",
      "creator_id": "t3_short_1",
      "duration_ms": 34.7,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:33:33+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "a6dfeea6-28bb-4a2d-a9ea-1f5f5497f67d",
      "creator_id": "t3_short_2",
      "duration_ms": 30.8,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:33:46+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "8b01c393-8c0d-4489-8b52-9370710c6b4e",
      "creator_id": "t3_short_3",
      "duration_ms": 42.0,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:33:59+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "de6f69fc-281d-4b15-92d3-9fa4f344cff7",
      "creator_id": "t3_short_4",
      "duration_ms": 45.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:34:12+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "a283bac4-a766-4f2e-a175-3b526424ba50",
      "creator_id": "t3_short_5",
      "duration_ms": 33.4,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:34:25+00:00"
    },
    {
      "combined_score": 0.5101,
      "content_id": "49f024f5-6bf2-468e-bbf2-f736bc32d0f1",
      "creator_id": "t3_long_1",
      "duration_ms": 151.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8926,
      "status": "decided",
      "style_score": 0.1275,
      "text_chars": 2142,
      "timestamp": "2026-11-15T21:34:38+00:00"
    },
    {
      "combined_score": 0.3997,
      "content_id": "411c0623-dcb8-4fed-9636-0474ec3e9e51",
      "creator_id": "t3_long_2",
      "duration_ms": 162.2,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.7726,
      "status": "decided",
      "style_score": 0.0269,
      "text_chars": 2510,
      "timestamp": "2026-11-15T21:34:51+00:00"
    },
    {
      "combined_score": 0.5894,
      "content_id": "9cec1a86-c9ca-404b-8331-5240a69253ea",
      "creator_id": "t3_long_3",
      "duration_ms": 160.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8231,
      "status": "decided",
      "style_score": 0.3556,
      "text_chars": 2418,
      "timestamp": "2026-11-15T21:35:05+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "3cb85837-512f-4c98-aac3-5d0e5dbd4c00",
      "creator_id": "t3_long_4",
      "duration_ms": 162.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.8074,
      "status": "decided",
      "style_score": 0.492,
      "text_chars": 2304,
      "timestamp": "2026-11-15T21:35:18+00:00"
    },
    {
      "combined_score": 0.3857,
      "content_id": "177556c7-d304-494d-ab60-b6d350bb0a4a",
      "creator_id": "t3_long_5",
      "duration_ms": 161.2,
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.6146,
      "status": "decided",
      "style_score": 0.1568,
      "text_chars": 5855,
      "timestamp": "2026-11-15T21:35:31+00:00"
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
      "timestamp": "2026-11-15T21:35:53+00:00"
    },
    {
      "creator_id": "t3_c4_missing",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "text_chars": null,
      "timestamp": "2026-11-15T21:35:53+00:00"
    },
    {
      "creator_id": "t3_c4_short",
      "duration_ms": 0.1,
      "event": "rejected",
      "reason": "text_too_short",
      "status": "rejected",
      "text_chars": 2,
      "timestamp": "2026-11-15T21:35:53+00:00"
    },
    {
      "creator_id": "t3_c4_long",
      "duration_ms": 0.0,
      "event": "rejected",
      "reason": "text_too_long",
      "status": "rejected",
      "text_chars": 20005,
      "timestamp": "2026-11-15T21:35:53+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "e7ab0154-9908-4e0f-9f94-f3255b5fa77a",
      "creator_id": "t3_c4",
      "duration_ms": 24.2,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:35:53+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "75739da9-1600-4cff-96c9-adee39633f6c",
      "creator_id": "t3_c4",
      "duration_ms": 25.3,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:35:54+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "706c84ba-90c4-4282-9426-54606ef1f40c",
      "creator_id": "t3_c4",
      "duration_ms": 31.9,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:35:54+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "78e95856-6ed0-40ef-8dc1-64f2995a1b0a",
      "creator_id": "t3_c4",
      "duration_ms": 26.1,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:35:54+00:00"
    },
    {
      "combined_score": 0.6,
      "content_id": "468394ba-60fd-4654-9b62-8acd47ad6861",
      "creator_id": "t3_c4",
      "duration_ms": 24.0,
      "guess": "unsure",
      "label": "We couldn't tell whether this was written by a person or by AI. This is not a finding against you. Our check is often unsure, especially on short or very formal writing.",
      "model_score": 0.4858,
      "status": "decided",
      "style_score": 0.7636,
      "text_chars": 114,
      "timestamp": "2026-11-15T21:35:54+00:00"
    },
    {
      "creator_id": "t3_c4",
      "event": "rejected",
      "limit": "5 per 1 minute",
      "reason": "rate_limited",
      "status": "rejected",
      "timestamp": "2026-11-15T21:35:54+00:00"
    }
  ]
}
(.venv) (base) evannashen@Evannas-MacBook-Air-3 ai201-project4-provenance-guard-starter-v2026 %
```
