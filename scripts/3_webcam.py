import argparse
from pathlib import Path

import cv2
from ultralytics import YOLO


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT_DIR / "models" / "best.pt"


def main() -> None:
    parser = argparse.ArgumentParser(description="Nhan dien rac realtime bang webcam")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--camera", type=int, default=0)
    parser.add_argument("--conf", type=float, default=0.35)
    args = parser.parse_args()

    if not args.model.is_file():
        raise FileNotFoundError(f"Khong tim thay model: {args.model}")

    model = YOLO(str(args.model))
    camera = cv2.VideoCapture(args.camera)
    if not camera.isOpened():
        raise RuntimeError(f"Khong the mo webcam so {args.camera}")

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                raise RuntimeError("Khong doc duoc khung hinh tu webcam")

            result = model.predict(frame, conf=args.conf, verbose=False)[0]
            cv2.imshow("YOLO - Phan loai rac", result.plot())
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
