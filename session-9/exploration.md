#### PyTorch Library
pytorch is a deep learning framework which provides plethora of functions for developing different
machine learning and deep learning frameworks.
This is created by Facebook(Meta) and it is known for its pythonic approach and lucid way of developing the any deep learning model
Apart from some standard deep learning functions, it also provides other extended libraries like torchvision, torchaudio etc. For example torchvision has so many functionalities that can be used in the computer vision pipeline. For example image preprocessing functions like augmentations are provided in the torchvision library.

Apart from computer vision torch also has functionality for NLP(Natural Language Processing). It has all the predefined functions for transformer, LSTM, RNN, GRU which are heavily used in NLP applications

# For Example
```python
import torch
from torch.nn import Module, Sequential, Linear
import torch.nn as nn

# Pytroch simple model (Neural Network)
class Simple_Model(Module):
    def __init__(self, in_features, out_features):
        super(Simple_Module, self).__init__()

        self.model = Sequential(nn.Linear(in_features, 128),nn.ReLU(),
                    nn.Linear(128, 256), nn.ReLU(), nn.Linear(256,out_features))

    def forward(self,x):
        return self.model(x)

```