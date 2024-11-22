from ultralytics import YOLO

# Load a model
model = YOLO("best_v11_l.pt")  # load a custom trained model

# Export the model
model.export(format="onnx")
#model.export(format="openvino")  # creates 'yolov8n_openvino_model/'
#model.export(format="engine")  # creates 'yolov8n.engine'
