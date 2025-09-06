from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt, pyqtSignal
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

class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    
    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

class PreviewWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Image Preview")
        
        layout = QVBoxLayout()
        image_label = ClickableLabel()
        image_preview = QPixmap(image_path)
        image_preview = image_preview.scaled(
            400, image_preview.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        image_label.setPixmap(image_preview)
        image_label.clicked.connect(self.close)
        layout.addWidget(image_label)
        
        self.setLayout(layout)

class MetaClean(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.filenames = []
        self.preview_windows = []
        
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
        self.file_list.itemDoubleClicked.connect(self.image_preview)
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
        continue_button.clicked.connect(self.process_images)
        layoutV2.addWidget(continue_button, alignment=Qt.AlignBottom)

        layoutH.addLayout(layoutV1, 1)
        layoutH.addLayout(layoutV2, 1)

        layoutV0.addLayout(layoutH)

        container = QWidget()
        container.setLayout(layoutV0)

        self.setCentralWidget(container)
        
    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Images", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        for file in files:
            if file not in self.filenames:
                self.filenames.append(file)
                item = QListWidgetItem()
                pixmap = QPixmap(file)
                if not pixmap.isNull():
                    icon = QIcon(pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                    item.setIcon(icon)
                item.setText(file)
                self.file_list.addItem(item)

    def remove_selected(self):
        for item in self.file_list.selectedItems():
            self.filenames.remove(item.text())
            self.file_list.takeItem(self.file_list.row(item))

    def image_preview(self, item):
        preview = PreviewWindow(item.text())
        preview.show()
        self.preview_windows.append(preview)

    def process_images(self):
        print(self.filenames)