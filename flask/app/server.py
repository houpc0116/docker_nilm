import json, jsonify
import requests
import os

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from pathlib import Path
from PIL import Image
#from flask_uploads import UploadSet, IMAGES, configure_uploads
#from PIL import Image

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello():
	return "Hello World!"

## 上傳檔案
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file:
        	# 儲存原始圖片
            filename = file.filename
            filepath = '/app/static/uploads/'+filename
            #print(filename)
            file.save(filepath)
            # 縮放圖片
            fileSplitName =filename.split('.')
            scaled_path ='/app/static/uploads/thumb/'+fileSplitName[0]+'.gif'
            scaled_size = (800, 600)
            image = Image.open(file)
            image.thumbnail(scaled_size)
            image.save(scaled_path, 'GIF')
            #file.save( os.path.join(current_directory, filename) )
            return 'File uploaded successfully.'
    return render_template('upload.html')

#if __name__ == '__main__':
	#app.run(host='0.0.0.0')
