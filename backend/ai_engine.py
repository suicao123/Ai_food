"""
AI Engine – YOLOv8 inference wrapper.
"""

import os
from pathlib import Path

import numpy as np
from ultralytics import YOLO

WEIGHTS_PATH = Path(__file__).resolve().parent / "models" / "best.pt"

# TỪ ĐIỂN DỊCH TÊN MODEL (KHÔNG DẤU) SANG TIẾNG VIỆT CHUẨN MỸ MÃN
VI_LABEL_MAP = {
    'Banh_canh': 'Bánh canh', 'Banh_chung': 'Bánh chưng', 'Banh_cuon': 'Bánh cuốn', 
    'Banh_khot': 'Bánh khọt', 'Banh_mi': 'Bánh mì', 'Banh_trang': 'Bánh tráng', 
    'Banh_trang_tron': 'Bánh tráng trộn', 'Banh_xeo': 'Bánh xèo', 'Bo_kho': 'Bò kho', 
    'Bo_la_lot': 'Bò lá lốt', 'Bong_cai': 'Bông cải', 'Bun': 'Bún', 'Bun_bo_Hue': 'Bún bò Huế', 
    'Bun_cha': 'Bún chả', 'Bun_dau': 'Bún đậu', 'Bun_mam': 'Bún mắm', 'Bun_rieu': 'Bún riêu', 
    'Ca': 'Cá', 'Ca_chua': 'Cà chua', 'Ca_phao': 'Cà pháo', 'Ca_rot': 'Cà rốt', 
    'Canh': 'Canh', 'Cha': 'Chả', 'Cha_gio': 'Chả giò', 'Chanh': 'Chanh', 'Com': 'Cơm', 
    'Com_tam': 'Cơm tấm', 'Con_nguoi': 'Con người', 'Cu_kieu': 'Củ kiệu', 'Cua': 'Cua', 
    'Dau_hu': 'Đậu hũ', 'Dua_chua': 'Dưa chua', 'Dua_leo': 'Dưa leo', 'Goi_cuon': 'Gỏi cuốn', 
    'Hamburger': 'Hamburger', 'Heo_quay': 'Heo quay', 'Hu_tieu': 'Hủ tiếu', 
    'Kho_qua_thit': 'Khổ qua dồn thịt', 'Khoai_tay_chien': 'Khoai tây chiên', 'Lau': 'Lẩu', 
    'Long_heo': 'Lòng heo', 'Mi': 'Mì', 'Muc': 'Mực', 'Nam': 'Nấm', 'Oc': 'Ốc', 
    'Ot_chuong': 'Ớt chuông', 'Pho': 'Phở', 'Pho_mai': 'Phô mai', 'Rau': 'Rau', 
    'Salad': 'Salad', 'Thit_bo': 'Thịt bò', 'Thit_ga': 'Thịt gà', 'Thit_heo': 'Thịt heo', 
    'Thit_kho': 'Thịt kho', 'Thit_nuong': 'Thịt nướng', 'Tom': 'Tôm', 'Trung': 'Trứng', 
    'Xoi': 'Xôi', 'cam': 'Cam'
}

_model: YOLO | None = None

def _get_model() -> YOLO:
    global _model
    if _model is None:
        if not WEIGHTS_PATH.exists():
            raise FileNotFoundError(
                f"YOLO weights not found at {WEIGHTS_PATH}. "
                "Run `python setup_model.py` first."
            )
        _model = YOLO(str(WEIGHTS_PATH))
    return _model

def predict(image_path: str) -> tuple[str, float]:
    model = _get_model()
    results = model(image_path)
    result = results[0]

    if result.boxes is None or len(result.boxes) == 0:
        return ("unknown", 0.0)

    confidences = result.boxes.conf.cpu().tolist()
    class_ids = result.boxes.cls.cpu().tolist()

    best_idx = int(max(range(len(confidences)), key=lambda i: confidences[i]))
    best_conf = float(confidences[best_idx])
    best_cls_id = int(class_ids[best_idx])

    # 1. Lấy tên gốc từ model (VD: 'Banh_mi')
    raw_label = result.names.get(best_cls_id, "unknown")
    
    # 2. Dịch sang tiếng Việt có dấu (VD: 'Bánh mì'). Nếu không có trong từ điển thì giữ nguyên.
    vi_label = VI_LABEL_MAP.get(raw_label, raw_label)

    return (vi_label, round(best_conf, 4))

def predict_frame(frame: np.ndarray) -> list[dict]:
    model = _get_model()
    results = model(frame, verbose=False) 
    
    result = results[0]
    detections = []
    
    if result.boxes is None or len(result.boxes) == 0:
        return detections

    boxes = result.boxes.xywh.cpu().numpy() 
    confidences = result.boxes.conf.cpu().numpy()
    class_ids = result.boxes.cls.cpu().numpy()

    for i in range(len(boxes)):
        x_c, y_c, w, h = boxes[i]
        
        x = x_c - (w / 2)
        y = y_c - (h / 2)
        
        confidence = float(confidences[i])
        cls_id = int(class_ids[i])
        
        # 1. Lấy tên gốc từ model
        raw_label = result.names.get(cls_id, "unknown")
        
        # 2. Dịch sang tiếng Việt có dấu
        vi_label = VI_LABEL_MAP.get(raw_label, raw_label)

        detections.append({
            "x": float(x),
            "y": float(y),
            "w": float(w),
            "h": float(h),
            "label": vi_label,
            "confidence": round(confidence, 4)
        })

    return detections