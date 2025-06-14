from flask import Flask, request, jsonify, render_template, send_from_directory, send_file
from flask_cors import CORS
import numpy as np
import torch
from ultralytics import YOLO
import cv2
import os
import io

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# Load a COCO-pretrained YOLO11n model
model = YOLO("models/yolo11n.pt")
model.to(device)

# Specify a custom folder files
template_folder = os.path.join(os.getcwd(), 'files')
app = Flask(__name__, template_folder=template_folder)
#app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/test')
def test():
    return jsonify({"status": "success"}), 200

@app.route('/css/js_example_style.css')
def js_example_style():
    # Render and serve the HTML file directly from the html-files
    return render_template('css/js_example_style.css')
    
@app.route('/js/jquery-3.6.0.min.js')
def jquery_js():
    # Render and serve the HTML file directly from the html-files
    return render_template('js/jquery-3.6.0.min.js')

@app.route('/app1')
def app1():
    return render_template('app1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    #Run YOLO prediction
    results = model(img)
    # Get prediction results (bounding boxes, labels, confidence)
    bbox_predicted = results[0].boxes
    class_names = results[0].names
    for data in bbox_predicted:
        class_name = class_names[data.cls.item()]
        class_conf = data.conf.item()
        xyxy_box = data.xyxy.cpu().tolist()[0]
        xmin, ymin, xmax, ymax = xyxy_box
        # Draw rectangle
        cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
        # Draw label text
        cv2.putText(img, class_name, (int(xmin), int(ymin) - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    success, img_encoded = cv2.imencode('.jpg', img)
    if not success:
        raise ValueError("Image encoding failed.")
    return send_file(
        io.BytesIO(img_encoded.tobytes()),
        mimetype='image/jpeg',
        as_attachment=False
    )
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
