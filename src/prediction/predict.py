from pathlib import Path
import sys
import torch
import torch.nn as nn

from PIL import Image
from torchvision import models, transforms

# ==================================================
# PROJECT ROOT
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.append(str(SRC_PATH))

# ==================================================
# CLASS NAMES
# ==================================================

CLASSES = [
    "broken_rail",
    "crack",
    "misalignment",
    "normal",
    "surface_wear"
]

# ==================================================
# MODEL PATH
# ==================================================

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "railway_resnet18_augmented.pth"
)

# ==================================================
# LOAD MODEL
# ==================================================

model = models.resnet18(weights=None)

model.fc = nn.Linear(
    model.fc.in_features,
    len(CLASSES)
)

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=torch.device("cpu")
    )
)

model.eval()

# ==================================================
# IMAGE TRANSFORM
# ==================================================

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# ==================================================
# PREDICTION FUNCTION
# ==================================================

def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image_tensor = transform(image)

    image_tensor = image_tensor.unsqueeze(0)

    with torch.no_grad():

        output = model(image_tensor)

    predicted_index = torch.argmax(
        output,
        dim=1
    ).item()

    predicted_class = CLASSES[predicted_index]

    probabilities = torch.softmax(
        output,
        dim=1
    )

    confidence = (
        probabilities[0][predicted_index].item()
        * 100
    )

    # ======================================
    # PRIORITY
    # ======================================

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

    # ======================================
    # ACTION
    # ======================================

    if predicted_class == "broken_rail":
        action = "Immediate track shutdown and repair."

    elif predicted_class == "crack":
        action = "Schedule urgent rail inspection and repair."

    elif predicted_class == "misalignment":
        action = (
            "Inspect alignment and perform corrective maintenance."
        )

    elif predicted_class == "surface_wear":
        action = (
            "Monitor wear and schedule preventive maintenance."
        )

    else:
        action = "No maintenance required."

    return {
        "anomaly": predicted_class,
        "confidence": round(confidence, 2),
        "priority": priority,
        "action": action
    }