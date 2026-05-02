"""
seed.py – Pre-fill the FoodInfo table with 68 food items for the new YOLOv8 dataset.

Usage:
    python seed.py
"""

import sys
import io
from database import Base, SessionLocal, engine, FoodInfo

# Ensure terminal can handle UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except Exception:
        pass

# List of 68 items provided by the user
RAW_CLASSES = [
    "Salad", "Hamburger", "Banh_canh", "Banh_chung", "Banh_cuon", "Banh_khot", "Banh_mi", 
    "Banh_trang", "Banh_trang_tron", "Banh_xeo", "Bo_kho", "Bo_la_lot", "Bong_cai", "Bun", 
    "Bun_bo_Hue", "Bun_cha", "Bun_dau", "Bun_mam", "Bun_rieu", "Ca", "Ca_chua", "Ca_phao", 
    "Ca_rot", "Canh", "Cha", "Cha_gio", "Chanh", "Com", "Com_tam", "Con_nguoi", "Cu_kieu", 
    "Cua", "Dau_hu", "Dua_chua", "Dua_leo", "Goi_cuon", "Heo_quay", "Hu_tieu", "Kho_qua_thit", 
    "Khoai_tay_chien", "Lau", "Long_heo", "Mi", "Muc", "Nam", "Oc", "Ot_chuong", "Pho", 
    "Pho_mai", "Rau", "Thit_bo", "Thit_ga", "Thit_heo", "Thit_kho", "Thit_nuong", "Tom", 
    "Trung", "Xoi", "ya_banh_beo", "yb_cao_lau", "yc_mi_Quang", "yd_com_chien_duong_chau", 
    "ye_bun_cha_ca", "yf_com_chien_ga", "yg_chao_long", "yh_nom_hoa_chuoi", "yi_nui_xao_bo", 
    "yj_sup_cua"
]

def get_mock_data(item_name):
    """Generate somewhat realistic mock data based on item name."""
    name_lower = item_name.lower()
    
    # Default values
    data = {
        "name": item_name,
        "slug": item_name.lower().replace(" ", "_").replace("-", "_"),
        "calories": 200,
        "protein": 10.0,
        "carbs": 20.0,
        "fat": 8.0,
        "description": f"Thông tin chi tiết về {item_name}.",
        "ingredients": "Đang cập nhật..."
    }

    # Categorization for more "realistic" data
    if any(x in name_lower for x in ["rau", "cai", "chua", "rot", "leo", "nam", "chuong", "salad", "chanh", "phao", "kieu", "dua"]):
        data.update({"calories": 50, "protein": 2.0, "carbs": 10.0, "fat": 0.5})
    elif any(x in name_lower for x in ["thit", "ca", "tom", "cua", "muc", "oc", "heo", "ga", "bo", "trung", "cha", "long"]):
        if "com" not in name_lower and "bun" not in name_lower and "pho" not in name_lower:
            data.update({"calories": 250, "protein": 25.0, "carbs": 2.0, "fat": 15.0})
    elif any(x in name_lower for x in ["com", "bun", "mi", "pho", "xoi", "banh", "nui", "hieu", "lau", "chau"]):
        data.update({"calories": 450, "protein": 15.0, "carbs": 65.0, "fat": 12.0})
    elif "hamburger" in name_lower:
        data.update({"calories": 550, "protein": 25.0, "carbs": 45.0, "fat": 30.0})
    elif "khoai_tay_chien" in name_lower:
        data.update({"calories": 320, "protein": 3.5, "carbs": 40.0, "fat": 17.0})
    elif "pho_mai" in name_lower:
        data.update({"calories": 400, "protein": 25.0, "carbs": 1.5, "fat": 33.0})
    elif "con_nguoi" in name_lower:
        data.update({"calories": 0, "protein": 0.0, "carbs": 0.0, "fat": 0.0, "description": "Đối tượng là con người, không phải món ăn."})
    
    return data

def seed():
    print("[!] Recreating FoodInfo table...")
    FoodInfo.__table__.drop(engine, checkfirst=True)
    FoodInfo.__table__.create(engine)

    db = SessionLocal()
    try:
        for item in RAW_CLASSES:
            dish_data = get_mock_data(item)
            db.add(FoodInfo(**dish_data))
            # print(f"  [+] Added {item}") # Avoid too much output

        db.commit()
        print(f"\n[✓] Seeding complete! Total items: {len(RAW_CLASSES)}")
    except Exception as e:
        db.rollback()
        print(f"[X] Error during seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
