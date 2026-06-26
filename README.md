# QueueStorm Investigator

An AI/API SupportOps Challenge service built with FastAPI and Google Gemini.

## Tech Stack
- **Framework**: FastAPI, Uvicorn
- **Language**: Python 3.11+
- **AI/LLM**: Google Gemini (via `google-genai` SDK)
- **Validation**: Pydantic

## AI Approach
The application uses the `gemini-2.5-flash` model for fast and cost-effective text reasoning. The system prompt injects strict safety boundaries and taxonomy schemas into the LLM context. We use Gemini's `response_schema` structured JSON output to guarantee adherence to the exact response shape required by the API contract.

### Safety Guardrails
The safety rules (e.g., no OTP requests, no unauthorized refunds, no third-party contacts) are strictly enforced through explicit instructions in the `SYSTEM_PROMPT`. The prompt penalizes violations implicitly, and `gemini-2.5-flash` follows these negative constraints well.

## Setup & Run Locally
1. Clone this repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   Copy `.env.example` to `.env` and insert your Gemini API Key.
   ```
   GEMINI_API_KEY=your_key_here
   ```
5. Run the server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   The service will be available at `http://localhost:8000/`.

## Deploy (Docker)
1. Build the image:
   ```bash
   docker build -t queuestorm-investigator .
   ```
2. Run the image:
   ```bash
   docker run -p 8000:8000 -e GEMINI_API_KEY=your_key_here queuestorm-investigator
   ```

## Assumptions & Limitations
- Assumes the Gemini API responds within the 30-second per-request timeout.
- The `gemini-2.5-flash` model is lightweight and highly capable, but for exceptionally ambiguous fraud logic, `gemini-2.5-pro` may yield higher safety compliance.
