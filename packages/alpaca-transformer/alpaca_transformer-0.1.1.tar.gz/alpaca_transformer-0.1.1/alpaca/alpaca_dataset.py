import torch
import torch.nn.functional as F
from torch.utils.data import Dataset

class AlpacaDataset(Dataset):
    def __init__(self, txt_file, tokenizer, max_seq_len=512):
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len
        
       
        with open(txt_file, 'r') as f:
            whole_text = f.read()  
        
        
        self.vocab = self.tokenizer.create_vocab(whole_text)
        
        
        with open(txt_file, 'r') as f:
            self.sentences = f.readlines()

    def __getitem__(self, index):
        sentence = self.sentences[index]
        
        tokens = self.tokenizer.tokenize(sentence, vocab=self.vocab)
        
       
        tokens = [t if 0 <= t < len(self.vocab) else 0 for t in tokens]  
        
        
        tokens = [t if t >= 0 else 0 for t in tokens]
        
        
        if len(tokens) < self.max_seq_len:
            padding = [0] * (self.max_seq_len - len(tokens))
            tokens = tokens + padding
        else:
            tokens = tokens[:self.max_seq_len]
        
        return torch.tensor(tokens)

    
    def __len__(self):
        return len(self.sentences)
