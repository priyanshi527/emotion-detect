import os
from flask import Flask, request, render_template, send_from_directory, redirect,url_for, Response
from fer import FER
import matplotlib.pyplot as plt 
import base64

a={'angry': '😠','disgust': '🤢', 'fear': '😱', 'happy':'😁', 'sad': '☹️', 'surprise': '😮', 'neutral' : '😐'}
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
        #print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        #print("{} is the file name".format(upload.filename))
        
        filename = upload.filename
        destination = "/".join([target, filename])
        upload.save(destination)
 

    folder='images'
    ex=folder+'/'+filename
    img = plt.imread(ex)
    detector = FER(mtcnn=True)
    emotion, score = detector.top_emotion(img)
    ans = a[emotion]
      
    return render_template("complete_display_image.html",image_name=ex,text=ans)

    
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


if __name__ == "__main__":
    app.run(debug=True)