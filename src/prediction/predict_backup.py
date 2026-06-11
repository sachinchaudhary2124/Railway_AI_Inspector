from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.append(str(SRC_PATH))

print("Project Root :", PROJECT_ROOT)

import torch
import torch.nn as nn

from PIL import Image
from reports.report_generator import save_report

from torchvision import models
from torchvision import transforms

print("Libraries Imported Successfully")



# ==========================================================
# PROJECT ROOT
# ==========================================================





# ==========================================================
# MODEL PATH
# ==========================================================

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "railway_resnet18_augmented.pth"
)

print("Model Path :", MODEL_PATH)
print("Model Exists :", MODEL_PATH.exists())



##########################################################################
# ==========================================================
# CLASS NAMES
# ==========================================================

CLASSES = [
    "broken_rail",
    "crack",
    "misalignment",
    "normal",
    "surface_wear"
]

print("Classes :", CLASSES)


# ==========================================================
# CREATE RESNET18 MODEL
# ==========================================================

model = models.resnet18(weights=None)

model.fc = nn.Linear(
    model.fc.in_features,
    len(CLASSES)
)

print("ResNet18 Architecture Created")


# =====================================================
# LOAD TRAINED WEIGHTS
# =====================================================

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=torch.device("cpu")
    )
)

model.eval()

print("Model Weights Loaded Successfully")


# =====================================================
# IMAGE TRANSFORM
# =====================================================

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

print("Image Transform Created")


# =====================================================
# IMAGE PATH
# =====================================================

IMAGE_PATH = (
    PROJECT_ROOT
    / "data"
    / "test"
    / "crack"
    / "crack.jpg"
)

print("Image Path :", IMAGE_PATH)
print("Image Exists :", IMAGE_PATH.exists())



# =====================================================
# LOAD IMAGE
# =====================================================

image = Image.open(IMAGE_PATH)

print("Image Loaded Successfully")
print("Image Size :", image.size)
print("Image Mode :", image.mode)


# =====================================================
# APPLY TRANSFORM
# =====================================================

image_tensor = transform(image)

print("Tensor Shape :", image_tensor.shape)

# =====================================================
# ADD BATCH DIMENSION
# =====================================================

image_tensor = image_tensor.unsqueeze(0)

print("Batch Tensor Shape :", image_tensor.shape)


# =====================================================
# MODEL PREDICTION
# =====================================================

with torch.no_grad():

    output = model(image_tensor)

print("Raw Output :", output)
print("Output Shape :", output.shape)


# =====================================================
# GET PREDICTED CLASS
# =====================================================

predicted_index = torch.argmax(output, dim=1).item()

predicted_class = CLASSES[predicted_index]

print("Predicted Index :", predicted_index)
print("Predicted Class :", predicted_class)



# =====================================================
# CONFIDENCE SCORE
# =====================================================

probabilities = torch.softmax(output, dim=1)

confidence = probabilities[0][predicted_index].item() * 100

print("Confidence : {:.2f}%".format(confidence))


# =====================================================
# REPAIR PRIORITY
# =====================================================

if predicted_class == "broken_rail":
    priority = "CRITICAL"

elif predicted_class == "crack":

    if confidence >= 90:
        priority = "HIGH"
    else:
        priority = "MEDIUM"

elif predicted_class == "misalignment":
    priority = "HIGH"

elif predicted_class == "surface_wear":
    priority = "MEDIUM"

else:
    priority = "LOW"

print("Repair Priority :", priority)



#################################################################################
# =====================================================
# MAINTENANCE REPORT
# =====================================================

print("\n")
print("=" * 50)
print("RAILWAY INSPECTION REPORT")
print("=" * 50)

print("Anomaly Type     :", predicted_class)
print("Confidence Score :", f"{confidence:.2f}%")
print("Priority Level   :", priority)

if predicted_class == "broken_rail":
    action = "Immediate track shutdown and repair."

elif predicted_class == "crack":
    action = "Schedule urgent rail inspection and repair."

elif predicted_class == "misalignment":
    action = "Inspect alignment and perform corrective maintenance."

elif predicted_class == "surface_wear":
    action = "Monitor wear and schedule preventive maintenance."

else:
    action = "No maintenance required."

print("Recommended Action :", action)


print("=" * 50)

#########################################################################
# =====================================================
# GEOLOCATION DATA
# =====================================================

latitude = 21.1702
longitude = 72.8311



print("\nLocation Information")
print("Latitude  :", latitude)
print("Longitude :", longitude)


save_report(
    anomaly_type=predicted_class,
    confidence=confidence,
    priority=priority,
    action=action,
    latitude=latitude,
    longitude=longitude
)