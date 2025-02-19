import torch
import torch.nn as nn
from tqdm.auto import tqdm
from .validate import validate
import wandb

def train(epochs, transformer, loss_fn, train_dl, optimizer=torch.optim.Adam, lr=1e-4, device=None, validate_data=False, validation_dl=None, wandb_tracking:str=None):
    if not device:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    transformer.to(device)
    optimizer = optimizer(transformer.parameters(), lr=lr)
    
    if wandb_tracking:
        wandb.init(project=wandb_tracking, config={"Learning_Rate": lr, "Epochs": epochs})

    for epoch in tqdm(range(epochs)):
        transformer.train()
        total_loss = 0
        
        for tensor_tokens in train_dl:
            tensor_tokens = tensor_tokens.to(device)
            out = transformer(tensor_tokens, tensor_tokens)
            target = tensor_tokens
            loss_fn = nn.CrossEntropyLoss()
            loss = loss_fn(out.view(-1, out.size(-1)), target.view(-1))
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()

            if wandb_tracking:
                wandb.log({"batch_train_loss": loss.item()})

        epoch_loss = total_loss / len(train_dl)
        if wandb_tracking:
            wandb.log({"epoch_train_loss": epoch_loss})
        
        print(f"Epoch: {epoch+1} | Loss: {epoch_loss:.4f}")

        if validate_data and validation_dl:
            val_loss = validate(transformer, validation_dl, loss_fn, device)
            if wandb_tracking:
                wandb.log({"epoch_validation_loss": val_loss})

    if wandb_tracking:
        wandb.finish()
