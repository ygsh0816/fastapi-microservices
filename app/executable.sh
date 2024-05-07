#!/bin/sh

# Activate your virtual environment if you're using one
# source /path/to/your/venv/bin/activate

# Run your FAST API app using uvicorn
uvicorn app.main:fast_app --host 0.0.0.0 --port 8000