from ultralytics import YOLO

if __name__ == "__main__":
    # Load a pretrained YOLO model
    model = YOLO('yolov8l.pt')

    # Train the model
    results = model.train(data='data.yaml', epochs=25, imgsz=640,
                          task='detect', device='cpu', patience=50, name='yolov8_fruits_detection',
                          workers=4, batch=8)

    # Evaluate the model's performance on the validation set
    results = model.val()
