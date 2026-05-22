"""
FastAPI server for the Gyroscopic Harmonizer.

Run:
    uvicorn api_server:app --reload --host 127.0.0.1 --port 8000
"""

from typing import Any, Dict, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

from gyroscopic_harmonizer import GyroscopicHarmonizer


app = FastAPI(
    title="Gyroscopic Ethical Harmonizer API",
    version="1.0.0",
    description="Local-first API for deterministic four-axis ethical verdicts.",
)

harmonizer = GyroscopicHarmonizer()


class DilemmaRequest(BaseModel):
    scenario: str = Field(..., min_length=1)
    actions: List[str] = Field(..., min_length=1)
    stakeholders: List[str] = Field(default_factory=list)
    severity: str = "MODERATE"
    time_pressure: float = Field(default=0.0, ge=0.0, le=1.0)
    context: Dict[str, Any] = Field(default_factory=dict)


class QuickCheckRequest(BaseModel):
    scenario: str = Field(..., min_length=1)
    action: str = Field(..., min_length=1)


class AxisReasoningRequest(BaseModel):
    scenario: str = Field(..., min_length=1)
    action: str = Field(..., min_length=1)


@app.get("/")
def root() -> Dict[str, Any]:
    return {
        "service": "Gyroscopic Ethical Harmonizer",
        "status": "running",
        "endpoints": [
            "GET /health",
            "POST /verdict",
            "POST /quick-check",
            "POST /axis-reasoning",
            "GET /stability-report",
        ],
    }


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/verdict")
def verdict(request: DilemmaRequest) -> Dict[str, Any]:
    return harmonizer.evaluate(
        scenario=request.scenario,
        actions=request.actions,
        stakeholders=request.stakeholders,
        severity=request.severity,
        time_pressure=request.time_pressure,
        context=request.context,
    )


@app.post("/quick-check")
def quick_check(request: QuickCheckRequest) -> Dict[str, str]:
    return {
        "action": request.action,
        "verdict": harmonizer.quick_check(request.scenario, request.action),
    }


@app.post("/axis-reasoning")
def axis_reasoning(request: AxisReasoningRequest) -> Dict[str, Any]:
    return {
        "action": request.action,
        "reasoning": harmonizer.get_axis_reasoning(request.scenario, request.action),
    }


@app.get("/stability-report")
def stability_report() -> Dict[str, Any]:
    return harmonizer.stability_report()
