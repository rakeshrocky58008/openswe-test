# openswe-test

A FastAPI project with a basic UI for testing the OpenSWE bot.

## Features

- **Bot Chat UI** – send messages to the OpenSWE bot and view replies
- **Calculator API** – basic arithmetic (add, subtract, multiply, divide) and power functions (square, cube) exposed as REST endpoints
- **Interactive UI** served by FastAPI + Jinja2 at `http://localhost:8000`

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Main UI |
| GET | `/api/health` | Health check |
| POST | `/api/bot/send` | Send a message to the bot |
| POST | `/api/calculate` | Perform arithmetic |

Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Running Tests

```bash
pytest test_calculator.py
```

