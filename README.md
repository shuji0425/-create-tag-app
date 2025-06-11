# Gemini Tag Generator

This project consists of a Next.js frontend and a FastAPI backend to generate image tags using the Gemini API.

## Structure

- `frontend/` – Next.js application written in TypeScript with TailwindCSS
- `backend/` – FastAPI server structured with domain, usecases, interfaces and infrastructure modules following Clean Architecture principles

## Setup

1. Copy `.env.example` in each directory to `.env` and adjust values.
2. Install dependencies for both parts.
3. TailwindCSS is already configured in the frontend; styles are in `src/styles/globals.css`.
4. Run `start.sh` to launch backend and frontend together.

## Requirements

- Node.js 18+
- Python 3.10+

The project is lightweight so it should run on machines with 8GB of RAM.
