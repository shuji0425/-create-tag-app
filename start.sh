#!/bin/bash

# Python 仮想環境を有効化
test -d backend/venv || python3 -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt >/dev/null 2>&1

# node_modules がない場合は Node パッケージをインストール
if [ ! -d frontend/node_modules ]; then
  cd frontend && npm install >/dev/null 2>&1 && cd ..
fi

# バックエンドとフロントエンドを起動
cd backend && uvicorn app.main:app --reload &
BACK_PID=$!
cd ../frontend && npm run dev &
FRONT_PID=$!

trap "kill $BACK_PID $FRONT_PID" EXIT
wait
