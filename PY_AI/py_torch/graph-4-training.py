import torch.optim as optim

optimizer = optim.Adam(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

epochs = 50
for epoch in range(epochs):
    optimizer.zero_grad()
    predictions = model(sources, targets).squeeze()
    loss = criterion(predictions, values)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch} Loss: {loss.item()}")
    if epoch % 10 == 0:
        torch.save(model.state_dict(), f"blockchain_model_{epoch}.pth")