import torch

def main():
    print("Hello from llms-from-scratch!")

def torch_check():
    print(torch.__version__)
    print(torch.cuda.is_available())

if __name__ == "__main__":
    main()
    torch_check()
