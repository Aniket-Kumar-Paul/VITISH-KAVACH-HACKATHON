import torch
from vit_pytorch import ViT_face, ViTs_face
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

import albumentations as A
from albumentations.pytorch import ToTensorV2

from loss import OctupletLoss

print(ViT_face)

def get_image_tensor(path: str):
    img1 = cv2.imread(path)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img1 = cv2.resize(img1, (112, 112)) / 255.0
    x1 = torch.tensor([img1], dtype=torch.float32).permute(0, 3, 1, 2) / 1.0
    print(x1.min(), x1.max())
    return x1

x1 = get_image_tensor('../images/neeraj.jpeg')
print(x1.min(), x1.max())
img1 = x1[0].permute(1, 2, 0)
print(img1.shape)


print(x1.shape)

x2 = get_image_tensor('../images/aniket.jpeg')
print(x2.min(), x2.max())
img2 = x2[0].permute(1, 2, 0)
print(img2.shape)


print(x2.shape)

model = ViTs_face(
    loss_type='CosFace',
    GPU_ID=torch.device("cuda" if torch.has_cuda else "cpu"),
    num_class=93431,
    image_size=112,
    patch_size=8,
    ac_patch_size=12,
    pad=4,
    dim=512,
    depth=20,
    heads=8,
    mlp_dim=2048,
    dropout=0.1,
    emb_dropout=0.1
)

cp = torch.load(
    '../artifacts/model-weights/Backbone_VITs_Epoch_2_Batch_12000_Time_2021-03-17-04-05_checkpoint.pth',
    map_location='cpu'
)
model.load_state_dict(cp)
model.eval()


model = torch.load('../artifacts/model-weights/FaceTransformerOctupletLoss.pt')

with torch.no_grad():
    y1 = model.forward(x1)
    y2 = model.forward(x2)

print()
