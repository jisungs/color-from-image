from flask import Flask, render_template, redirect, url_for, request
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='static/uploads/'

@app.route('/')
def index():
    return render_template(['index.html'])

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return request(url_for('index'))
    
    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('show_colors', filename=file.filename))

def extract_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.resize((100,100))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    result = result.convert('RGB')
    main_colors = result.getcolors(100*100)

    return [color[1] for color in main_colors]


@app.route('/colors/<filename>')
def show_colors(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    colors = extract_colors(filepath)
    print(colors)
    return render_template('colors.html', filename=filename, colors=colors)



if __name__ == '__main__':
    app.run(debug=True, port=5002)