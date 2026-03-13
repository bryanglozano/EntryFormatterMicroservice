import json
import time
from pathlib import Path

PIPE_DIR = Path("pipe")
REQ = PIPE_DIR / "format_request.txt"
RES = PIPE_DIR / "format_response.txt"

POLL_SECONDS = 0.1


def send(req):
    REQ.write_text(json.dumps(req))


def wait_for_response(timeout=5):

    start = time.time()

    while time.time() - start < timeout:

        raw = RES.read_text().strip()

        if raw:
            return json.loads(raw)

        time.sleep(POLL_SECONDS)

    raise TimeoutError("Timed out waiting for response")


def clear():
    RES.write_text("")


def main():

    PIPE_DIR.mkdir(exist_ok=True)
    REQ.touch(exist_ok=True)
    RES.touch(exist_ok=True)

    clear()

    send({
        "action": "format",
        "entry": {
            "date": "3/11/26",
            "title": "Morning Run",
            "category": "Fitness",
            "notes": "Ran 30 minutes"
        }
    })

    print("FORMAT ->", wait_for_response())


if __name__ == "__main__":
    main()
