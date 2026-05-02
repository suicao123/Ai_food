import json
from database import Base, SessionLocal, engine, FoodItem, Recipe
from recipe_data import REAL_RECIPE_DATA

# Danh sách 68 class từ ai_engine.py (trừ "Con người")
RAW_CLASSES = [
    'Bánh canh', 'Bánh chưng', 'Bánh cuốn', 'Bánh khọt', 'Bánh mì', 'Bánh tráng',
    'Bánh tráng trộn', 'Bánh xèo', 'Bò kho', 'Bò lá lốt', 'Bông cải', 'Bún', 'Bún bò Huế',
    'Bún chả', 'Bún đậu', 'Bún mắm', 'Bún riêu', 'Cá', 'Cà chua', 'Cà pháo', 'Cà rốt',
    'Canh', 'Chả', 'Chả giò', 'Chanh', 'Cơm', 'Cơm tấm', 'Củ kiệu', 'Cua',
    'Đậu hũ', 'Dưa chua', 'Dưa leo', 'Gỏi cuốn', 'Hamburger', 'Heo quay', 'Hủ tiếu',
    'Khổ qua dồn thịt', 'Khoai tây chiên', 'Lẩu', 'Lòng heo', 'Mì', 'Mực', 'Nấm', 'Ốc',
    'Ớt chuông', 'Phở', 'Phô mai', 'Rau', 'Salad', 'Thịt bò', 'Thịt gà', 'Thịt heo',
    'Thịt kho', 'Thịt nướng', 'Tôm', 'Trứng', 'Xôi', 'Cam'
]

# Phân loại nguyên liệu (còn lại là món ăn)
INGREDIENTS = {
    'Bông cải', 'Cá', 'Cà chua', 'Cà pháo', 'Cà rốt', 'Chanh', 'Củ kiệu', 'Cua',
    'Đậu hũ', 'Dưa chua', 'Dưa leo', 'Mực', 'Nấm', 'Ốc', 'Ớt chuông', 'Phô mai',
    'Rau', 'Thịt bò', 'Thịt gà', 'Thịt heo', 'Tôm', 'Trứng', 'Cam'
}


def seed():
    print("=" * 60)
    print("  FOOD TRACKER AI - DATABASE SEEDER")
    print("=" * 60)

    print("\n[!] Re-initializing database (drop & create all tables)...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    total_items = 0
    total_recipes = 0
    items_with_real_data = 0
    items_with_fallback = 0

    try:
        for name in RAW_CLASSES:
            if name == "Con người":
                continue

            # Xác định item_type
            if name in REAL_RECIPE_DATA:
                item_type = REAL_RECIPE_DATA[name]["item_type"]
            else:
                item_type = "ingredient" if name in INGREDIENTS else "dish"

            # Tạo FoodItem
            food_item = FoodItem(name=name, item_type=item_type)
            db.add(food_item)
            db.flush()  # Lấy food_item.id
            total_items += 1

            # Nếu có dữ liệu thật trong REAL_RECIPE_DATA → dùng nó
            if name in REAL_RECIPE_DATA:
                recipes_data = REAL_RECIPE_DATA[name]["recipes"]
                items_with_real_data += 1
                for r in recipes_data:
                    recipe = Recipe(
                        food_item_id=food_item.id,
                        recipe_name=r["recipe_name"],
                        ingredients=json.dumps(r["ingredients"], ensure_ascii=False),
                        instructions=r["instructions"]
                    )
                    db.add(recipe)
                    total_recipes += 1
                print(f"  [OK] {name} ({item_type}) - {len(recipes_data)} cong thuc that")
            else:
                # Fallback: tạo 1 recipe placeholder cho các class chưa có data thật
                items_with_fallback += 1
                fallback_recipe = Recipe(
                    food_item_id=food_item.id,
                    recipe_name=f"Cách chế biến {name} cơ bản",
                    ingredients=json.dumps(
                        [name, "Gia vị cơ bản", "Hành tỏi"],
                        ensure_ascii=False
                    ),
                    instructions=(
                        f"1. Sơ chế {name} sạch sẽ.\n"
                        f"2. Chế biến {name} theo khẩu vị.\n"
                        f"3. Trình bày và thưởng thức."
                    )
                )
                db.add(fallback_recipe)
                total_recipes += 1
                print(f"  [--] {name} ({item_type}) - 1 cong thuc fallback")

        db.commit()

        print("\n" + "=" * 60)
        print("  KẾT QUẢ SEED")
        print("=" * 60)
        print(f"  Total FoodItem:          {total_items}")
        print(f"  Total Recipe:            {total_recipes}")
        print(f"  Items with real data:    {items_with_real_data}")
        print(f"  Items with fallback:     {items_with_fallback}")
        print("=" * 60)
        print("  DONE! Database seeded successfully!")
        print("=" * 60)

    except Exception as e:
        db.rollback()
        print(f"\n[ERROR]: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    seed()
