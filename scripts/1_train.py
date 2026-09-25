from pathlib import Path

from ultralytics import YOLO


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_CONFIG = ROOT_DIR / "dataset" / "data.yaml"
BASE_MODEL = ROOT_DIR / "models" / "yolov8n.pt"
RUNS_DIR = ROOT_DIR / "runs"


def main() -> None:
    if not DATA_CONFIG.is_file():
        raise FileNotFoundError(f"Khong tim thay cau hinh dataset: {DATA_CONFIG}")
    if not BASE_MODEL.is_file():
        raise FileNotFoundError(
            f"Khong tim thay trong so goc: {BASE_MODEL}. "
            "Hay dat yolov8n.pt vao thu muc models."
        )

    model = YOLO(str(BASE_MODEL))
    model.train(
        data=str(DATA_CONFIG),
        epochs=100,
        imgsz=640,
        batch=-1,
        patience=20,
        project=str(RUNS_DIR),
        name="waste_classifier",
        exist_ok=True,
        pretrained=True,
    )


if __name__ == "__main__":
    main()
