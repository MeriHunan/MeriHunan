from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QProgressBar, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
import os, re
from PyQt5 import QtCore


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)
    
class InfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.progressBars = []
        self.dataExists = False
        for i in range(10):#            Creating 10 hidden progress bars
            progress = QProgressBar()
            progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
            progress.setVisible(False)
            layout.addWidget(progress)
            self.progressBars.append(progress)   #Storing the progress bars
        layout.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(layout)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)

    def sizeHint(self):
        if self.dataExists:
            return QSize(200, 100)
        return QSize(0, 100)

    def setInfo(self, indexes, class_names, prediction):
        self.dataExists = True
        for progress in self.progressBars:
            progress.setVisible(False)

        predicitons = []
        for i in indexes[0]:
            class_name = class_names[i]
            class_name = re.sub(r'\d+', '', class_name).strip()
            confidence_score = int(prediction[0][i] * 100)
            predicitons.append((class_name, confidence_score))
        
        predicitons.sort(key=lambda x:x[1], reverse=True)
        idx = 0
        for name, percent in predicitons:
            self.progressBars[idx].setFormat(name + " %p%")
            self.progressBars[idx].setValue(percent)
            self.progressBars[idx].setVisible(True)
            idx += 1
            if idx == len(self.progressBars):
                break

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pixmap = None
        self.resize(600, 600)
        self.setAcceptDrops(True)

        mainLayout = QHBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        self.infoWidget = InfoWidget()
        mainLayout.addWidget(self.infoWidget)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.photoViewer.setSizePolicy(sizePolicy)

        self.setLayout(mainLayout)

    def resizeEvent(self, event):
        if self.pixmap is not None:
            self.set_image(self.pixmap)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            # Disable scientific notation for clarity
            np.set_printoptions(suppress=True)

            # Load the model
            model = load_model("Rock_AI_stuff_tenser\\keras_model.h5", compile=False)

            # Load the labels
            class_names = open("Rock_AI_stuff_tenser\labels.txt", "r").readlines()

            # Create the array of the right shape to feed into the keras model
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            # Above the line below is the first half of model
            image = Image.open(f"{file_path}").convert("RGB")
            # Below the line above is the second half of model
            pixmap = QPixmap(file_path)
            self.set_image(pixmap)


            # resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

            # turn the image into a numpy array
            image_array = np.asarray(image)

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # Predicts the model
            prediction = model.predict(data)
            print("This is prediction:")
     #       print(prediction)
            indexes = np.nonzero(prediction[0] > 0.10)
     #       print(indexs)
            #index = np.argmax(prediction)# This line took the highest out of predictions but I wanted 0.10 or above so I wrote the function above_10 to use instead of .arhmax
     #       for i in indexs[0]:
     #           class_name = class_names[i]
     #          confidence_score = prediction[0][i]

            # Print prediction and confidence score
#                print("Class:", class_name, end="")
#                print("Confidence Score:", confidence_score)
            self.infoWidget.setInfo(indexes, class_names, prediction)
            event.accept()
        else:
            event.ignore()

    def set_image(self, pixmap):
        self.pixmap = pixmap
        sz = self.photoViewer.size()
        pixmap_resized = self.pixmap.scaled(sz.width() - 20, sz.height() - 20, QtCore.Qt.KeepAspectRatio)
        self.photoViewer.setPixmap(pixmap_resized)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()


sys.exit(app.exec_())