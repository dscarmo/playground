'''
Let's see how mlflow's log_model works
'''
import mlflow as mlf
from mlflow.pytorch import log_model
import torch


class DummyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x):
        return self.linear(x)


if __name__ == "__main__":
    mlf.set_experiment("Playground")

    with mlf.start_run(run_name="Testing mlflow log_model"):
        mlf.log_param("Hello", "World")
        mlf.log_metric("a", 0)
        a = DummyModel()

        log_model(a, "models")