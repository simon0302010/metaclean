import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget


class MetaClean(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.filenames = []
        
        self.setWindowTitle("MetaClean")
        self.setMinimumSize(QSize(400, 300))
        
        self.show_start()
        
    def show_start(self):
        label = QLabel("Select image files to remove their metadata.")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Select Images")
        button.clicked.connect(self.open_file)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(label)
        layout.addWidget(button, alignment=Qt.AlignCenter)
        layout.addStretch()

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        
    def open_file(self):
        dlg = QFileDialog(self)
        dlg.setFileMode(QFileDialog.ExistingFiles)
        dlg.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if dlg.exec_():
            self.filenames = dlg.selectedFiles()