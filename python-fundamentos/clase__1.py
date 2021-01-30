#interface
import sys
from PyQt4 import  QtGui 
 
 
class ventanaprincipal(QtGui.QMainWindow):
    def __init__(self):
        super(ventanaprincipal, self).__init__()
 
        self.setWindowTitle("Edward Figueroa Maldonado")

app=QtGui.QApplication(sys.argv)
ventanita=ventanaprincipal()
ventanita.show()
sys.exit(app.exec_())
