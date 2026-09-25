# YOLO Phan Loai Rac

Bo khung de tai: **Tim hieu mo hinh YOLO va ung dung trong bai toan phan loai rac**.

## Cau truc

```text
dataset/
	images/train/       # Anh huan luyen
	images/val/         # Anh danh gia
	labels/train/       # Nhan YOLO tuong ung voi images/train
	labels/val/         # Nhan YOLO tuong ung voi images/val
	data.yaml           # Cau hinh 5 lop
models/
	yolov8n.pt          # Trong so goc, tu tai ve
	best.pt             # Trong so tot nhat sau khi huan luyen
scripts/
	1_train.py
	2_test_image.py
	3_webcam.py
test_images/
runs/                 # Ket qua do Ultralytics sinh ra
```

## Cai dat

Nen dung Python 3.9-3.12 va tao moi truong ao:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Dat file `yolov8n.pt` vao `models/`. Ultralytics cung co the tu tai file nay khi khoi tao model bang ten, nhung dat san vao thu muc `models/` giup du an reproducible hon.

## Chuan bi dataset

Moi anh can co mot file nhan cung ten, vi du:

```text
dataset/images/train/anh_001.jpg
dataset/labels/train/anh_001.txt
```

Moi dong trong file `.txt` co dang:

```text
class_id x_center y_center width height
```

Toa do phai duoc chuan hoa trong khoang 0-1. Class id trong cau hinh hien tai la:

```text
0 nhua | 1 thuy_tinh | 2 kim_loai | 3 giay | 4 rac_huu_co
```

## Chay

Huan luyen:

```powershell
python scripts/1_train.py
```

Sau khi huan luyen, copy hoac doi ten trong so tot nhat vao `models/best.pt`, sau do test mot anh:

```powershell
python scripts/2_test_image.py --image test_images/test1.jpg
```

Co the chi ro model va nguong tin cay:

```powershell
python scripts/2_test_image.py --model models/best.pt --conf 0.4
```

Nhan dien realtime bang webcam. Nhan `q` de thoat:

```powershell
python scripts/3_webcam.py
```

## Luu y ve nhan

Day la bai toan **object detection**, khong chi la classification anh. Vi vay moi vat the rac trong anh phai co bounding box va nhan YOLO tuong ung. Nen chia du lieu theo ty le khoang 80/20, giu cac lop xuat hien o ca tap train va val, va kiem tra anh cung file nhan truoc khi train.