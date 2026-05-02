"use client";

import React, { useEffect, useRef, useState } from "react";

export default function LiveScanner() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const overlayCanvasRef = useRef<HTMLCanvasElement>(null);
  const hiddenCanvasRef = useRef<HTMLCanvasElement>(null);
  const wsRef = useRef<WebSocket | null>(null);

  const [isConnected, setIsConnected] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const isProcessingRef = useRef(false);

  useEffect(() => {
    // 1. Setup Camera Stream
    let stream: MediaStream | null = null;
    const startCamera = async () => {
      try {
        stream = await navigator.mediaDevices.getUserMedia({
          video: { 
            width: { ideal: 1280 },
            height: { ideal: 720 },
            facingMode: "environment" 
          },
          audio: false,
        });
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (err: any) {
        setError(`Failed to access camera: ${err.message}`);
      }
    };

    startCamera();

    // 2. Setup WebSocket - Use 127.0.0.1 for better compatibility on Windows
    const ws = new WebSocket("ws://127.0.0.1:8000/api/ws/live");
    wsRef.current = ws;

    ws.onopen = () => {
      setIsConnected(true);
      setError(null);
      console.log("WebSocket connected");
    };

    ws.onclose = () => {
      setIsConnected(false);
      console.log("WebSocket disconnected");
    };

    ws.onerror = (err) => {
      console.error("WebSocket error", err);
      // Don't set error immediately if it's just a fast refresh disconnect
      if (ws.readyState === WebSocket.CLOSED) {
        setError("WebSocket connection error");
      }
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      drawBoundingBoxes(data);
      isProcessingRef.current = false; // Release lock when results arrive
    };

    // Cleanup on unmount
    return () => {
      if (stream) {
        stream.getTracks().forEach((track) => track.stop());
      }
      if (ws) {
        ws.close();
      }
    };
  }, []);

  // 3. Capture Frames & Send via WebSocket
  useEffect(() => {
    let intervalId: NodeJS.Timeout;

    const captureAndSend = () => {
      // Only send if connected, not currently processing a frame, and WS is open
      if (!isConnected || isProcessingRef.current || !videoRef.current || !hiddenCanvasRef.current || !wsRef.current) return;
      if (wsRef.current.readyState !== WebSocket.OPEN) return;

      const video = videoRef.current;
      const canvas = hiddenCanvasRef.current;
      const ctx = canvas.getContext("2d");

      if (!ctx || video.videoWidth === 0 || video.videoHeight === 0) return;

      // Set canvas size to match video resolution
      if (canvas.width !== video.videoWidth || canvas.height !== video.videoHeight) {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
      }

      // Draw current video frame to hidden canvas
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

      // Convert to Base64 JPEG
      const base64Image = canvas.toDataURL("image/jpeg", 0.6); // Lower quality for speed

      // Send via WebSocket
      const base64Data = base64Image.split(",")[1];
      isProcessingRef.current = true; // Set lock
      wsRef.current.send(base64Data);
    };

    if (isConnected) {
      intervalId = setInterval(captureAndSend, 100); // Try 10 FPS, but controlled by isProcessingRef
    }

    return () => {
      if (intervalId) clearInterval(intervalId);
    };
  }, [isConnected]);

  // 4. Draw Bounding Boxes
  const drawBoundingBoxes = (detections: any) => {
    if (!overlayCanvasRef.current || !videoRef.current) return;

    const canvas = overlayCanvasRef.current;
    const video = videoRef.current;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    // Match overlay canvas size to video layout size
    if (canvas.width !== video.clientWidth || canvas.height !== video.clientHeight) {
      canvas.width = video.clientWidth;
      canvas.height = video.clientHeight;
    }

    // We need to scale the coordinates from original video resolution to the displayed canvas size
    const scaleX = canvas.width / video.videoWidth;
    const scaleY = canvas.height / video.videoHeight;

    // Clear previous drawings
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (detections && detections.boxes) {
      detections.boxes.forEach((box: any) => {
        const { x, y, w, h, label, confidence } = box;

        // Apply scale
        const scaledX = x * scaleX;
        const scaledY = y * scaleY;
        const scaledW = w * scaleX;
        const scaledH = h * scaleY;

        // Draw Box
        ctx.strokeStyle = "#00FF00";
        ctx.lineWidth = 3;
        ctx.strokeRect(scaledX, scaledY, scaledW, scaledH);

        // Draw Label with background
        const text = `${label} (${(confidence * 100).toFixed(1)}%)`;
        ctx.font = "bold 16px sans-serif";
        const textWidth = ctx.measureText(text).width;
        
        ctx.fillStyle = "#00FF00";
        ctx.fillRect(scaledX, scaledY > 25 ? scaledY - 25 : scaledY, textWidth + 10, 25);
        
        ctx.fillStyle = "#000000";
        ctx.fillText(text, scaledX + 5, scaledY > 25 ? scaledY - 7 : scaledY + 18);
      });
    }
  };

  return (
    <div className="flex flex-col items-center justify-center space-y-6 w-full max-w-6xl mx-auto">
      <div className="text-center w-full">
        <h1 className="text-4xl font-bold gradient-text mb-2">Live Camera Scan</h1>
        <p className="text-slate-400 text-lg">
          Point your camera at food to detect it in real-time.
        </p>
        {!isConnected && !error && (
          <p className="text-yellow-400 text-sm mt-2 animate-pulse">Connecting to AI Server...</p>
        )}
        {error && <p className="text-red-400 text-sm mt-2 font-semibold">⚠️ {error}</p>}
      </div>

      <div className="relative w-full rounded-2xl overflow-hidden glass-card border-2 border-slate-700 shadow-2xl aspect-video flex items-center justify-center bg-black">
        <video
          ref={videoRef}
          autoPlay
          playsInline
          muted
          className="absolute inset-0 w-full h-full object-contain"
        />
        <canvas
          ref={overlayCanvasRef}
          className="absolute inset-0 w-full h-full object-contain pointer-events-none"
        />
        {/* Hidden canvas for capturing frames */}
        <canvas ref={hiddenCanvasRef} className="hidden" />
      </div>
    </div>
  );
}
