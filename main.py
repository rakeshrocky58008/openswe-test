from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional

from calculator import add, subtract, multiply, divide

app = FastAPI(title="OpenSWE Bot Tester", description="FastAPI UI for testing the OpenSWE bot")

templates = Jinja2Templates(directory="templates")


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str  # add | subtract | multiply | divide


class CalculationResponse(BaseModel):
    result: Optional[float] = None
    error: Optional[str] = None


class BotMessage(BaseModel):
    message: str


class BotResponse(BaseModel):
    reply: str


# ---------------------------------------------------------------------------
# UI route
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Serve the main UI page."""
    return templates.TemplateResponse("index.html", {"request": request})


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@app.get("/api/health")
async def health():
    """Simple health-check endpoint."""
    return {"status": "ok", "service": "openswe-bot-tester"}


# ---------------------------------------------------------------------------
# Calculator API
# ---------------------------------------------------------------------------

@app.post("/api/calculate", response_model=CalculationResponse)
async def calculate(req: CalculationRequest):
    """Perform a basic arithmetic calculation."""
    ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    fn = ops.get(req.operation)
    if fn is None:
        return CalculationResponse(error=f"Unknown operation '{req.operation}'. Choose from: add, subtract, multiply, divide.")
    try:
        result = fn(req.a, req.b)
        return CalculationResponse(result=result)
    except ValueError as exc:
        return CalculationResponse(error=str(exc))


# ---------------------------------------------------------------------------
# OpenSWE bot test endpoint
# ---------------------------------------------------------------------------

@app.post("/api/bot/send", response_model=BotResponse)
async def bot_send(msg: BotMessage):
    """
    Echo-style endpoint for testing the OpenSWE bot interaction.

    In a real integration you would forward the message to the OpenSWE bot
    API here. For now it returns a structured echo reply so the UI can be
    validated end-to-end without external credentials.
    """
    text = msg.message.strip()
    if not text:
        return BotResponse(reply="Please enter a message.")
    return BotResponse(reply=f"[OpenSWE Bot echo] You said: {text}")
