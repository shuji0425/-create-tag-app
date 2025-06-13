# Gemini タグ生成器

このプロジェクトは、Gemini API を利用して画像タグを生成する Next.js フロントエンドと FastAPI バックエンドから構成されています。

## 構成

- `frontend/` – TailwindCSS を用いた TypeScript 製の Next.js アプリケーション
- `backend/` – Clean Architecture に基づきドメイン、ユースケース、インターフェース、インフラストラクチャに分割された FastAPI サーバ

## セットアップ

1. 各ディレクトリの `.env.example` を `.env` としてコピーし、値を設定します。
   - `backend/.env` には `GEMINI_API_KEY` を設定してください。
2. フロントエンドとバックエンドの依存関係をインストールします。
3. フロントエンドでは TailwindCSS が既に設定されており、スタイルは `src/styles/globals.css` にあります。
4. `start.sh` を実行するとバックエンドとフロントエンドを同時に起動できます。

## 必要条件

- Node.js 18 以上
- Python 3.10 以上

このプロジェクトは軽量のため、8GB の RAM があれば実行可能です。
