from PyQt6.QtWidgets import QMainWindow,QApplication

from PTB1.MainWindowExt import MainWindowExt

app=QApplication([])
mainWindow=QMainWindow()
myui=MainWindowExt()
myui.setupUi(mainWindow)
myui.showWindow()
app.exec()