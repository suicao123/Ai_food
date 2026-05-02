import Link from "next/link";
import React from "react";

export default function UserLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      {/* ── Navigation (Chỉ dành cho User) ────────────────────────── */}
      <nav className="sticky top-0 z-50 glass-card border-b border-t-0 border-x-0 rounded-none px-6 py-3 flex items-center justify-between">
        <Link
          href="/"
          className="text-xl font-bold gradient-text tracking-tight"
        >
          🍜 Food Tracker AI
        </Link>

        <div className="flex gap-4 text-sm font-medium">
          <Link
            href="/"
            className="text-slate-300 hover:text-white transition-colors"
          >
            Upload
          </Link>
          <Link
            href="/live"
            className="text-slate-300 hover:text-white transition-colors"
          >
            Live Scan
          </Link>
          <Link
            href="/history"
            className="text-slate-300 hover:text-white transition-colors"
          >
            Lịch sử
          </Link>
        </div>
      </nav>

      {/* ── Main content (Đóng khung cho User) ────────────────────── */}
      <main className="max-w-5xl mx-auto px-4 py-8">{children}</main>
    </>
  );
}
