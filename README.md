# 🚆 Railway AI Inspector

An AI-Powered Railway Track Monitoring and Predictive Maintenance System developed as part of the SmartBridge Internship Program.

---

## 📌 Project Overview

Railway AI Inspector is a deep learning-based application that automatically detects railway track anomalies from images and provides maintenance recommendations.

The system helps improve railway safety by identifying track defects early and prioritizing maintenance actions.

---

## 🎯 Problem Statement

Manual railway track inspection is:

- Time-consuming
- Labor-intensive
- Prone to human error
- Difficult to scale

This project uses Computer Vision and Deep Learning to automate anomaly detection and support predictive maintenance.

---

## 🚀 Features

### Landing Page
- Professional railway-themed UI
- Centralized control center access

### Railway Inspection Dashboard
- Upload railway track images
- Real-time anomaly prediction
- Confidence score generation
- Maintenance priority classification
- Track status monitoring

### Anomaly Detection

The system can detect:

- Crack
- Misalignment
- Broken Rail
- Surface Wear
- Normal Track

### Analytics Dashboard

Provides:

- Anomaly Distribution Visualization
- Confidence Trend Analysis
- Prediction History Insights

### Reports Module

Generates inspection summaries and maintenance recommendations.

---

## 🏗️ Project Architecture

```
Input Railway Image
        │
        ▼
 Image Preprocessing
        │
        ▼
 Deep Learning Model
   (ResNet18 CNN)
        │
        ▼
 Anomaly Classification
        │
        ▼
 Priority Assignment
        │
        ▼
 Dashboard Visualization
        │
        ▼
 Maintenance Recommendation
```

---

## 🧠 Technologies Used

### Frontend

- Streamlit

### Backend

- Python

### Deep Learning

- PyTorch
- Torchvision

### Data Processing

- NumPy
- Pandas

### Visualization

- Matplotlib

### Image Processing

- Pillow (PIL)

---

## 📂 Project Structure

```
Railway_AI_Inspector
│
├── data
│   ├── train
│   ├── validation
│   └── test
│
├── models
│   ├── railway_cnn_baseline.pth
│   ├── railway_resnet18_augmented.pth
│   └── railway_resnet18_transfer.pth
│
├── notebooks
│
├── src
│   ├── dashboard
│   ├── prediction
│   ├── preprocessing
│   ├── detection
│   └── reports
│
├── requirements.txt
└── README.md
```

---

## 🤖 Deep Learning Model

### Model Used

ResNet18

### Training Strategy

- Transfer Learning
- Data Augmentation
- Image Normalization
- Multi-Class Classification

### Output Classes

1. Crack
2. Misalignment
3. Broken Rail
4. Surface Wear
5. Normal

---

## 📊 Sample Output

Example Prediction:

| Metric | Value |
|----------|----------|
| Anomaly | Misalignment |
| Confidence | 99.96% |
| Priority | High |
| Track Status | Warning |

Recommended Action:

> Inspect alignment and perform corrective maintenance.

---

## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/sachinchaudhary2124/Railway_AI_Inspector.git
```

### Navigate

```bash
cd Railway_AI_Inspector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run src/dashboard/dashboard.py
```

---

## 🌐 Deployment

Streamlit Cloud Deployment:

(https://sachinchaudhary2124-railway-ai-ins-srcdashboarddashboard-cvgdyy.streamlit.app/)



## 📈 Future Enhancements

- Real-time railway camera integration
- Video anomaly detection
- IoT sensor integration
- Predictive failure forecasting
- Maintenance scheduling automation
- Railway Digital Twin Integration

---

