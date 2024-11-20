#imports

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

#App settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(250, 300)

#All objects/widgets

text_box = QLineEdit()
grid = QGridLayout()


#Design




#Show/Run
main_window.show()
app.exec_()
