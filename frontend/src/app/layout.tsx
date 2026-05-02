import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Food Tracker AI",
  description:
    "Nhận diện món ăn Việt Nam bằng AI – Quét ảnh, xem thông tin dinh dưỡng và lịch sử quét.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="vi">
      <body className="antialiased bg-[#0a0a0b] text-white">
        {children}
      </body>
    </html>
  );
}
