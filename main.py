from gateway.threat_engine import calculate_threat_level
from gateway.metrics import get_metrics
from fastapi import FastAPI, Request
from gateway.request_filter import analyze_request

app = FastAPI()

@app.get("/")
def home():
    return {"message":"AI API Threat Detection Gateway Running"}

@app.post("/api")
async def api_gateway(request: Request):

    data = await request.json()

    decision = analyze_request(data)

    if decision == "block":
        return {"status":"blocked"}

    return {"status":"allowed"}

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