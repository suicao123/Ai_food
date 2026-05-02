import axios from "axios";

const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
});

export interface RecipeInfo {
    recipe_name: string;
    ingredients: string[];
    instructions: string;
}

export interface FoodResult {
    id: number;
    label: string;
    confidence: number;
    item_type: string;
    message: string;
    recipes: RecipeInfo[];
    image_url: string;
    created_at: string;
}

export interface HistoryRecord {
    id: number;
    food_name: string;
    confidence: number;
    image_path: string;
    created_at: string | null;
}

export async function scanFood(file: File): Promise<FoodResult> {
    const formData = new FormData();
    formData.append("file", file);
    const res = await api.post<FoodResult>("/api/scan", formData, {
        headers: { "Content-Type": "multipart/form-data" },
    });
    return res.data;
}

export async function getHistory(): Promise<HistoryRecord[]> {
    const res = await api.get<HistoryRecord[]>("/api/history");
    return res.data;
}

export async function exportExcel(): Promise<void> {
    const res = await api.get("/api/export", { responseType: "blob" });
    const url = window.URL.createObjectURL(new Blob([res.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "scan_history.xlsx");
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
}

export default api;
