from Chuong1_Ham.baitap21.ui.MainWindow21 import Ui_MainWindow

class MainWindow21Ext(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonThucHien.clicked.connect(self.tinhtoan)
    def tinhtoan (self):
        def giaithua(n):
            if n==0: return 1
            else: return n * giaithua(n-1)
        def A(n, k):
            return giaithua(n) / giaithua(n - k)
        def C(n, k):
            return giaithua(n) / (giaithua(n - k) * giaithua(k))

        n = int(self.lineEditN.text())
        k = int(self.lineEditK.text())
        ansA = int(A(n, k))
        ansC = int(C(n, k))
        self.lineEditA.setText(str(ansA))
        self.lineEditC.setText(str(ansC))

    def showWindow(self):
        self.MainWindow.show()
