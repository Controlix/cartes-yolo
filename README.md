# YOLOv11 Object Detection Training

This project is set up to train a YOLOv11 model for object detection.

## Setup

1. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your data:**
   - Place your training images in `data/images/train`
   - Place your validation images in `data/images/val`
   - Place your training labels in `data/labels/train`
   - Place your validation labels in `data/labels/val`

   The label files should be in YOLO format (txt files with one line per bounding box: `class_id center_x center_y width height`).

4. **Update `data/dataset.yaml`:**
   - Change the `names` list to match the classes in your dataset.

## Training

To start training the model, make sure your virtual environment is activated and run the following command:

```bash
python train.py
```

The training results, including saved model weights, will be stored in the `runs/` directory.
