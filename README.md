# YOLO11 Object Detection Training

This project is set up to train a YOLO11 model for object detection.

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

## Docker

You can also run this project using Docker.

1.  **Build the Docker image:**

    ```bash
    docker build -t cartes-yolo .
    ```

2. **Run the Docker container:**

    To train the model inside the container, you need to mount your local `data/` and `runs/` directories so that the container can access your dataset and save the training results.

    ```bash
    docker run -it --rm \
      -v "$(pwd)/data:/app/data" \
      -v "$(pwd)/runs:/app/runs" \
      cartes-yolo \
      --data data/dataset.yaml --epochs 100 --imgsz 640 --project runs/train --name train
    ```

    You can customize the arguments passed to `train.py` (e.g., `--epochs`, `--imgsz`, `--name`) as needed.

    ### Example: Running with results in a local `tmp` folder

    To direct the training results to a local `tmp` folder instead of `runs`, you can use the following command. This command mounts your local `data` directory to `/data` inside the container and your local `tmp` directory to `/app/runs` inside the container, which is where the training script will write its output.

    ```bash
    docker run -it --rm \
      -v "$(pwd)/data:/data" \
      -v "$(pwd)/tmp:/app/runs" \
      cartes-yolo \
      --epochs=1 --data=/data/dataset.yaml
    ```





