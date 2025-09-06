import sys
import importlib.resources

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

from .core import (
    gui, process, exiftool
)


def process_images(filenames, selected_options):
    process.process_images(filenames, selected_options)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("MetaClean")
    app.setApplicationDisplayName("MetaClean")
    
    with importlib.resources.path("metaclean.assets", "icon128.png") as icon_path:
        app.setWindowIcon(QIcon(str(icon_path)))
    
    if exiftool.check_installed():        
        window = gui.MetaClean(process_images=process_images)
        window.show()
        
        app.exec()
    else:
        print("\033[31mPlease install ExifTool before running this program.\033[0m")
        QMessageBox.critical(
            None,
            "ExifTool Not Found",
            "Please install ExifTool before running this program."
        )
        sys.exit(1)
    
if __name__ == "__main__":
    main()