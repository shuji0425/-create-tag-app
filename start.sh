#!/bin/bash

# Activate python virtual environment
test -d backend/venv || python3 -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt >/dev/null 2>&1

# Install Node packages if node_modules doesn't exist
if [ ! -d frontend/node_modules ]; then
  cd frontend && npm install >/dev/null 2>&1 && cd ..
fi

# Run backend and frontend
cd backend && uvicorn app.main:app --reload &
BACK_PID=$!
cd ../frontend && npm run dev &
FRONT_PID=$!

trap "kill $BACK_PID $FRONT_PID" EXIT
wait
