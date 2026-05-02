"use client";

import { useCallback, useEffect, useState } from "react";
import Image from "next/image";
import { exportExcel, getHistory, HistoryRecord } from "@/lib/api";

export default function HistoryPage() {
    const [records, setRecords] = useState<HistoryRecord[]>([]);
    const [loading, setLoading] = useState(true);
    const [exporting, setExporting] = useState(false);

    const fetchData = useCallback(async () => {
        setLoading(true);
        try {
            const data = await getHistory();
            setRecords(data);
        } catch {
            console.error("Failed to load history");
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => {
        fetchData();
    }, [fetchData]);

    const handleExport = async () => {
        setExporting(true);
        try {
            await exportExcel();
        } catch {
            alert("Xuất file thất bại!");
        } finally {
            setExporting(false);
        }
    };

    const formatDate = (iso: string | null) => {
        if (!iso) return "—";
        return new Date(iso).toLocaleString("vi-VN", {
            day: "2-digit",
            month: "2-digit",
            year: "numeric",
            hour: "2-digit",
            minute: "2-digit",
        });
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* ── Header ───────────────────────────────────────────── */}
            <div className="flex items-center justify-between">
                <div>
                    <h1 className="text-3xl font-extrabold gradient-text">Lịch Sử Quét</h1>
                    <p className="text-slate-400 text-sm mt-1">
                        {records.length} kết quả đã ghi nhận
                    </p>
                </div>
            </div>

            {/* ── Table ────────────────────────────────────────────── */}
            {loading ? (
                <div className="flex justify-center py-20">
                    <div className="spinner" />
                </div>
            ) : records.length === 0 ? (
                <div className="glass-card p-12 text-center text-slate-500">
                    Chưa có lịch sử quét nào.
                </div>
            ) : (
                <div className="glass-card overflow-hidden">
                    <div className="overflow-x-auto">
                        <table className="w-full text-sm">
                            <thead>
                                <tr className="border-b border-white/10 text-left text-xs uppercase tracking-wider text-slate-500">
                                    <th className="px-5 py-3">#</th>
                                    <th className="px-5 py-3">Ảnh</th>
                                    <th className="px-5 py-3">Tên món</th>
                                    <th className="px-5 py-3">Độ tin cậy</th>
                                    <th className="px-5 py-3">Thời gian</th>
                                </tr>
                            </thead>
                            <tbody>
                                {records.map((r, idx) => (
                                    <tr
                                        key={r.id}
                                        className="border-b border-white/5 hover:bg-white/[0.03] transition-colors"
                                    >
                                        <td className="px-5 py-3 text-slate-500">{idx + 1}</td>
                                        <td className="px-5 py-3">
                                            {r.image_path ? (
                                                <Image
                                                    src={`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}${r.image_path}`}
                                                    alt={r.food_name}
                                                    width={40}
                                                    height={40}
                                                    className="rounded-lg object-cover border border-white/10"
                                                />
                                            ) : (
                                                <div className="w-10 h-10 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-xs text-slate-600">
                                                    —
                                                </div>
                                            )}
                                        </td>
                                        <td className="px-5 py-3 font-medium text-white">
                                            {r.food_name}
                                        </td>
                                        <td className="px-5 py-3">
                                            <div className="flex items-center gap-2">
                                                <div className="w-20 h-1.5 rounded-full bg-white/10">
                                                    <div
                                                        className="h-full rounded-full bg-gradient-to-r from-indigo-500 to-emerald-500"
                                                        style={{
                                                            width: `${Math.round(r.confidence * 100)}%`,
                                                        }}
                                                    />
                                                </div>
                                                <span className="text-indigo-300 text-xs font-semibold">
                                                    {Math.round(r.confidence * 100)}%
                                                </span>
                                            </div>
                                        </td>
                                        <td className="px-5 py-3 text-slate-400">
                                            {formatDate(r.created_at)}
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            )}

            {/* ── Floating export button ───────────────────────────── */}
            <button
                onClick={handleExport}
                disabled={exporting || records.length === 0}
                className="fixed bottom-6 right-6 flex items-center gap-2 px-5 py-3 rounded-full font-semibold text-sm
                   bg-gradient-to-r from-indigo-600 to-violet-600 text-white shadow-lg shadow-indigo-500/30
                   hover:shadow-indigo-500/50 hover:scale-105 active:scale-95
                   transition-all disabled:opacity-40 disabled:cursor-not-allowed pulse-ring"
            >
                {exporting ? (
                    <>
                        <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        Đang xuất…
                    </>
                ) : (
                    <>📥 Xuất Excel</>
                )}
            </button>
        </div>
    );
}
