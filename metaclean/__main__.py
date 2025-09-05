import sys
from PyQt5.QtWidgets import QApplication
from .core import gui


def main():
    app = QApplication(sys.argv)
    
    window = gui.MetaClean()
    window.show()
    
    app.exec()
    
if __name__ == "__main__":
    main()