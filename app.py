from flask import Flask, render_template
import random

app = Flask(__name__)

# list of images
images = [
    "photo-1472457847783-3d10540b03d7.jpeg",
    "photo-1472457897821-70d3819a0e24.jpeg",
    "photo-1472457974886-0ebcd59440cc.jpeg",
    "photo-1484656551321-a1161420a2a0.jpeg",
    "photo-1484824823018-c36f00489002.jpeg",
    "photo-1518331368925-fd8d678778e0.jpeg",
    "photo-1518331483807-f6adb0e1ad23.jpeg",
    "photo-1544816565-aa8c1166648f.jpeg",
    "photo-1547700055-b61cacebece9.jpeg",
    "photo-1558492426-df14e290aefa.jpeg"
]

@app.route('/')
def index():
    f=open("/etc/os-release", "r").read()
    url = random.choice(images)
    return render_template('index.html', url=url, f=f)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
