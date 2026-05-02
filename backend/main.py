"""
main.py – FastAPI application for Food Tracker AI.

Endpoints
---------
POST /api/scan    – Upload food image → YOLO predict → DB lookup → save history
GET  /api/history – Fetch all scan records
GET  /api/export  – Download Excel of scan history
"""

import os
import uuid
import json
from datetime import datetime
from pathlib import Path

import pandas as pd
import base64
import cv2
import numpy as np
from fastapi import Depends, FastAPI, File, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from ai_engine import predict, predict_frame
from database import Base, FoodItem, Recipe, ScanHistory, engine, get_db
import admin

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(title="Food Tracker AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure uploads directory exists
UPLOAD_DIR = Path(__file__).resolve().parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

# Serve uploaded images as static files
app.mount("/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")

# Include Admin router
app.include_router(admin.router)


# ---------------------------------------------------------------------------
# Startup – create tables
# ---------------------------------------------------------------------------

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------------------------
# POST /api/scan
# ---------------------------------------------------------------------------

@app.post("/api/scan")
async def scan_food(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # 1. Save uploaded image
    ext = Path(file.filename or "image.jpg").suffix or ".jpg"
    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = UPLOAD_DIR / filename

    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    # 2. Run YOLO inference
    label, confidence = predict(str(file_path))

    # 3. Lookup food info by name
    food = db.query(FoodItem).filter(FoodItem.name == label).first()
    
    recipes_list = []
    item_type = "unknown"
    message = f"Phát hiện: {label}"
    
    if food:
        item_type = food.item_type
        if item_type == "dish":
            message = f"Bạn đang có {label}! Dưới đây là các cách nấu:"
        else:
            message = f"Bạn đang có {label}! Dưới đây là các món ngon bạn có thể làm:"
            
        for r in food.recipes:
            recipes_list.append({
                "recipe_name": r.recipe_name,
                "ingredients": json.loads(r.ingredients),
                "instructions": r.instructions
            })

    # 4. Save to scan history
    record = ScanHistory(
        food_name=label,
        confidence=confidence,
        image_path=f"/uploads/{filename}",
        created_at=datetime.utcnow(),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return JSONResponse(
        content={
            "id": record.id,
            "label": label,
            "confidence": confidence,
            "item_type": item_type,
            "message": message,
            "recipes": recipes_list,
            "image_url": f"/uploads/{filename}",
            "created_at": record.created_at.isoformat(),
        }
    )


# ---------------------------------------------------------------------------
# GET /api/history
# ---------------------------------------------------------------------------

@app.get("/api/history")
def get_history(db: Session = Depends(get_db)):
    records = db.query(ScanHistory).order_by(ScanHistory.created_at.desc()).all()
    return [
        {
            "id": r.id,
            "food_name": r.food_name,
            "confidence": r.confidence,
            "image_path": r.image_path,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in records
    ]


# ---------------------------------------------------------------------------
# GET /api/export
# ---------------------------------------------------------------------------

@app.get("/api/export")
def export_history(db: Session = Depends(get_db)):
    records = db.query(ScanHistory).order_by(ScanHistory.created_at.desc()).all()

    data = []
    for r in records:
        data.append({
            "ID": r.id,
            "Tên món/Nguyên liệu": r.food_name,
            "Độ tin cậy (%)": round(r.confidence * 100, 1),
            "Ảnh": r.image_path,
            "Thời gian": r.created_at.isoformat() if r.created_at else "",
        })

    df = pd.DataFrame(data)
    export_path = Path(__file__).resolve().parent / "scan_history.xlsx"
    df.to_excel(str(export_path), index=False, engine="openpyxl")

    return FileResponse(
        path=str(export_path),
        filename="scan_history.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


# ---------------------------------------------------------------------------
# WebSocket /api/ws/live (Giữ nguyên logic Bounding Box)
# ---------------------------------------------------------------------------

@app.websocket("/api/ws/live")
async def websocket_live_scan(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            try:
                img_bytes = base64.b64decode(data)
                np_arr = np.frombuffer(img_bytes, np.uint8)
                frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
                if frame is not None:
                    detections = predict_frame(frame)
                    await websocket.send_json({"boxes": detections})
                else:
                    await websocket.send_json({"error": "Could not decode frame"})
            except Exception as e:
                print(f"Error processing frame: {e}")
    except WebSocketDisconnect:
        print("WebSocket client disconnected")
