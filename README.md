# Smart Companion – Micro-Win Task Assistant

## Problem Statement
This project addresses **Problem Statement 1 – The Smart Companion**, designed to help neurodivergent users overcome executive function challenges by breaking overwhelming tasks into small, achievable micro-steps.

## Features
- Task decomposition into non-intimidating micro-wins
- Privacy-first local storage using SQLite
- Fast response (<5 seconds)
- Minimal cognitive load design

## Tech Stack
- Backend: FastAPI (Python)
- Database: SQLite (Local-first)
- Deployment: Docker

## How to Run (Docker)

```bash
docker build -t smart-companion .
docker run -p 8000:8000 smart-companion
