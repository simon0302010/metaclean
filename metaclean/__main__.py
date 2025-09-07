import sys
import importlib.resources

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

from .core import (
    gui, process, exiftool
)


def process_images(filenames, selected_options, is_cancelled):
    return process.process_images(filenames, selected_options, is_cancelled)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("MetaClean")
    app.setApplicationDisplayName("MetaClean")
    
    icon_files = importlib.resources.files("metaclean.assets")
    icon_path = icon_files / "icon128.png"
    with importlib.resources.as_file(icon_path) as icon_file:
        app.setWindowIcon(QIcon(str(icon_file)))
    
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