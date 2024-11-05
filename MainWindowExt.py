from PTB1.MainWindow import Ui_MainWindow

class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonSolve.clicked.connect(self.process_solution)
    def process_solution(self):
        try:
            a=float(self.lineEditA.text())
            b=float(self.lineEditB.text())
            if a==0 and b==0:
                self.labelResult.setText("Infinity Solution")
            elif a==0 and b!=0:
                self.labelResult.setText("No Solution")
            else:
                self.labelResult.setText(f"x={-b/a}")
            self.labelResult.setStyleSheet("Color:blue;background-color:cyan")
        except:
            self.labelResult.setText("Invalid input data")
            self.labelResult.setStyleSheet("Color:red;background-color:cyan")