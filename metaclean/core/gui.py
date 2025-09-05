import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QListWidget, QListWidgetItem


class MetaClean(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.filenames = []
        
        self.setWindowTitle("MetaClean")
        self.setMinimumSize(QSize(400, 300))
        
        self.setup_ui()
        
    def setup_ui(self):
        layoutH = QHBoxLayout()
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()

        layoutH.setSpacing(20)

        # add widgets
        self.file_list = QListWidget()
        layoutV1.addWidget(self.file_list)

        button = QPushButton("Add Images")
        button.clicked.connect(self.add_files)
        layoutV1.addWidget(button, alignment=Qt.AlignBottom)

        layoutH.addLayout(layoutV1, 1)
        layoutH.addLayout(layoutV2, 1)

        container = QWidget()
        container.setLayout(layoutH)

        self.setCentralWidget(container)
        
    def add_files(self):
        dlg = QFileDialog(self)
        dlg.setFileMode(QFileDialog.ExistingFiles)
        dlg.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if dlg.exec_():
            for filepath in dlg.selectedFiles():
                new_item = QListWidgetItem(filepath)
                self.file_list.addItem(new_item)
