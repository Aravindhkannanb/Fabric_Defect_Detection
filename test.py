from ultralytics import YOLO

# Load the YOLO11 model

# Export the model to ONNX format

# Load the exported ONNX model
onnx_model = YOLO("best_v11_l.pt")

# Run inference
results = onnx_model("test1.jpg")
results[0].show()