import os

from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import *

from PIL import Image, ImageEnhance, ImageFilter

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

app = QApplication([])


window = QWidget()
window.resize(600, 400)


main_line = QHBoxLayout()


left_line = QVBoxLayout()


folders_btn = QPushButton("Папка")
left_line.addWidget(folders_btn)


file_list = QListWidget()
file_list.addItems(["bright.png", "field.png", "trees.png", "villiage.png"])
left_line.addWidget(file_list)

v1_line = QVBoxLayout()
img_lbl = QLabel()
v1_line.addWidget(img_lbl)

btn_layout = QHBoxLayout()


left_btn = QPushButton("Вліво")
right_btn = QPushButton("Вправо")
mirror_btn = QPushButton("Дзеркало")
sharp_btn = QPushButton("Різкість")
bw_btn = QPushButton("Ч/Б")


btn_layout.addWidget(left_btn)
btn_layout.addWidget(right_btn)
btn_layout.addWidget(mirror_btn)
btn_layout.addWidget(sharp_btn)
btn_layout.addWidget(bw_btn)


v1_line.addLayout(btn_layout)


main_line.addLayout(left_line)
main_line.addLayout(v1_line)

class ImageProcessor:
    def __init__(self):
        self.folder = ""
        self.filename = ""
        self.image = ""
    def load(self):
        img_path = os.path.join(self.folder, self.filename)
        self.image = Image.open(img_path)
    def show(self):
        pix = pil2pixmap(self.image)
        pix= pix.scaledToWidth(500)
        img_lbl.setPixmap(pix)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.show()

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.show()

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.show()

    def sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.show()

    def black_or_white(self):
        self.image = self.image.convert("L")
        self.show()

ip = ImageProcessor()
ip.filename = "img.jpg"
ip.load()
ip.show()
def open_folder():
    ip.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(ip.folder)
    file_list.clear()
    for file in files:
        if file.endswith(".jpg"):
            file_list.addItem(file)


def show_chosen_image():
    ip.filename= img_lbl.currentItem().text()
    ip.load()
    ip.show()

bw_btn.clicked.connect(black_or_white)
sharp_btn.clicked.connect(ip.sharp)
mirror_btn.clicked.connect(ip.mirror)
right_btn.clicked.connect(ip.rotate_right)
left_btn.clicked.connect(ip.rotate_left)
file_list.currentRowChanged.connect(show_chosen_image)
folders_btn.clicked.connect(open_folder)
window.setLayout(main_line)
window.show()
app.exec()



