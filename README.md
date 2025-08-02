# Space Station Object Detection (YOLOv8)

## Overview
This project detects **Toolbox**, **Oxygen Tank**, and **Fire Extinguisher** objects in space station images using YOLOv8.

## Dataset
- Train images: 846
- Validation images: 154
- Classes: Toolbox, Oxygen Tank, Fire Extinguisher

## Performance
- mAP@0.5: **0.916**
- mAP@0.5:0.95: **0.792**
- Class-wise mAP:
  - Toolbox: 0.81
  - Oxygen Tank: 0.83
  - Fire Extinguisher: 0.72

## Files
- `best.pt`: Trained YOLOv8 model weights
- `data.yaml`: Dataset configuration
- `train.py`: Script to train the model
- `predict.py`: Script to run inference
- `results/`: Training results (metrics, graphs, confusion matrix)
- `Performance_Report.pdf`: Performance analysis

## Steps to Reproduce
1. Install dependencies:
   ```bash
   pip install ultralytics opencv-python torch
