# 🚀 OrbitalScan: Space Station Object Detection (YOLOv8)

**OrbitalScan** is an AI-powered computer vision solution designed to **detect critical objects inside a space station** using **YOLOv8**.  
Developed for **BuildWithDelhi 2.0 Hackathon** by **Team BrainCache**.

---

## 1. Problem Statement
Astronauts need **real-time monitoring of essential tools** (Toolbox, Oxygen Tanks, Fire Extinguishers) to ensure safety and operational efficiency in space missions.

---

## 2. Our Solution
We trained a custom **YOLOv8 model** achieving:
- **mAP@0.5 = 0.916**
- **mAP@0.5-0.95 = 0.792**

The solution is deployed as a **Streamlit Web App** with:
- Image/Video Upload
- Live Camera Detection
- Annotated Results Download
- Confusion Matrix & Performance Metrics
- Auto-generated PDF Reports

---

## 3. Features
- **High Accuracy** (91.6% mAP@0.5)
- **Interactive Space-Themed UI**
- **Live Detection via Camera**
- **PDF Performance Reports**
- **Optimized YOLOv8 Model**

---

## 4. Technologies Used
- **Python** (YOLOv8, OpenCV, Streamlit)
- **PyTorch** for model training
- **Pandas & Matplotlib** for analysis
- **FPDF** for report generation
- **Streamlit-Lottie** for animations

---

## 5. Project Structure
OrbitalScan/
│── app.py # Streamlit Web App
│── train.py # Training Script
│── predict.py # Inference Script
│── best.pt # Trained YOLOv8 Model
│── data.yaml # Dataset Configuration
│── requirements.txt # Dependencies
│── results/ # Performance Results (results.png, confusion matrix, etc.)
│── README.md # Documentation

yaml
Copy
Edit

---

## 6. How to Run Locally
1. **Clone the Repository**
   ```bash
   git clone https://github.com/YourRepo/OrbitalScan.git
   cd OrbitalScan
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the App

bash
Copy
Edit
streamlit run app.py
7. Deploy on Streamlit Cloud
Push this repo to GitHub

Go to Streamlit Cloud

Connect your repo and click Deploy

App will be available at:

arduino
Copy
Edit
https://your-app-name.streamlit.app
8. Performance Report
mAP@0.5: 0.916

mAP@0.5-0.95: 0.792

Confusion Matrix: Included in results/

Failure Case Analysis: Low-light images caused minor misclassifications. Plan: Add more data augmentation.

9. Demo
Web App: Streamlit App URL

Presentation: Google Slides

Model Weights: Google Drive

10. Team
BrainCache

Swastika

Mohit

Uday

Rohit

11. License
MIT License.

12. Acknowledgements
Special thanks to BuildWithDelhi 2.0 Hackathon organizers and Ultralytics YOLO.

