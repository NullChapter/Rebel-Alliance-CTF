# Insecure-Design

## Storyline
Design Flaw:

Amidst the cosmic expanse, the Null InfoSec Chapter stands firm against cyber threats. Now, a Design Flaw looms – a vulnerability endangering our systems. The chapter seeks your assistance to strengthen defenses. Join forces to scrutinize, identify weaknesses, and implement remedies. Together, let's fortify our digital realm.

Data Injection:

Within the boundless digital cosmos, the Null InfoSec Chapter remains vigilant against cyber perils. Yet, the menace of Data Injection casts a dark shadow – a subtle vulnerability threatening our systems. The chapter implores your aid to combat this threat. Collaborate to analyze, detect weaknesses, and bolster defenses. Together, let's secure our digital frontiers.


## Flag

NULL{G37H4iP3r}

## Setup

### Manual

- Set environment variable `'FLAG_INTERMEDIATE'` to `'NEBYFEEN'` or any other 8 byte long string.
- Run the following commands with cwd as `2.Insecure-Design/` (`cd ./Insecure-Design/)
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  uvicorn src.main:app --host 0.0.0.0 --port 2916
  ```
- The port for the app wil be exposed at http://localhost:2916
