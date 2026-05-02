"use client";

import { useCallback, useRef, useState } from "react";
import Image from "next/image";
import { FoodResult, scanFood, RecipeInfo } from "@/lib/api";

function RecipeAccordion({ recipe }: { recipe: RecipeInfo }) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="recipe-card">
      <div className="recipe-header" onClick={() => setIsOpen(!isOpen)}>
        <span className="font-semibold text-slate-200">{recipe.recipe_name}</span>
        <span className={`transition-transform duration-300 ${isOpen ? "rotate-180" : ""}`}>
          ▼
        </span>
      </div>
      {isOpen && (
        <div className="recipe-content animate-fade-in">
          <div className="mb-4">
            <h4 className="text-[10px] uppercase tracking-wider text-slate-500 font-bold mb-2">Nguyên liệu</h4>
            <div className="flex flex-wrap">
              {recipe.ingredients.map((ing, i) => (
                <span key={i} className="ingredient-badge">{ing}</span>
              ))}
            </div>
          </div>
          <div>
            <h4 className="text-[10px] uppercase tracking-wider text-slate-500 font-bold mb-2">Cách thực hiện</h4>
            <div className="space-y-3">
              {recipe.instructions.split("\n").map((step, i) => (
                <div key={i} className="instruction-step">
                  <div className="step-number">{i + 1}</div>
                  <p>{step.replace(/^\d+\.\s*/, "").replace(/^Bước\s\d+:\s*/, "")}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default function HomePage() {
  const [dragging, setDragging] = useState(false);
  const [loading, setLoading] = useState(false);
  const [preview, setPreview] = useState<string | null>(null);
  const [result, setResult] = useState<FoodResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleFile = useCallback(async (file: File) => {
    setPreview(URL.createObjectURL(file));
    setResult(null);
    setError(null);
    setLoading(true);
    try {
      const data = await scanFood(file);
      setResult(data);
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : "Có lỗi xảy ra.";
      setError(msg);
    } finally {
      setLoading(false);
    }
  }, []);

  const onDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setDragging(false);
    const file = e.dataTransfer.files[0];
    if (file) handleFile(file);
  }, [handleFile]);

  const onSelect = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) handleFile(file);
  }, [handleFile]);

  const confPct = result ? Math.round(result.confidence * 100) : 0;

  return (
    <div className="space-y-8 animate-fade-in">
      <div className="text-center space-y-2">
        <h1 className="text-3xl md:text-4xl font-extrabold gradient-text">
          Trợ Lý Ẩm Thực AI
        </h1>
        <p className="text-slate-400 text-sm">
          Nhận diện món ăn & gợi ý công thức nấu nướng thông minh
        </p>
      </div>

      <div
        className={`upload-zone flex flex-col items-center justify-center gap-4 py-16 px-6 text-center ${dragging ? "dragging" : ""}`}
        onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
        onDragLeave={() => setDragging(false)}
        onDrop={onDrop}
        onClick={() => inputRef.current?.click()}
      >
        <div className="text-5xl select-none">📸</div>
        <p className="text-slate-300 font-medium">
          Chụp hoặc kéo thả ảnh vào đây
        </p>
        <input ref={inputRef} type="file" accept="image/*" className="hidden" onChange={onSelect} />
      </div>

      {loading && (
        <div className="flex flex-col items-center gap-3 animate-fade-in">
          <div className="spinner" />
          <p className="text-sm text-slate-400">AI đang phân tích món ăn…</p>
        </div>
      )}

      {error && (
        <div className="glass-card p-4 text-center text-red-400 animate-fade-in">
          ⚠️ {error}
        </div>
      )}

      {result && !loading && (
        <div className="glass-card p-6 md:p-8 space-y-8 animate-fade-in">
          <div className="flex flex-col md:flex-row gap-8">
            {preview && (
              <div className="relative w-full md:w-72 h-72 rounded-2xl overflow-hidden flex-shrink-0 border border-white/10 shadow-2xl">
                <Image src={preview} alt="Food" fill className="object-cover" />
                <div className="absolute top-3 left-3 px-3 py-1 rounded-full bg-black/60 backdrop-blur-md border border-white/10 text-[10px] font-bold text-white uppercase tracking-widest">
                  {result.item_type === "dish" ? "🍲 Món ăn" : "🥦 Nguyên liệu"}
                </div>
              </div>
            )}

            <div className="flex-1 space-y-6">
              <div>
                <h2 className="text-3xl font-bold text-white mb-2">{result.label}</h2>
                <div className="flex items-center gap-3">
                   <div className="flex-1 h-1.5 rounded-full bg-white/5 overflow-hidden">
                      <div className="h-full bg-gradient-to-r from-indigo-500 to-emerald-500" style={{ width: `${confPct}%` }} />
                   </div>
                   <span className="text-xs font-bold text-indigo-400">{confPct}% tin cậy</span>
                </div>
              </div>

              <p className="text-indigo-200 font-medium italic text-lg border-l-4 border-indigo-500 pl-4 py-1 bg-indigo-500/5">
                &quot;{result.message}&quot;
              </p>

              <div className="space-y-4">
                <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest flex items-center gap-2">
                  <span>🍽️</span> Danh sách công thức
                </h3>
                
                {result.recipes.length > 0 ? (
                  <div className="space-y-1">
                    {result.recipes.map((recipe, idx) => (
                      <RecipeAccordion key={idx} recipe={recipe} />
                    ))}
                  </div>
                ) : (
                  <div className="p-6 rounded-xl bg-white/5 border border-dashed border-white/10 text-center">
                    <p className="text-slate-500 text-sm italic">
                      Hệ thống đang cập nhật công thức cho nguyên liệu/món ăn này.
                    </p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
