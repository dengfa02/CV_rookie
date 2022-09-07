import torch


# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img = '/Users/GongLi/Documents/JetBrains/yolov5/data/images/bus.jpg'

# Inference
results = model(img, size=640)  # includes NMS

# Results
results.show()
