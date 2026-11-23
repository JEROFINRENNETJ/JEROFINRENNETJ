# Study Progress Tracker

## Purpose

The Study Progress Tracker is a small Python application that records study time and compares the total with a weekly study goal. It is designed as a learning exercise in CLI arguments, file storage, and input validation.

## Technologies

- Python 3
- Standard-library `argparse`, `json`, and `pathlib` modules

## Running the project

No third-party packages are required.

```bash
python3 projects/study_progress_tracker.py --goal 10 --minutes 90
python3 projects/study_progress_tracker.py --goal 10
```

The first command adds 90 minutes to the saved weekly total and displays progress toward a 10-hour goal. The second command displays the saved progress without adding a session. Data is stored in `study_progress.json` in the repository directory.

## Sample output

```text
Added 90 minutes. Total: 1.5 hours / 10.0 hours (15.0%)
```

## Current status

Working and suitable for demonstration. Future improvements could include separate weekly periods and an export feature.

## My contribution

I planned, implemented, documented, and tested this project independently.
