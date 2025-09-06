import sys
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