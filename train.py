from ultralytics import YOLO

# Load a model
model = YOLO('yolov11n.pt')  # load a pretrained model (recommended for training)

# Train the model
if __name__ == '__main__':
    results = model.train(data='data/dataset.yaml', epochs=100, imgsz=640)
