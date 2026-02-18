#!/usr/bin/env python3
import time
import random

print("🔥 AUTO-SENDER DIMULAI...")
print("Target: 628+62 813-7604-9703")

# Baca virtex
try:
    with open("virtex_gila.txt", "r", encoding="utf-8") as f:
        virtex = f.read()
except:
    virtex = "VIRUS TOTAL " + "x" * 10000

print("Kirim pesan setiap 0.5 detik...")

for i in range(1000):
    print(f"[✓] Kirim ke-{i+1}")
    # Ini cuma simulasi, ganti dengan API beneran kalo ada
    # requests.post("https://api.example.com/send", data={"to":"628+62 813-7604-9703", "text":virtex})
    time.sleep(0.5)

print("SELESAI!")
