import json
import time
from pathlib import Path

PIPE_DIR = Path("pipe")
REQ = PIPE_DIR / "format_request.txt"
RES = PIPE_DIR / "format_response.txt"

POLL_SECONDS = 0.1


def format_entry(entry):
    # Formats entry fields for consistency

    formatted = {}

    if "date" in entry:
        parts = entry["date"].split("/")
        if len(parts) == 3:
            month, day, year = parts
            formatted["date"] = f"20{year}-{month.zfill(2)}-{day.zfill(2)}"

    if "title" in entry:
        formatted["title"] = entry["title"].lower()

    if "category" in entry:
        formatted["category"] = entry["category"].lower()

    if "notes" in entry:
        formatted["notes"] = entry["notes"]

    return formatted


def process_request(req):

    if req.get("action") != "format":
        return {"ok": False, "error": "invalid_action"}

    entry = req.get("entry")

    if not entry:
        return {"ok": False, "error": "missing_entry"}

    formatted = format_entry(entry)

    return {
        "ok": True,
        "formatted_entry": formatted
    }


def main():

    PIPE_DIR.mkdir(exist_ok=True)
    REQ.touch(exist_ok=True)
    RES.touch(exist_ok=True)

    print("Entry Formatter Microservice running...")
    print("Request file:", REQ)
    print("Response file:", RES)

    while True:

        try:
            raw = REQ.read_text().strip()

            if raw:
                req = json.loads(raw)

                response = process_request(req)

                RES.write_text(json.dumps(response))

                # clear request after processing
                REQ.write_text("")

        except Exception as e:

            RES.write_text(json.dumps({
                "ok": False,
                "error": str(e)
            }))

        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
