from ultralytics import YOLO

model = YOLO("deneme.pt")
print("✅ YOLO modeli yüklendi.")
print("📦 Sınıflar:", model.names)