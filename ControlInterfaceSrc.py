# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\qirun\OneDrive\Documents\Labs\Code\SyringePumpControl\ControlInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(30, 20, 501, 281))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.SyringeVolumeSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.SyringeVolumeSpinBox.setObjectName("SyringeVolumeSpinBox")
        self.horizontalLayout_5.addWidget(self.SyringeVolumeSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.SyringeInternalDiameterSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.SyringeInternalDiameterSpinBox.setObjectName("SyringeInternalDiameterSpinBox")
        self.horizontalLayout_6.addWidget(self.SyringeInternalDiameterSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.CalibrationSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.CalibrationSpinBox.setProperty("value", 1.0)
        self.CalibrationSpinBox.setObjectName("CalibrationSpinBox")
        self.horizontalLayout_4.addWidget(self.CalibrationSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.SavedLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.SavedLabel.setObjectName("SavedLabel")
        self.horizontalLayout_7.addWidget(self.SavedLabel)
        self.Step2ApplyButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.Step2ApplyButton.setObjectName("Step2ApplyButton")
        self.horizontalLayout_7.addWidget(self.Step2ApplyButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.ManualWithdrawButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ManualWithdrawButton.setObjectName("ManualWithdrawButton")
        self.horizontalLayout_13.addWidget(self.ManualWithdrawButton)
        self.ManualInfuseButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ManualInfuseButton.setObjectName("ManualInfuseButton")
        self.horizontalLayout_13.addWidget(self.ManualInfuseButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 2, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.VolumeDisplacementPerMicrostepLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.VolumeDisplacementPerMicrostepLabel.setObjectName("VolumeDisplacementPerMicrostepLabel")
        self.horizontalLayout_10.addWidget(self.VolumeDisplacementPerMicrostepLabel)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.VolumeDisplacementPerStepLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.VolumeDisplacementPerStepLabel.setObjectName("VolumeDisplacementPerStepLabel")
        self.horizontalLayout_9.addWidget(self.VolumeDisplacementPerStepLabel)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.EngageButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.EngageButton.setObjectName("EngageButton")
        self.horizontalLayout_11.addWidget(self.EngageButton)
        self.DisengageButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.DisengageButton.setObjectName("DisengageButton")
        self.horizontalLayout_11.addWidget(self.DisengageButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.DisplacementVolumeSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.DisplacementVolumeSpinBox.setObjectName("DisplacementVolumeSpinBox")
        self.horizontalLayout_2.addWidget(self.DisplacementVolumeSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.PlungerThrowSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.PlungerThrowSpinBox.setObjectName("PlungerThrowSpinBox")
        self.horizontalLayout_3.addWidget(self.PlungerThrowSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.Step1CalculateButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.Step1CalculateButton.setObjectName("Step1CalculateButton")
        self.verticalLayout_2.addWidget(self.Step1CalculateButton)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.CurrentPlungerPositionSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.CurrentPlungerPositionSpinBox.setObjectName("CurrentPlungerPositionSpinBox")
        self.horizontalLayout_12.addWidget(self.CurrentPlungerPositionSpinBox)
        self.CurrentPlungerPositionSetButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.CurrentPlungerPositionSetButton.setObjectName("CurrentPlungerPositionSetButton")
        self.horizontalLayout_12.addWidget(self.CurrentPlungerPositionSetButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 3, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.DisplacementTargetVolumeSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.DisplacementTargetVolumeSpinBox.setObjectName("DisplacementTargetVolumeSpinBox")
        self.gridLayout.addWidget(self.DisplacementTargetVolumeSpinBox, 2, 1, 1, 1)
        self.RampSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.RampSpinBox.setObjectName("RampSpinBox")
        self.gridLayout.addWidget(self.RampSpinBox, 1, 1, 1, 1)
        self.SpeedUnitComboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.SpeedUnitComboBox.setObjectName("SpeedUnitComboBox")
        self.SpeedUnitComboBox.addItem("")
        self.SpeedUnitComboBox.addItem("")
        self.SpeedUnitComboBox.addItem("")
        self.SpeedUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.SpeedUnitComboBox, 0, 2, 1, 1)
        self.DisplacementTargetVolumeComboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.DisplacementTargetVolumeComboBox.setObjectName("DisplacementTargetVolumeComboBox")
        self.DisplacementTargetVolumeComboBox.addItem("")
        self.DisplacementTargetVolumeComboBox.addItem("")
        self.gridLayout.addWidget(self.DisplacementTargetVolumeComboBox, 2, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 2, 1, 1)
        self.SpeedSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.SpeedSpinBox.setObjectName("SpeedSpinBox")
        self.gridLayout.addWidget(self.SpeedSpinBox, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 4, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PauseButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.PauseButton.setObjectName("PauseButton")
        self.gridLayout_2.addWidget(self.PauseButton, 0, 0, 1, 1)
        self.WithdrawTargetButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.WithdrawTargetButton.setObjectName("WithdrawTargetButton")
        self.gridLayout_2.addWidget(self.WithdrawTargetButton, 1, 0, 1, 1)
        self.StopButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.StopButton.setObjectName("StopButton")
        self.gridLayout_2.addWidget(self.StopButton, 0, 1, 1, 1)
        self.InfuseTargetButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.InfuseTargetButton.setObjectName("InfuseTargetButton")
        self.gridLayout_2.addWidget(self.InfuseTargetButton, 1, 1, 1, 1)
        self.horizontalLayout_14.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_14, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Syringe Pump Control"))
        self.label_14.setText(_translate("MainWindow", "Current plunger position"))
        self.label_2.setText(_translate("MainWindow", "2) Define syringe"))
        self.label_6.setText(_translate("MainWindow", "Syringe volume (mL)"))
        self.label_7.setText(_translate("MainWindow", "Syringe internal diameter (mm)"))
        self.label_5.setText(_translate("MainWindow", "Calibration"))
        self.SavedLabel.setText(_translate("MainWindow", "Saved:?"))
        self.Step2ApplyButton.setText(_translate("MainWindow", "Apply"))
        self.label_15.setText(_translate("MainWindow", "Manual control"))
        self.ManualWithdrawButton.setText(_translate("MainWindow", "Withdraw"))
        self.ManualInfuseButton.setText(_translate("MainWindow", "Infuse"))
        self.label_13.setText(_translate("MainWindow", "Per microstep:"))
        self.VolumeDisplacementPerMicrostepLabel.setText(_translate("MainWindow", "---"))
        self.label_10.setText(_translate("MainWindow", "The volume displacement per step:"))
        self.VolumeDisplacementPerStepLabel.setText(_translate("MainWindow", "-----"))
        self.label_9.setText(_translate("MainWindow", "Motor engage/disengage"))
        self.EngageButton.setText(_translate("MainWindow", "Engage"))
        self.DisengageButton.setText(_translate("MainWindow", "Disengage"))
        self.label.setText(_translate("MainWindow", "1) Calculate syringe diameter"))
        self.label_3.setText(_translate("MainWindow", "Displacement volume (ml)"))
        self.label_4.setText(_translate("MainWindow", "Plunger throw (mm)"))
        self.Step1CalculateButton.setText(_translate("MainWindow", "Calculate"))
        self.CurrentPlungerPositionSetButton.setText(_translate("MainWindow", "Set"))
        self.SpeedUnitComboBox.setItemText(0, _translate("MainWindow", "ul/s"))
        self.SpeedUnitComboBox.setItemText(1, _translate("MainWindow", "ul/min"))
        self.SpeedUnitComboBox.setItemText(2, _translate("MainWindow", "ml/s"))
        self.SpeedUnitComboBox.setItemText(3, _translate("MainWindow", "ml/min"))
        self.DisplacementTargetVolumeComboBox.setItemText(0, _translate("MainWindow", "ul"))
        self.DisplacementTargetVolumeComboBox.setItemText(1, _translate("MainWindow", "ml"))
        self.label_16.setText(_translate("MainWindow", "s"))
        self.label_17.setText(_translate("MainWindow", "Speed"))
        self.label_18.setText(_translate("MainWindow", "Ramp"))
        self.label_19.setText(_translate("MainWindow", "Displacement target volume"))
        self.PauseButton.setText(_translate("MainWindow", "Pause/Continue"))
        self.WithdrawTargetButton.setText(_translate("MainWindow", "Withdraw to target"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.InfuseTargetButton.setText(_translate("MainWindow", "Infuse to target"))

