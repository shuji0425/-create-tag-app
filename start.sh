#!/bin/bash
set -euo pipefail

# Activate python virtual environment
echo "Activating Python virtual environment..."
test -d backend/venv || python3 -m venv backend/venv
source backend/venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r backend/requirements.txt

# Install Node packages if node_modules doesn't exist
echo "Installing Node packages..."
if [ ! -d frontend/node_modules ]; then
  (cd frontend && npm install)
fi

# Run backend and frontend
echo "Starting backend..."
(cd backend && uvicorn app.main:app --reload) &
BACK_PID=$!

echo "Starting frontend..."
(cd frontend && npm run dev) &
FRONT_PID=$!

trap 'echo "Stopping..."; kill $BACK_PID $FRONT_PID' EXIT
wait
