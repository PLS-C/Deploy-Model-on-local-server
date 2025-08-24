from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import torch
from ultralytics import YOLO
import cv2
import os
import sympy as sp

# Load a model
#model = YOLO("yolo11n-pose.pt")  # load an official model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = YOLO("yolo11n.pt").to(device)

# Specify a custom folder files
template_folder = os.path.join(os.getcwd(), 'files')
app = Flask(__name__, template_folder=template_folder)
#app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def serve_file():
    # Render and serve the HTML file directly from the html-files
    return render_template('index.html')

@app.route('/webcam')
def webcam():
    # Render and serve the HTML file directly from the html-files
    return render_template('webcam.html')
    
@app.route('/js/opencv.js')
def opencv_js():
    # Render and serve the HTML file directly from the html-files
    return render_template('js/opencv.js')

@app.route('/predicted_web', methods=['POST'])
def predicted_web():
    data = request.get_json()
    name_data = data['Name']
    instances_data = data['instances']
    numpy_array = np.array(instances_data, dtype=np.float32)
    tensor_data = torch.from_numpy(numpy_array)  # shape: (1, 3, H, W)
    
    # Move to GPU if available
    if torch.cuda.is_available():
        tensor_data = tensor_data.to("cuda")
        
    # Run YOLO inference
    results = model(tensor_data)  # predict on an image
    result = results[0]
    
    # Extract detection components
    boxes = result.boxes.xyxy
    cls_indices = result.boxes.cls
    names = result.names
    scores = result.boxes.conf

    # Filter: only keep detections with score > 0.5
    mask = scores > 0.5
    filtered_boxes = boxes[mask].int().tolist()
    filtered_scores = scores[mask].tolist()
    filtered_classes = cls_indices[mask].tolist()
    filtered_names = [names[i] for i in filtered_classes]
    
    return jsonify({"status": "success", 
                "bbox": filtered_boxes,
                "class": filtered_names,
                "scores": filtered_scores}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
