from select import select
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os, sys
from PyQt5.QtGui import *
from PIL import ImageEnhance
from random import randint
app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Easy edit')
main_win.resize(900,759)
main_layout = QHBoxLayout()             #Главный
layout1=QVBoxLayout()                   #Лево
layout2=QVBoxLayout()                   #Право
layout3=QVBoxLayout()                   #
layout4=QHBoxLayout()                   #Кнопки стандарт
layout5=QHBoxLayout()                   #
selected = 0
jkl = []
allim = []
p = os.path.abspath('')
class Imyg():
    def __init__(self, name):
        self.name = name
        self.image = QImage(os.path.join(folder, self.name))
        self.first = 1
    def shows(self):
        image.setPixmap(QPixmap.fromImage(self.image))
    def newshows(self):
        global selected
        self.newname = str(randint(1,999999999999)) + '.png'
        self.newimage.save(self.newname)
        os.replace(self.newname, os.path.join(papka, self.newname))
        self.newimage = QImage(os.path.join(papka, self.newname))
        image.setPixmap(QPixmap.fromImage(self.newimage))
        allim.append(Imyg(self.newname))
        selected = self.newname
    def detects(self):
        if self.first == 1:
            self.namus = self.name
            self.folder = folder
        else:
            self.folder = papka
            self.namus = self.newname
    def vbs(self):
        with Image.open(os.path.join(self.folder, self.namus)) as original:
            self.newimage = original.convert('L')
        self.first = 2
    def lefts(self):
        with Image.open(os.path.join(self.folder, self.namus)) as original:
            self.newimage = original.transpose(Image.ROTATE_90)
        self.first = 2
    def rights(self):
        with Image.open(os.path.join(self.folder, self.namus)) as original:
            self.newimage = original.transpose(Image.ROTATE_270)
        self.first = 2
    def kons(self):
        with Image.open(os.path.join(self.folder, self.namus)) as original:
            self.newimage = original.filter(ImageFilter.SHARPEN)
        self.first = 2
    def mirrors(self):
        with Image.open(os.path.join(self.folder, self.namus)) as original:
            self.newimage = original.transpose(Image.FLIP_LEFT_RIGHT)
        self.first = 2
def show():
    selected = list.selectedItems()[0].text()
    for i in allim:
        if selected == i.name:
            i.shows()
            i.first = 1
def vb():
    selected = list.selectedItems()[0].text()
    for i in allim:
        if selected == i.name:
            i.detects()
            i.vbs()
            i.newshows()
def left():
    selected = list.selectedItems()[0].text()
    for i in allim:
        if selected == i.name:
            i.detects()
            i.lefts()
            i.newshows()
def right():
    selected = list.selectedItems()[0].text()
    for i in allim:
        if selected == i.name:
            i.detects()
            i.rights()
            i.newshows()
def kon():
    selected = list.selectedItems()[0].text()
    for i in allim:
        if selected == i.name:
            i.detects()
            i.kons()
            i.newshows()
def mirror():
    selected = list.selectedItems()[0].text()
    for i in allim:
        if selected == i.name:
            i.detects()
            i.mirrors()
            i.newshows()
def modifid():
    global papka
    papka = os.path.join(p, 'Modified')
    if os.path.exists(papka):
        pass
    else:
        os.mkdir(papka)
        modifid()
def dir():
    global folder
    folder = QFileDialog.getExistingDirectory()
    data = os.listdir(os.path.join(sys.path[0], folder))
    list.clear()
    for i in data:
        if i.endswith('.png'):
            with Image.open(os.path.join(folder, i)) as original:
                imagepath = os.path.abspath(i)
                original = original.convert('RGBA')
                original.save(i)
                data = os.listdir(os.path.join(sys.path[0], folder))
                list.addItem(i)
                allim.append(Imyg(i))
        if i.endswith('.jpg'):
            with Image.open(os.path.join(folder, i)) as original:
                imagepath = os.path.abspath(i)
                original = original.convert('RGBA')
                lenys = len(i)
                name =  i[:lenys-4] + '.png'
                original.save(name)
                data = os.listdir(os.path.join(sys.path[0], folder))
                list.addItem(name)
                allim.append(Imyg(name))
                os.remove(imagepath)
    modifid()
button1 = QPushButton('Папка')
button2 = QPushButton('Лево')
button3 = QPushButton('Право')
button4 = QPushButton('Зеркало')
button5 = QPushButton('Резкость')
button6 = QPushButton('Ч/Б')
list = QListWidget()
image = QLabel('Картинка') 
layout1.addWidget(button1)
layout1.addWidget(list)
layout2.addWidget(image)
layout4.addWidget(button2)
layout4.addWidget(button3)
layout4.addWidget(button4)
layout4.addWidget(button5)
layout4.addWidget(button6)
layout2.addLayout(layout4)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
image.setAlignment(Qt.AlignCenter)
list.itemClicked.connect(show)
button1.clicked.connect(dir)
button6.clicked.connect(vb)
button2.clicked.connect(left)
button3.clicked.connect(right)
button5.clicked.connect(kon)
button4.clicked.connect(mirror)
main_win.setLayout(main_layout) 
main_win.show() 
app.exec_()