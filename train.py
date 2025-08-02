from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('yolov8n.pt')

# Train
model.train(
    data='data.yaml',
    epochs=15,
    imgsz=640
)
