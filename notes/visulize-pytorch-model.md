---
author: Vasken Dermardiros
title: visulize-pytorch-model
categories: note
tags:
- pytorch
- programming
- model
- visualization
links:
- https://appsilon.com/visualize-pytorch-neural-networks/
- https://github.com/lutzroeder/netron
---

Tried this when exploring the stable diffusion code.

## Basic `print`

Given a model `model`, you can simply do: `print(model)` and you get something like:

``` plain
ContextUnet(
  (init_conv): ResidualConvBlock(
    (conv1): Sequential(
      (0): Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
      (1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (2): GELU(approximate='none')
    )
    (conv2): Sequential(
      (0): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
      (1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (2): GELU(approximate='none')
    )
  )
  (down1): UnetDown(
    (model): Sequential(
      (0): ResidualConvBlock(
        (conv1): Sequential(
          (0): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1),
          padding=(1, 1))

    ...
```

## Torchviz

`pip install torchviz` first.

``` python
from torchviz import make_dot

# Dummy batch (easier than using the real thing)
X_dummy = (
    torch.randn(batch_size, 3, height, height, device=device),  # image
    torch.randn(batch_size, device=device),  # time
    torch.randn(batch_size, n_cfeat, device=device),  # context label
)

# Model
make_dot(model(*X_dummy), params=dict(nn_model.named_parameters()))

# Show attributes and saves
make_dot(model(*X_dummy), params=dict(nn_model.named_parameters()), show_attrs=True, show_saved=True)
```

and the output is a very detailed output of every step. Would be nice if you can decide to open up which level of block.

## Netron

(NOTE: cannot export to ONNX right now because of a bug in PyTorch that's causing conflicts... To revisit when PyTorch >2.0.1 is out.)

This package allows to visualize an interactive [graph of a model](https://github.com/lutzroeder/netron) after it is converted to the [ONNX](https://onnx.ai/) format.

``` python
# Dummy batch (easier than using the real thing)
X_dummy = (
    torch.randn(batch_size, 3, height, height, device=device),  # image
    torch.randn(batch_size, device=device),  # time
    torch.randn(batch_size, n_cfeat, device=device),  # context label
)

# Export
torch.onnx.export(model, X_dummy, "model.onnx", verbose=True)
```

and then you import the `.onnx` model into the [Netron app website](https://netron.app/).

## Tensorboard

This can also be done with PyTorch models.

```python
!pip install tensorboard

from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("torchlogs/")
model = Net()
writer.add_graph(model, X)
writer.close()

```

```bash
cd <path-to-logs-dir>
tensorboard --logdir=./
```

Then open up the browser at `http://localhost:6006` and you should see the dashboard.
