import torch
import torch.nn as nn
from tqdm.auto import tqdm
from .validate import validate
import wandb


def train(epochs, transformer, loss_fn, train_dl, optimizer=torch.optim.Adam, lr=1e-4, device=None, validate_data=False, validation_dl=None, wandb_tracking:str=None):
    if not device:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    transformer.to(device)  # Ensure the transformer model is moved to the correct device
    optimizer = optimizer(transformer.parameters(), lr=lr)
    
    for epoch in tqdm(range(epochs)):
        transformer.train()
        total_loss = 0
        
        for tensor_tokens in train_dl:
            tensor_tokens = tensor_tokens.to(device)  # Move the tensor to the device
            out = transformer(tensor_tokens, tensor_tokens)
            target = tensor_tokens
            loss_fn = nn.CrossEntropyLoss()
            loss = loss_fn(out.view(-1, out.size(-1)), target.view(-1))
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        if wandb_tracking:
            run = wandb.init(
                            project=wandb_tracking,
                            config = {
                                "Learning_Rate": lr,
                                "Epochs":epochs
                            })
            wandb.log({"batch_train_loss": loss.item()})
        
        print(f"Epoch: {epoch+1} | Loss: {total_loss / len(train_dl):.4f}")

        if validate_data:
            loss = validate(transformer, validation_dl, loss_fn, device)
            if wandb_tracking:
                wandb.log({"batch__validation_loss": loss.item()})



