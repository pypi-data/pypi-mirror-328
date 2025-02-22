from dataclasses import dataclass
import torch


@dataclass 
class TrainConfig:
    """Training configuration"""
    
    num_epochs: int
    batch_size: int
    lr: float
    wd: float
    optimizer: str # string should resolve to a torch.optim.Optimizer object
    clip_val: float = 1
    val_freq: int = 1