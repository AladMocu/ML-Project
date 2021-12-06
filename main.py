from PyQt5 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet
import random
import matplotlib
import numpy as np
import logic


matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1181, 591))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(40, -1, 40, -1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        pixmap = QtGui.QPixmap('./assets/iot.png')
        self.iot_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.iot_lbl.setObjectName("iot_lbl")
        self.iot_lbl.setPixmap(pixmap)
        self.iot_lbl.resize(pixmap.width(), pixmap.height())

        self.verticalLayout.addWidget(self.iot_lbl, alignment=QtCore.Qt.AlignCenter)
        self.iot_rad = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.iot_rad.setObjectName("iot_rad")
        self.iot_rad.setChecked(True)
        self.verticalLayout.addWidget(self.iot_rad)
        self.atk_rad = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atk_rad.sizePolicy().hasHeightForWidth())
        self.atk_rad.setSizePolicy(sizePolicy)
        self.atk_rad.setChecked(False)
        self.atk_rad.setObjectName("atk_rad")
        self.verticalLayout.addWidget(self.atk_rad)
        self.atk_field = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.atk_field.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.atk_field)



        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.execPackage = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.execPackage.setObjectName("execPachage")
        self.verticalLayout_2.addWidget(self.execPackage)
        self.arrow_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.arrow_lbl.setObjectName("arrow_lbl")
        self.verticalLayout_2.addWidget(self.arrow_lbl)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(40, -1, 40, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.CSM_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.CSM_label.setObjectName("CSM_label")

        pixmap2 = QtGui.QPixmap('./assets/shield.png')
        self.CSM_label.setPixmap(pixmap2)
        self.CSM_label.resize(pixmap.width(), pixmap.height())

        self.verticalLayout_3.addWidget(self.CSM_label, alignment=QtCore.Qt.AlignCenter)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.iot_rad.setText(_translate("MainWindow", "Reporte Dispositivo Normal"))
        self.atk_rad.setText(_translate("MainWindow", "Atacante"))
        self.execPackage.setText(_translate("MainWindow", "Enviar Simulacion Paquete"))
        self.arrow_lbl.setText(_translate("MainWindow", "{}"))
        self.plainTextEdit.setPlainText(logic.log)
        self.add_actions()

    def add_actions(self):
        arr = [
            "3478  >  3719 [FIN, ACK] Seq=1 Ack=1 Win=7936 Len=0 TSval=4121769948 TSecr=30459863",
            "22  >  50426 [ACK] Seq=1 Ack=22 Win=29056 Len=0 TSval=1844512794 TSecr=766030734",
            "22  >  50426 [ACK] Seq=1018 Ack=1382 Win=31872 Len=0 TSval=1844512894 TSecr=766030790",
            "22  >  50426 [ACK] Seq=1382 Ack=1490 Win=31872 Len=0 TSval=1844513002 TSecr=766030951",
            "22  >  50426 [ACK] Seq=2086 Ack=3462 Win=37504 Len=0 TSval=1844516994 TSecr=766034862",
            "[TCP Retransmission] 22  >  50426 [PSH, ACK] Seq=4654 Ack=4382 Win=40192 Len=196 TSval=1844522665 TSecr=766040474"
        ]
        self.execPackage.clicked.connect(lambda: self.classify(random.choice(arr) if self.iot_rad.isChecked() else
                                                               self.atk_field.text()))
        #"27000  >  50000 Len=4"

    def classify(self, trace):
        logic.classify(trace)
        self.arrow_lbl.setText("{" + str(trace) + "}")
        self.plainTextEdit.setPlainText(logic.log)


def draw():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProyectoFinal = QtWidgets.QMainWindow()
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    ui = Ui_MainWindow()
    ui.setupUi(ProyectoFinal)
    ProyectoFinal.show()
    sys.exit(app.exec_())

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    draw()
