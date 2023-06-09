import argparse
import warnings
from code.trainer import AutoEncoderTrainer

import torch

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train AutoEncoder")
    parser.add_argument("--root", type=str, default="data")
    parser.add_argument("--test-root", type=str, default="test_root")
    parser.add_argument("--resnet-model", type=str, default="resnet34",
                        choices=["resnet18", "resnet34", "resnet50", "resnet101", "resnet152"])
    parser.add_argument("--qb", type=int, default=4)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--save-results-every", type=int, default=10)
    parser.add_argument("--save-models-dir", type=str, default="models")
    parser.add_argument("--use-checkpoint", action="store_true")
    args = parser.parse_args()

    print("Starting training with the following parameters:")
    for arg in vars(args):
        print(f"{arg}: {getattr(args, arg)}")

    print()

    trainer = AutoEncoderTrainer(
        root=args.root,
        test_root=args.test_root,
        resnet_model_name=args.resnet_model,
        qb=args.qb,
        epochs=args.epochs,
        batch_size=args.batch_size,
        lr=args.lr,
        device=args.device,
        save_results_every=args.save_results_every,
        save_models_dir=args.save_models_dir,
        use_checkpoint=args.use_checkpoint
    )

    trainer.train()

