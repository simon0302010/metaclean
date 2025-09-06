from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QListWidget,
    QListWidgetItem,
)

class MetaClean(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.filenames = []
        
        self.setWindowTitle("MetaClean")
        self.setMinimumSize(QSize(550, 400))
        
        self.setup_ui()
        
    def setup_ui(self):
        layoutV0 = QVBoxLayout()
        layoutH = QHBoxLayout()
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()

        layoutH.setSpacing(10)

        description = QLabel("Select images and choose metadata to remove")
        layoutV0.addWidget(description, alignment=Qt.AlignCenter)

        # add widgets
        self.file_list = QListWidget()
        layoutV1.addWidget(self.file_list)

        # add buttons
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add Images")
        add_button.clicked.connect(self.add_files)
        remove_button = QPushButton("Remove selected")
        remove_button.clicked.connect(self.remove_selected)

        button_layout.addWidget(add_button)
        button_layout.addWidget(remove_button)
        
        # ensure buttons are the same size
        max_width = max(add_button.sizeHint().width(), remove_button.sizeHint().width())
        add_button.setMinimumWidth(max_width)
        remove_button.setMinimumWidth(max_width)

        layoutV1.addLayout(button_layout)

        continue_button = QPushButton("Continue")
        layoutV2.addWidget(continue_button, alignment=Qt.AlignBottom)

        layoutH.addLayout(layoutV1, 1)
        layoutH.addLayout(layoutV2, 1)

        layoutV0.addLayout(layoutH)

        container = QWidget()
        container.setLayout(layoutV0)

        self.setCentralWidget(container)
        
    def add_files(self):
        dlg = QFileDialog(self)
        dlg.setFileMode(QFileDialog.ExistingFiles)
        dlg.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if dlg.exec_():
            for filepath in dlg.selectedFiles():
                if filepath not in self.filenames:
                    new_item = QListWidgetItem(filepath)
                    self.file_list.addItem(new_item)
                    self.filenames.append(filepath)

    def remove_selected(self):
        for item in self.file_list.selectedItems():
            self.filenames.remove(item.text())
            self.file_list.takeItem(self.file_list.row(item))