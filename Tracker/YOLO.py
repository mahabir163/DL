from ultralytics import YOLO

model = YOLO("best.pt")

results = model.track(source=0,conf=0.3,iou=0.5,show=True)
print(results)
