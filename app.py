import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

# 1. 20개의 클래스 이름
CLASS_NAMES = [
    "패턴1", "패턴2", "패턴3", "패턴4", "패턴5",
    "패턴6", "패턴7", "패턴8", "패턴9", "패턴10",
    "패턴11", "패턴12", "패턴13", "패턴14", "패턴15",
    "패턴16", "패턴17", "패턴18", "패턴19", "Other"
]


def load_model():
    model = resnet18(weights=None)

    # ★수정 1: 흑백 이미지(1채널)를 받도록 모델의 첫 번째 층을 수정★
    model.conv1 = torch.nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)

    # 20개 클래스에 맞게 마지막 출력층 수정
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, 20)

    # 가중치 덮어씌우기
    state_dict = torch.load('best_chart_resnet_model.pth', map_location='cpu')
    model.load_state_dict(state_dict)

    model.eval()
    return model


model = load_model()

# ★수정 2: 이미지 전처리 정규화(Normalize)를 1채널에 맞게 변경★
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])  # 코랩 학습 시 다른 값을 썼다면 수정해주세요.
])


@app.post("/predict/")
async def predict_chart(file: UploadFile = File(...)):
    image_data = await file.read()

    # ★수정 3: 이미지를 RGB(컬러)가 아닌 L(흑백)로 변환하여 읽기★
    image = Image.open(io.BytesIO(image_data)).convert('L')

    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        top_prob, top_catid = torch.max(probabilities, 0)

    pattern_name = CLASS_NAMES[top_catid.item()]

    return {
        "pattern": pattern_name,
        "confidence": float(top_prob.item())
    }