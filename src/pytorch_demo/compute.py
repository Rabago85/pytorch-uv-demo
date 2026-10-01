# import torch


# def run_pytorch_demo():
#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#     print(f"PyTorch version: {torch.__version__}")
#     print(f"Selected device: {device}")

#     x = torch.tensor([1.0, 2.0, 3.0], device=device)
#     y = x * 2

#     print(f"Input: {x}")
#     print(f"Output: {y}")

#     return y
import torch


def run_pytorch_demo():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print(f"PyTorch version: {torch.__version__}")
    print(f"Selected device: {device}")

    x = torch.tensor([1.0, 2.0, 3.0], device=device)
    y = x * 2

    print(f"Input: {x}")
    print(f"Output: {y}")
    print(f"Sum: {y.sum().item()}")

    return y