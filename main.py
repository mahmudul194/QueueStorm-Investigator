from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from dotenv import load_dotenv
import logging

load_dotenv()

from schemas import TicketRequest
from ai_service import analyze_ticket_with_ai

app = FastAPI(title="QueueStorm Investigator API")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/analyze-ticket")
async def analyze_ticket(ticket: TicketRequest):
    try:
        response = analyze_ticket_with_ai(ticket)
        return response
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        return JSONResponse(status_code=422, content={"detail": "Invalid schema for response", "errors": e.errors()})
    except Exception as e:
        logger.error(f"Internal error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during analysis")

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Malformed input or missing required fields."},
    )
