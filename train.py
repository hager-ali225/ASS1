import torch
import torch.nn as nn
import torch.optim as optim

from dataset import load_data
from models.model1 import Model1

X, Y = load_data("../data/data.txt")

X = torch.tensor(X, dtype=torch.float32)
Y = torch.tensor(Y, dtype=torch.float32)

model = Model1()

criterion = nn.MSELoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

EPOCHS = 100

for epoch in range(EPOCHS):

    optimizer.zero_grad()

    outputs = model(X)

    loss = criterion(outputs, Y)

    loss.backward()

    optimizer.step()

    print(
        f"Epoch {epoch+1} Loss: {loss.item()}"
    )

torch.save(
    model.state_dict(),
    "weights/model1.pth"
)

print("Training Finished")