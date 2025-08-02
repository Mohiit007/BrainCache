from ultralytics import YOLO

# Load your trained model
model = YOLO('best.pt')

# Run predictions on test images
results = model.predict(source='path_to_test_images', save=True)
