# web/ — Akustik Kamera paneli

Kamera görüntüsü ve üstünde ses kaynağı ısı haritası gösteren web paneli.
Kart gerekmez; laptop kamerasıyla çalışır.

## Çalıştırma

```bash
cd web
python -m http.server 8000
```

Tarayıcıda **http://localhost:8000** açın → "Kamerayı başlat" → kamera iznini verin.
(Kamera yalnızca `localhost` veya `https` üzerinden açılır.)

## Isı haritası kaynakları

- **Demo**: Tarayıcı içinde dolaşan sahte bir ses kaynağı üretir. Ek kurulum gerekmez.
- **WebSocket**: Gerçek veri için. Test etmek isterseniz:
  ```bash
  pip install websockets
  python fake_server.py
  ```
  Panelde Veri kaynağı → WebSocket → `ws://localhost:8765` → Bağlan.

## Veri formatı (docs/interfaces.md önerisi)

Algoritma her karede şu JSON'u gönderir:

```json
{ "t": 1732190000.12, "w": 16, "h": 12, "data": [0.0, 0.1, ...] }
```

- `t`: zaman damgası (saniye, unix)
- `w`, `h`: ızgara sütun ve satır sayısı
- `data`: `w*h` sayı, sol üstten satır satır, 0–1 arası (1 = en yüksek ses)

## Durum (1. hafta)

- [x] Panel iskeleti
- [x] Kamera akışı web'de (kamera seçimi dahil)
- [x] Isı haritası katmanı, renk ölçeği, saydamlık ve eşik ayarı
- [x] Demo veri + WebSocket bağlantısı (2. hafta işinin altyapısı)
