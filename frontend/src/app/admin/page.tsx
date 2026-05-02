"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

interface FoodItem {
  id: number;
  name: string;
  item_type: string;
}

interface IngredientInput {
  name: string;
  quantity: string;
}

export default function AdminDashboard() {
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  const [foods, setFoods] = useState<FoodItem[]>([]);
  const [selectedFood, setSelectedFood] = useState<FoodItem | null>(null);
  const [searchTerm, setSearchTerm] = useState("");

  // Form states
  const [recipeName, setRecipeName] = useState("");
  const [ingredients, setIngredients] = useState<IngredientInput[]>([{ name: "", quantity: "" }]);
  const [instructions, setInstructions] = useState<string[]>([""]);
  const [submitting, setSubmitting] = useState(false);
  const [toastMessage, setToastMessage] = useState<{ type: "success" | "error"; text: string } | null>(null);

  useEffect(() => {
    const token = localStorage.getItem("adminToken");
    if (!token) {
      router.push("/admin/login");
      return;
    }

    const fetchFoods = async () => {
      try {
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
        const res = await fetch(`${apiUrl}/api/admin/foods`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (res.status === 401) {
          localStorage.removeItem("adminToken");
          router.push("/admin/login");
          return;
        }
        if (!res.ok) throw new Error("Failed to fetch foods");
        const data = await res.json();
        setFoods(data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchFoods();
  }, [router]);

  // --- Ingredient Handlers ---
  const handleAddIngredient = () => setIngredients([...ingredients, { name: "", quantity: "" }]);
  const handleRemoveIngredient = (index: number) => {
    const newIngredients = [...ingredients];
    newIngredients.splice(index, 1);
    setIngredients(newIngredients.length ? newIngredients : [{ name: "", quantity: "" }]);
  };
  const handleIngredientChange = (index: number, field: "name" | "quantity", value: string) => {
    const newIngredients = [...ingredients];
    newIngredients[index][field] = value;
    setIngredients(newIngredients);
  };

  // --- Instruction Handlers ---
  const handleAddInstruction = () => setInstructions([...instructions, ""]);
  const handleRemoveInstruction = (index: number) => {
    const newInstructions = [...instructions];
    newInstructions.splice(index, 1);
    setInstructions(newInstructions.length ? newInstructions : [""]);
  };
  const handleInstructionChange = (index: number, value: string) => {
    const newInstructions = [...instructions];
    newInstructions[index] = value;
    setInstructions(newInstructions);
  };

  const showToast = (type: "success" | "error", text: string) => {
    setToastMessage({ type, text });
    setTimeout(() => setToastMessage(null), 3000);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedFood) return;

    // Validate and format ingredients
    const validIngredients = ingredients
      .filter(i => i.name.trim() !== "")
      .map(i => i.quantity.trim() ? `${i.quantity.trim()} ${i.name.trim()}` : i.name.trim());

    // Validate and format instructions
    const validInstructionsList = instructions.filter(i => i.trim() !== "");
    const formattedInstructions = validInstructionsList
      .map((step, idx) => `${idx + 1}. ${step.trim()}`)
      .join("\n");

    if (!recipeName.trim() || validIngredients.length === 0 || !formattedInstructions) {
      showToast("error", "Vui lòng điền đầy đủ thông tin (Tên món, Nguyên liệu, Cách làm).");
      return;
    }

    setSubmitting(true);
    try {
      const token = localStorage.getItem("adminToken");
      const payload = {
        food_item_id: selectedFood.id,
        recipe_name: recipeName,
        ingredients: validIngredients,
        instructions: formattedInstructions,
      };

      const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
      const res = await fetch(`${apiUrl}/api/admin/recipes`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(payload),
      });

      if (!res.ok) throw new Error("Thêm công thức thất bại");

      showToast("success", "Thêm công thức thành công!");
      // Reset form
      setRecipeName("");
      setIngredients([{ name: "", quantity: "" }]);
      setInstructions([""]);
    } catch (err: any) {
      showToast("error", err.message);
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return <div className="flex justify-center items-center h-full text-gray-500 text-lg">Đang tải dữ liệu hệ thống...</div>;
  }

  const filteredFoods = foods.filter((f) => f.name.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="flex h-full gap-8">
      {/* Toast Notification */}
      {toastMessage && (
        <div className={`fixed top-20 right-8 px-6 py-4 rounded-lg shadow-2xl z-50 text-white font-bold transition-all flex items-center gap-3 ${
          toastMessage.type === "success" ? "bg-emerald-500" : "bg-red-500"
        }`}>
          {toastMessage.type === "success" ? (
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" /></svg>
          ) : (
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          )}
          {toastMessage.text}
        </div>
      )}

      {/* Cột Trái (30%): Danh sách món ăn */}
      <div className="w-[30%] bg-white rounded-xl shadow-sm border border-gray-200 flex flex-col overflow-hidden">
        <div className="p-5 border-b border-gray-100 bg-gray-50/50">
          <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
            <svg className="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 10h16M4 14h16M4 18h16" /></svg>
            Chọn món ăn
          </h2>
          <div className="relative">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg className="h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clipRule="evenodd" />
              </svg>
            </div>
            <input
              type="text"
              placeholder="Tìm kiếm nguyên liệu / món..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent text-sm bg-gray-50 transition-all"
            />
          </div>
        </div>
        
        <div className="flex-1 overflow-y-auto p-3 space-y-1 bg-gray-50/30 custom-scrollbar">
          {filteredFoods.map((food) => (
            <div
              key={food.id}
              onClick={() => setSelectedFood(food)}
              className={`p-3.5 rounded-lg cursor-pointer transition-all flex justify-between items-center group ${
                selectedFood?.id === food.id
                  ? "bg-emerald-50 border border-emerald-200 shadow-sm"
                  : "hover:bg-white hover:shadow-sm border border-transparent"
              }`}
            >
              <div className="flex items-center gap-3">
                <div className={`w-2 h-2 rounded-full ${selectedFood?.id === food.id ? 'bg-emerald-500' : 'bg-gray-300 group-hover:bg-emerald-300'}`}></div>
                <span className={`font-medium ${selectedFood?.id === food.id ? 'text-emerald-800' : 'text-gray-700'}`}>{food.name}</span>
              </div>
              <span className={`text-xs px-2.5 py-1 rounded-full font-medium ${
                food.item_type === 'ingredient' ? 'bg-blue-50 text-blue-600' : 'bg-orange-50 text-orange-600'
              }`}>
                {food.item_type === 'ingredient' ? 'Nguyên liệu' : 'Món ăn'}
              </span>
            </div>
          ))}
          {filteredFoods.length === 0 && (
            <div className="text-center p-8 text-gray-400">
              <svg className="w-12 h-12 mx-auto mb-3 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
              Không tìm thấy kết quả.
            </div>
          )}
        </div>
      </div>

      {/* Cột Phải (70%): Form chi tiết */}
      <div className="w-[70%] bg-white rounded-xl shadow-sm border border-gray-200 flex flex-col overflow-hidden relative">
        {!selectedFood ? (
          <div className="flex flex-col justify-center items-center h-full text-gray-400 bg-gray-50/50">
            <svg className="w-20 h-20 mb-6 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M12 6v6m0 0v6m0-6h6m-6 0H6" /></svg>
            <p className="text-xl font-medium text-gray-500">Hãy chọn một món ăn từ danh sách để bắt đầu</p>
          </div>
        ) : (
          <div className="flex flex-col h-full">
            {/* Form Header */}
            <div className="px-8 py-6 border-b border-gray-100 bg-white sticky top-0 z-10 shadow-sm">
              <p className="text-sm font-medium text-emerald-600 mb-1 tracking-wider uppercase">THÊM CÔNG THỨC MỚI</p>
              <h2 className="text-3xl font-bold text-gray-800">
                {selectedFood.name}
              </h2>
            </div>

            {/* Form Content */}
            <div className="flex-1 overflow-y-auto p-8 custom-scrollbar bg-gray-50/30">
              <form id="recipe-form" onSubmit={handleSubmit} className="space-y-10 max-w-4xl">
                
                {/* 1. Tên công thức */}
                <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
                  <label className="flex items-center gap-2 text-base font-bold text-gray-800 mb-3">
                    <span className="flex items-center justify-center w-6 h-6 rounded-full bg-emerald-100 text-emerald-700 text-xs">1</span>
                    Tên món / Công thức
                  </label>
                  <input
                    type="text"
                    value={recipeName}
                    onChange={(e) => setRecipeName(e.target.value)}
                    className="w-full px-5 py-3 rounded-lg border border-gray-200 focus:ring-2 focus:ring-emerald-500 focus:border-transparent outline-none transition-all text-lg font-medium text-gray-800 placeholder-gray-300"
                    placeholder="VD: Cơm tấm sườn bì chả truyền thống"
                  />
                </div>

                {/* 2. Nguyên liệu */}
                <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
                  <label className="flex items-center justify-between text-base font-bold text-gray-800 mb-4">
                    <div className="flex items-center gap-2">
                      <span className="flex items-center justify-center w-6 h-6 rounded-full bg-emerald-100 text-emerald-700 text-xs">2</span>
                      Thành phần nguyên liệu
                    </div>
                  </label>
                  
                  <div className="space-y-3">
                    {ingredients.map((ing, index) => (
                      <div key={index} className="flex gap-3 items-start group">
                        <div className="w-[70%]">
                          <input
                            type="text"
                            value={ing.name}
                            onChange={(e) => handleIngredientChange(index, "name", e.target.value)}
                            className="w-full px-4 py-2.5 rounded-lg border border-gray-200 focus:ring-2 focus:ring-emerald-500 outline-none transition-all"
                            placeholder="Tên nguyên liệu (VD: Thịt ba chỉ)"
                          />
                        </div>
                        <div className="w-[30%]">
                          <input
                            type="text"
                            value={ing.quantity}
                            onChange={(e) => handleIngredientChange(index, "quantity", e.target.value)}
                            className="w-full px-4 py-2.5 rounded-lg border border-gray-200 focus:ring-2 focus:ring-emerald-500 outline-none transition-all"
                            placeholder="Định lượng (VD: 500g)"
                          />
                        </div>
                        <button
                          type="button"
                          onClick={() => handleRemoveIngredient(index)}
                          className="mt-1 p-2 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-lg transition-colors opacity-50 group-hover:opacity-100"
                          title="Xóa"
                        >
                          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                        </button>
                      </div>
                    ))}
                  </div>
                  <button
                    type="button"
                    onClick={handleAddIngredient}
                    className="mt-4 px-4 py-2.5 bg-emerald-50 text-emerald-700 font-medium rounded-lg hover:bg-emerald-100 transition-colors flex items-center gap-2"
                  >
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" /></svg>
                    Thêm nguyên liệu
                  </button>
                </div>

                {/* 3. Cách làm */}
                <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
                  <label className="flex items-center text-base font-bold text-gray-800 mb-4">
                    <span className="flex items-center justify-center w-6 h-6 rounded-full bg-emerald-100 text-emerald-700 text-xs mr-2">3</span>
                    Hướng dẫn thực hiện
                  </label>
                  
                  <div className="space-y-4">
                    {instructions.map((step, index) => (
                      <div key={index} className="flex gap-4 group">
                        <div className="flex-shrink-0 flex flex-col items-center mt-2">
                          <span className="w-8 h-8 flex items-center justify-center rounded-full bg-gray-100 text-gray-500 font-bold text-sm">
                            {index + 1}
                          </span>
                          {index < instructions.length - 1 && <div className="w-0.5 h-full bg-gray-100 mt-2"></div>}
                        </div>
                        <div className="flex-1 relative">
                          <textarea
                            value={step}
                            onChange={(e) => handleInstructionChange(index, e.target.value)}
                            rows={3}
                            className="w-full px-5 py-3 rounded-lg border border-gray-200 focus:ring-2 focus:ring-emerald-500 outline-none transition-all resize-none bg-gray-50 focus:bg-white"
                            placeholder={`Mô tả chi tiết bước ${index + 1}...`}
                          ></textarea>
                          <button
                            type="button"
                            onClick={() => handleRemoveInstruction(index)}
                            className="absolute top-2 right-2 p-1.5 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded transition-colors opacity-0 group-hover:opacity-100"
                            title="Xóa bước này"
                          >
                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>
                  
                  <button
                    type="button"
                    onClick={handleAddInstruction}
                    className="mt-5 ml-12 px-4 py-2.5 bg-blue-50 text-blue-700 font-medium rounded-lg hover:bg-blue-100 transition-colors flex items-center gap-2"
                  >
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" /></svg>
                    Thêm bước thực hiện
                  </button>
                </div>
              </form>
            </div>

            {/* Form Footer / Submit Button */}
            <div className="px-8 py-5 border-t border-gray-200 bg-white flex justify-end items-center sticky bottom-0 z-10 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]">
              <button
                type="submit"
                form="recipe-form"
                disabled={submitting}
                className={`px-8 py-3.5 rounded-lg font-bold text-white shadow-lg transition-all flex items-center gap-2 text-lg ${
                  submitting 
                    ? "bg-emerald-400 cursor-not-allowed" 
                    : "bg-emerald-600 hover:bg-emerald-700 hover:shadow-emerald-500/30 hover:-translate-y-0.5"
                }`}
              >
                {submitting ? (
                  <>
                    <svg className="animate-spin -ml-1 mr-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Đang lưu...
                  </>
                ) : (
                  <>
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" /></svg>
                    Lưu Công Thức
                  </>
                )}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
