from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, QPoint
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtW
import sys
import cv2

from .parameters import *

class MainWindow(QtW.QWidget):
    # constructor
    def __init__(self, parent=None):
        super().__init__(parent)

        # default size
        self.size = radius # pixels
        self.zoom = zoom # zoom factor to crop webcam image
        
        # define window size and title
        self.resize(self.size, self.size)
        self.setWindowTitle("Cameo")
        
        # remove window frames
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # make window transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # make window always on top
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        
        # draw a label in the middle of the window
        self.label = QtW.QLabel(self)
        self.label.resize(self.size, self.size)
        
        # init webcam
        self.cap = cv2.VideoCapture(webcam)
        
        # timer to update window
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(interval)
        
        # store position
        self.oldPos = self.pos()

    # override closeEvent method
    def closeEvent(self, event):
        self.cap.release()
        cv2.destroyAllWindows()
        event.accept()

    # override mousePressEvent method    
    def mousePressEvent(self, event):
        # close window on mouse right click
        if event.button() == QtCore.Qt.RightButton:
            self.close()
        # update pos
        self.oldPos = event.globalPos()
        
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # override mouse scroll event
    def wheelEvent(self, event):
        # if shift is pressed
        if event.modifiers() == QtCore.Qt.ShiftModifier:
            deltaZoom = 10
            deltaWindow = 0
        else:
            deltaZoom = 0
            deltaWindow = 10       

        # change window size on scrool
        if event.angleDelta().y() > 0:
            self.size += deltaWindow
            self.zoom += deltaZoom
        else:
            self.size -= deltaWindow
            self.zoom -= deltaZoom
            
        self.resize(self.size, self.size)
        self.label.resize(self.size, self.size)

    # update window
    def updateFrame(self):
        # draw image from webcam
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            
            # convert to ARGB with alpha channel
            img.convertToFormat(QImage.Format_ARGB32)
            
            # make it square
            imgsize = min(img.width(), img.height())
            x0 = (img.width()  - imgsize) // 2 + self.zoom
            y0 = (img.height() - imgsize) // 2 + self.zoom
            imgsize -= self.zoom * 2
            rect = QRect(x0, y0, imgsize, imgsize)
            img = img.copy(rect)
            
            # new image, init transparent
            out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32) 
            out_img.fill(QtCore.Qt.transparent)
            
            # mask
            brush = QtGui.QBrush(img) 
            painter = QtGui.QPainter(out_img) 
            painter.setBrush(brush) 
            painter.setPen(QtCore.Qt.NoPen) 
            painter.drawEllipse(0, 0, imgsize,imgsize)
            painter.end()
            
            # add image to label
            pix = QPixmap.fromImage(out_img)
            self.label.setPixmap(pix)
            self.label.setScaledContents(True)
            # center label
            self.label.setAlignment(QtCore.Qt.AlignCenter)

def main():
    global webcam
    # capture input arguments
    args = sys.argv[1:]
    
    # check if --help
    if "--help" in args:
        print("Usage: cameo [options]")
        print("Options:")
        print("  --help       Display this information")
        print("  --webcam     Set webcam index (default 0), usually even numbers only: 0, 2, 4...")
        sys.exit(0)
    
    # check if --webcam
    if "--webcam" in args:
        # get webcam index
        webcam = args[args.index("--webcam") + 1]
        webcam = int(webcam)
        

    # create and run application
    app = QtW.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
