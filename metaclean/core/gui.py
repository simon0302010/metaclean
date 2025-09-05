import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel


class MetaClean(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("MetaClean")
        self.setMinimumSize(QSize(400, 300))
        
        self.show_start()
        
    def show_start(self):
        button = QPushButton("Select Files")
        
        self.setCentralWidget(button)