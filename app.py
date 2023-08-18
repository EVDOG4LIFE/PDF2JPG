import os
import logging
from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import pdf2image
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/uploads'
app.config['OUTPUT_FOLDER'] = '/tmp/output'
metrics = PrometheusMetrics(app)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            files = request.files.getlist('file')
            if not files or not all(f.filename.endswith('.pdf') for f in files):
                logger.error('Invalid file type uploaded.')
                return jsonify({"error": "Invalid file type. Please upload a PDF."}), 400

            output_filepaths = []
            for file in files:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                images = pdf2image.convert_from_path(filepath)
                for i, image in enumerate(images):
                    out_path = os.path.join(app.config['OUTPUT_FOLDER'], f"{filename}_page_{i + 1}.jpg")
                    image.save(out_path, 'JPEG')
                    output_filepaths.append(out_path)

            return jsonify({"files": [os.path.split(f)[-1] for f in output_filepaths]})

        except Exception as e:
            logger.error(f"Error processing file: {str(e)}")
            return jsonify({"error": "Error processing file. Please try again later."}), 500

    return render_template('upload.html')

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
