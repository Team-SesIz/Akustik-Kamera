"""
Sahte ısı haritası sunucusu (WebSocket).

Algoritma hazır olana kadar paneli "gerçek veri" modunda test etmek için.
Okan'ın algoritması ileride aynı JSON formatını aynı adrese gönderecek.

Kurulum:  pip install websockets
Çalıştır: python fake_server.py
Panelde:  Veri kaynağı -> WebSocket, adres ws://localhost:8765 -> Bağlan
"""
import asyncio
import json
import math
import random
import time

import websockets

W, H = 16, 12  # ızgara boyutu (docs/interfaces.md ile aynı olmalı)


def make_frame(t: float) -> dict:
    cx = 0.5 + 0.35 * math.sin(t * 0.5)
    cy = 0.5 + 0.25 * math.cos(t * 0.7)
    data = []
    for y in range(H):
        for x in range(W):
            dx, dy = x / (W - 1) - cx, y / (H - 1) - cy
            v = math.exp(-(dx * dx + dy * dy) / 0.02) + random.random() * 0.08
            data.append(round(min(1.0, v), 3))
    return {"t": time.time(), "w": W, "h": H, "data": data}


async def handler(ws):
    print("Panel bağlandı")
    try:
        while True:
            await ws.send(json.dumps(make_frame(time.time())))
            await asyncio.sleep(0.1)  # 10 kare/sn
    except websockets.ConnectionClosed:
        print("Panel ayrıldı")


async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("ws://localhost:8765 dinleniyor (Ctrl+C ile durdur)")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
