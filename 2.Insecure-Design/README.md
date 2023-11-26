# Insecure-Design

## Storyline

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
