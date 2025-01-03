import sys
from PyQtWidgets import QApplication, QmainWindow, QLabel
def main():
  app = QApplication(sys.argv)
  window = QMainWindow()
  window.setWindowTitle("Simple PyQt Example")
  window.set.Geometry(100,100,400,200)
  label = QLabel("Hello World",window)
  lebel.move(150,80)
  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()
