from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication([])


window = QWidget()
window.setWindowTitle("Easy Editor")
window.resize(600, 400)


main_line = QHBoxLayout(window)


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


window.setLayout(main_line)


window.show()
app.exec()



