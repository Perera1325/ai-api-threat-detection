from fastapi import FastAPI, Request

# security modules
from gateway.request_filter import analyze_request
from gateway.auth import validate_api_key, validate_jwt

# monitoring modules
from gateway.metrics import get_metrics
from gateway.threat_engine import calculate_threat_level

# routing engine
from gateway.router import route_request


app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI API Threat Detection Gateway Running"}


@app.post("/api")
async def api_gateway(request: Request):

    headers = request.headers

    api_key = headers.get("x-api-key")
    token = headers.get("authorization")

    # API KEY VALIDATION
    if not validate_api_key(api_key):
        return {"status": "invalid api key"}

    # JWT VALIDATION
    if token:
        token = token.replace("Bearer ", "")

        payload = validate_jwt(token)

        if not payload:
            return {"status": "invalid token"}

    # READ REQUEST BODY
    data = await request.json()

    # AI SECURITY ANALYSIS
    decision = analyze_request(data)

    if decision == "block":
        return {"status": "blocked"}

    # ROUTE REQUEST TO BACKEND SERVICE
    backend_response = route_request(data)

    return {
        "status": "allowed",
        "backend_response": backend_response
    }


@app.get("/metrics")
def metrics():
    return get_metrics()


@app.get("/threat-level")
def threat_level():

    metrics = get_metrics()

    level = calculate_threat_level(metrics)

    return {
        "threat_level": level,
        "metrics": metrics
    }