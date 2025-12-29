from ultralytics import YOLO
import argparse

# Load a model
model = YOLO('yolo11s.pt')  # load a pretrained model (recommended for training)

# Train the model
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='data/dataset.yaml', help='path to dataset.yaml')
    parser.add_argument('--epochs', type=int, default=100, help='number of epochs')
    parser.add_argument('--imgsz', type=int, default=640, help='image size')
    parser.add_argument('--project', type=str, default='runs/train', help='project name')
    parser.add_argument('--name', type=str, default='train', help='experiment name')
    parser.add_argument('--batch', type=int, default=16, help='batch size')
    opt = parser.parse_args()
    results = model.train(data=opt.data, epochs=opt.epochs, imgsz=opt.imgsz, project=opt.project, name=opt.name, batch=opt.batch, cache=True)
