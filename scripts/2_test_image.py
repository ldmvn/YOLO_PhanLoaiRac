import argparse
from pathlib import Path

from ultralytics import YOLO


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT_DIR / "models" / "best.pt"
DEFAULT_IMAGE = ROOT_DIR / "test_images" / "test1.jpg"


def main() -> None:
    parser = argparse.ArgumentParser(description="Nhan dien rac trong mot anh")
    parser.add_argument("--image", type=Path, default=DEFAULT_IMAGE)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--conf", type=float, default=0.25)
    args = parser.parse_args()

    if not args.model.is_file():
        raise FileNotFoundError(f"Khong tim thay model: {args.model}")
    if not args.image.is_file():
        raise FileNotFoundError(f"Khong tim thay anh: {args.image}")

    model = YOLO(str(args.model))
    model.predict(
        source=str(args.image),
        conf=args.conf,
        save=True,
        project=str(ROOT_DIR / "runs"),
        name="predict",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()
