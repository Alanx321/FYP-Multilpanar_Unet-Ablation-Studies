# main.py
# =========================================================
# Skeleton code for Medical Image Segmentation FYP
# University of Nottingham Malaysia
# Author: Alan
# =========================================================

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as T

# ---------------------------------------------------------
# 1. Dataset Loader (Skeleton)
# ---------------------------------------------------------
class MedicalDataset(Dataset):
    def __init__(self, image_paths, mask_paths, transform=None):
        # Store image & mask paths
        self.image_paths = image_paths
        self.mask_paths = mask_paths
        self.transform = transform

    def __len__(self):
        # Return total dataset size
        return len(self.image_paths)

    def __getitem__(self, idx):
        # Load image & mask (replace with actual medical image reader, e.g. nibabel for MRI/CT)
        image = torch.randn(1, 256, 256)   # Placeholder random tensor
        mask = torch.randint(0, 2, (1, 256, 256)) # Binary mask

        if self.transform:
            image = self.transform(image)

        return image, mask

# ---------------------------------------------------------
# 2. Simple UNet Model (Placeholder)
# ---------------------------------------------------------
class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        # TODO: Add encoder, bottleneck, decoder blocks
        self.conv = nn.Conv2d(1, 1, kernel_size=3, padding=1)

    def forward(self, x):
        return torch.sigmoid(self.conv(x))

# ---------------------------------------------------------
# 3. Training Loop (Skeleton)
# ---------------------------------------------------------
def train(model, dataloader, optimizer, criterion, device):
    model.train()
    total_loss = 0
    for images, masks in dataloader:
        images, masks = images.to(device), masks.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, masks.float())
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(dataloader)

# ---------------------------------------------------------
# 4. Main (Setup Training)
# ---------------------------------------------------------
def main():
    # Config
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Dataset (dummy example)
    train_dataset = MedicalDataset([], [])
    train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)

    # Model, Loss, Optimizer
    model = UNet().to(device)
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    # Training loop (placeholder)
    for epoch in range(5):
        loss = train(model, train_loader, optimizer, criterion, device)
        print(f"Epoch {epoch+1}, Loss: {loss:.4f}")

if __name__ == "__main__":
    main()
