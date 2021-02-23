# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

###############################################################################
#
# Beginning of code insertion



import sys
import time 
import numpy as np
from Phidget22.Devices.Stepper import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

from threading import Thread


try:
    ch = Stepper()
except RuntimeError as e:
    print("Runtime Exception %s" % e.details)
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

def StepperAttached(e):
    try:
        attached = e
        print("\nAttach Event Detected (Information Below)")
        print("===========================================")
        print("Library Version: %s" % attached.getLibraryVersion())
        print("Serial Number: %d" % attached.getDeviceSerialNumber())
        print("Channel: %d" % attached.getChannel())
        print("Channel Class: %s" % attached.getChannelClass())
        print("Channel Name: %s" % attached.getChannelName())
        print("Device ID: %d" % attached.getDeviceID())
        print("Device Version: %d" % attached.getDeviceVersion())
        print("Device Name: %s" % attached.getDeviceName())
        print("Device Class: %d" % attached.getDeviceClass())
        print("\n")

    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)   
    
def StepperDetached(e):
    detached = e
    try:
        print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)   

def ErrorEvent(e, eCode, description):
    print("Error %i : %s" % (eCode, description))

def PositionChangeHandler(e, position):
    
    print("Position: %f" % position, "Speed: ", ch.getVelocity())
    ui.PositionLineEdit.setText(str(np.around(position/60,decimals=3)))
    
    #print( ch.getVelocity() )

try:
    ch.setOnAttachHandler(StepperAttached)
    ch.setOnDetachHandler(StepperDetached)
    ch.setOnErrorHandler(ErrorEvent)
    ch.setOnPositionChangeHandler(PositionChangeHandler)

    print("Waiting for the Phidget Stepper Object to be attached...")
    ch.openWaitForAttachment(1000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)
    
time.sleep(1) 
    
StepsPerRevolution = 200
MicrosteppingDivision = 16 # Microstepping at 1/16th
LeadscrewPitch = 1.0 # millimeters per rotation
GearingRatio = 76 + (49/64) # :1
SecondsPerMinute = 60 # i.e. per minute

MicrostepsPerMillimeter = StepsPerRevolution * MicrosteppingDivision * GearingRatio / LeadscrewPitch

RescaleFactor = SecondsPerMinute / (MicrostepsPerMillimeter)
ch.setRescaleFactor( RescaleFactor ) # All units are now in millimeters and minutes
print("Rescale Factor: ", ch.getRescaleFactor(), "\n")

# Supply, 20V DC rated at 3.25A
# Reccommended motor current, 2.8A (at 12V)
ch.setCurrentLimit( 2.8 ) # Current limit in Amps

# Motor datasheet, 25rpm max
MaxVelocityMicrostepsPerSecond = (25/60) * StepsPerRevolution * MicrosteppingDivision * GearingRatio
MaxVelocity = 50
ch.setVelocityLimit( MaxVelocity )

MaxAcceleration = 100
ch.setAcceleration( MaxAcceleration )


StepResolution = LeadscrewPitch / (GearingRatio * StepsPerRevolution)
print("\n")
print("Step resolution: ")
#print(StepResolution, "mm")
#print(StepResolution*1E3, "um")
print(StepResolution*1E6, "nm\n")

MicrostepResolution = LeadscrewPitch / (GearingRatio * StepsPerRevolution * MicrosteppingDivision)
print("Microstep resolution: ")
#print(MicrostepResolution, "mm")
#print(MicrostepResolution*1E3, "um")
print(MicrostepResolution*1E6, "nm\n")


ch.setControlMode(1) # Continuous movement


# End of code insertion
#
###############################################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 961)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.ManualControlLabel = QtWidgets.QLabel(self.centralwidget)
        self.ManualControlLabel.setObjectName("ManualControlLabel")
        self.horizontalLayout_5.addWidget(self.ManualControlLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.EngageButton = QtWidgets.QPushButton(self.centralwidget)
        self.EngageButton.setObjectName("EngageButton")
        self.verticalLayout_3.addWidget(self.EngageButton)
        self.DisengageButton = QtWidgets.QPushButton(self.centralwidget)
        self.DisengageButton.setObjectName("DisengageButton")
        self.verticalLayout_3.addWidget(self.DisengageButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.VelocityLimitLabel = QtWidgets.QLabel(self.centralwidget)
        self.VelocityLimitLabel.setObjectName("VelocityLimitLabel")
        self.horizontalLayout_3.addWidget(self.VelocityLimitLabel)
        self.ManualVelocitySpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ManualVelocitySpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ManualVelocitySpinBox.setDecimals(3)
        self.ManualVelocitySpinBox.setMinimum(0.001)
        self.ManualVelocitySpinBox.setProperty("value", 10.0)
        self.ManualVelocitySpinBox.setObjectName("ManualVelocitySpinBox")
        self.horizontalLayout_3.addWidget(self.ManualVelocitySpinBox)
        self.VelocityLimitUnits = QtWidgets.QLabel(self.centralwidget)
        self.VelocityLimitUnits.setObjectName("VelocityLimitUnits")
        self.horizontalLayout_3.addWidget(self.VelocityLimitUnits)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.AcceleratioLabel = QtWidgets.QLabel(self.centralwidget)
        self.AcceleratioLabel.setObjectName("AcceleratioLabel")
        self.horizontalLayout_2.addWidget(self.AcceleratioLabel)
        self.ManualAccelerationSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ManualAccelerationSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ManualAccelerationSpinBox.setDecimals(3)
        self.ManualAccelerationSpinBox.setMinimum(0.001)
        self.ManualAccelerationSpinBox.setProperty("value", 5.0)
        self.ManualAccelerationSpinBox.setObjectName("ManualAccelerationSpinBox")
        self.horizontalLayout_2.addWidget(self.ManualAccelerationSpinBox)
        self.AccelerationUnits = QtWidgets.QLabel(self.centralwidget)
        self.AccelerationUnits.setObjectName("AccelerationUnits")
        self.horizontalLayout_2.addWidget(self.AccelerationUnits)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_4.addWidget(self.line_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ManualUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.ManualUpButton.setObjectName("ManualUpButton")
        self.verticalLayout.addWidget(self.ManualUpButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PositionLabel = QtWidgets.QLabel(self.centralwidget)
        self.PositionLabel.setObjectName("PositionLabel")
        self.horizontalLayout.addWidget(self.PositionLabel)
        self.PositionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PositionLineEdit.setAcceptDrops(False)
        self.PositionLineEdit.setFrame(False)
        self.PositionLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PositionLineEdit.setObjectName("PositionLineEdit")
        self.horizontalLayout.addWidget(self.PositionLineEdit)
        self.PositionUnits = QtWidgets.QLabel(self.centralwidget)
        self.PositionUnits.setObjectName("PositionUnits")
        self.horizontalLayout.addWidget(self.PositionUnits)
        self.ZeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZeroButton.setObjectName("ZeroButton")
        self.horizontalLayout.addWidget(self.ZeroButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ManualDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.ManualDownButton.setObjectName("ManualDownButton")
        self.verticalLayout.addWidget(self.ManualDownButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.ProgrammedMoveLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProgrammedMoveLabel.setObjectName("ProgrammedMoveLabel")
        self.horizontalLayout_10.addWidget(self.ProgrammedMoveLabel)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ProgrammedUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProgrammedUpButton.setObjectName("ProgrammedUpButton")
        self.verticalLayout_5.addWidget(self.ProgrammedUpButton)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.StrokeLengthLabel = QtWidgets.QLabel(self.centralwidget)
        self.StrokeLengthLabel.setObjectName("StrokeLengthLabel")
        self.horizontalLayout_6.addWidget(self.StrokeLengthLabel)
        self.StrokeLengthSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.StrokeLengthSpinBox.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.StrokeLengthSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StrokeLengthSpinBox.setDecimals(3)
        self.StrokeLengthSpinBox.setMaximum(300.0)
        self.StrokeLengthSpinBox.setProperty("value", 80.0)
        self.StrokeLengthSpinBox.setObjectName("StrokeLengthSpinBox")
        self.horizontalLayout_6.addWidget(self.StrokeLengthSpinBox)
        self.StrokeLengthUnits = QtWidgets.QLabel(self.centralwidget)
        self.StrokeLengthUnits.setObjectName("StrokeLengthUnits")
        self.horizontalLayout_6.addWidget(self.StrokeLengthUnits)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.RampDistanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.RampDistanceLabel.setObjectName("RampDistanceLabel")
        self.horizontalLayout_7.addWidget(self.RampDistanceLabel)
        self.RampDistanceSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.RampDistanceSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RampDistanceSpinBox.setDecimals(3)
        self.RampDistanceSpinBox.setMinimum(0.1)
        self.RampDistanceSpinBox.setMaximum(300.0)
        self.RampDistanceSpinBox.setProperty("value", 2.0)
        self.RampDistanceSpinBox.setObjectName("RampDistanceSpinBox")
        self.horizontalLayout_7.addWidget(self.RampDistanceSpinBox)
        self.RampDistanceUnits = QtWidgets.QLabel(self.centralwidget)
        self.RampDistanceUnits.setObjectName("RampDistanceUnits")
        self.horizontalLayout_7.addWidget(self.RampDistanceUnits)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.FinalSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.FinalSpeedLabel.setObjectName("FinalSpeedLabel")
        self.horizontalLayout_8.addWidget(self.FinalSpeedLabel)
        self.FinalSpeedSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.FinalSpeedSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FinalSpeedSpinBox.setDecimals(3)
        self.FinalSpeedSpinBox.setMinimum(0.001)
        self.FinalSpeedSpinBox.setProperty("value", 10.0)
        self.FinalSpeedSpinBox.setObjectName("FinalSpeedSpinBox")
        self.horizontalLayout_8.addWidget(self.FinalSpeedSpinBox)
        self.FinalSpeedUnits = QtWidgets.QLabel(self.centralwidget)
        self.FinalSpeedUnits.setObjectName("FinalSpeedUnits")
        self.horizontalLayout_8.addWidget(self.FinalSpeedUnits)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.ProgrammedDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProgrammedDownButton.setObjectName("ProgrammedDownButton")
        self.verticalLayout_5.addWidget(self.ProgrammedDownButton)
        self.horizontalLayout_12.addLayout(self.verticalLayout_5)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_12.addWidget(self.line_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem11)
        self.CalculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateButton.setObjectName("CalculateButton")
        self.verticalLayout_6.addWidget(self.CalculateButton)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.StrokeTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.StrokeTimeLabel.setObjectName("StrokeTimeLabel")
        self.horizontalLayout_9.addWidget(self.StrokeTimeLabel)
        self.StrokeTimeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.StrokeTimeLineEdit.setFrame(False)
        self.StrokeTimeLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StrokeTimeLineEdit.setObjectName("StrokeTimeLineEdit")
        self.horizontalLayout_9.addWidget(self.StrokeTimeLineEdit)
        self.StrokeTimeUnits = QtWidgets.QLabel(self.centralwidget)
        self.StrokeTimeUnits.setObjectName("StrokeTimeUnits")
        self.horizontalLayout_9.addWidget(self.StrokeTimeUnits)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem12)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.EngageButton, self.DisengageButton)
        MainWindow.setTabOrder(self.DisengageButton, self.ManualVelocitySpinBox)
        MainWindow.setTabOrder(self.ManualVelocitySpinBox, self.ManualAccelerationSpinBox)
        MainWindow.setTabOrder(self.ManualAccelerationSpinBox, self.ManualUpButton)
        MainWindow.setTabOrder(self.ManualUpButton, self.PositionLineEdit)
        MainWindow.setTabOrder(self.PositionLineEdit, self.ZeroButton)
        MainWindow.setTabOrder(self.ZeroButton, self.ManualDownButton)
        MainWindow.setTabOrder(self.ManualDownButton, self.ProgrammedUpButton)
        MainWindow.setTabOrder(self.ProgrammedUpButton, self.StrokeLengthSpinBox)
        MainWindow.setTabOrder(self.StrokeLengthSpinBox, self.RampDistanceSpinBox)
        MainWindow.setTabOrder(self.RampDistanceSpinBox, self.FinalSpeedSpinBox)
        MainWindow.setTabOrder(self.FinalSpeedSpinBox, self.ProgrammedDownButton)
        MainWindow.setTabOrder(self.ProgrammedDownButton, self.CalculateButton)
        MainWindow.setTabOrder(self.CalculateButton, self.StrokeTimeLineEdit)
            #######################################################################
        #
        # Beginning of code insertion
        
        self.ManualAccelerationSpinBox.setMinimum(0.001)
        self.ManualAccelerationSpinBox.setProperty( "value", MaxAcceleration/2 )
        self.ManualAccelerationSpinBox.setMaximum( MaxAcceleration )
        
        self.ManualVelocitySpinBox.setMinimum(0.001)
        self.ManualVelocitySpinBox.setProperty( "value", MaxVelocity/2 )
        self.ManualVelocitySpinBox.setMaximum( MaxVelocity )
    
        self.FinalSpeedSpinBox.setProperty("value", MaxVelocity/2 )
        self.FinalSpeedSpinBox.setMaximum( MaxVelocity )
        
        self.EngageButton.clicked.connect(self.clickedEngageButton)
        self.DisengageButton.clicked.connect(self.clickedDisengageButton)
        
        self.ManualUpButton.pressed.connect(self.pressedManualUpButton)
        self.ManualUpButton.released.connect(self.releasedManualUpButton)
        
        self.ManualDownButton.pressed.connect(self.pressedManualDownButton)
        self.ManualDownButton.released.connect(self.releasedManualDownButton)
        
        self.ZeroButton.clicked.connect(self.clickedZeroButton)
        
        self.CalculateButton.clicked.connect(self.clickedCalculateButton)
        
        self.ProgrammedUpButton.clicked.connect(self.clickedProgrammedUp)
        
        self.ProgrammedDownButton.clicked.connect(self.clickedProgrammedDown)
        
    def clickedEngageButton(self):
        ch.setTargetPosition( ch.getPosition() )
        ch.setEngaged(1)

    def clickedDisengageButton(self):
        ch.setEngaged(0)
        ch.setTargetPosition( ch.getPosition() )

    def pressedManualUpButton(self):
        ch.setVelocityLimit(0)
        ch.setAcceleration ( self.ManualAccelerationSpinBox.value() )
        ch.setEngaged(1)
        ch.setVelocityLimit( self.ManualVelocitySpinBox.value() )
        
    def releasedManualUpButton(self):
        ch.setVelocityLimit(0)
        ch.setTargetPosition( ch.getPosition() )
        
    def pressedManualDownButton(self):
        ch.setEngaged(1)
        ch.setVelocityLimit(0)
        ch.setAcceleration ( self.ManualAccelerationSpinBox.value() )
        ch.setVelocityLimit( -self.ManualVelocitySpinBox.value() )
        
    def releasedManualDownButton(self):
        ch.setVelocityLimit(0)
        ch.setTargetPosition( ch.getPosition() )
        
    def clickedZeroButton(self):
        ch.addPositionOffset( -ch.getPosition() )
        self.PositionLineEdit.setText("0.000")
    
    def clickedCalculateButton(self):
        if self.RampDistanceSpinBox.value() > self.StrokeLengthSpinBox.value():
            self.RampDistanceSpinBox.setProperty("value", self.StrokeLengthSpinBox.value() )
        
        RampTime = 2 * self.RampDistanceSpinBox.value() / self.FinalSpeedSpinBox.value()
        Acceleration = self.FinalSpeedSpinBox.value() / RampTime
        
        ConstantVelocityDistance = self.StrokeLengthSpinBox.value() - self.RampDistanceSpinBox.value()
        ConstantVelocityTime = ConstantVelocityDistance / self.FinalSpeedSpinBox.value()
        
        TotalTime = ConstantVelocityTime + RampTime
        
        self.StrokeTimeLineEdit.setText(str(np.around(TotalTime, decimals=2)))
        
        return [TotalTime*60, Acceleration/60]
        
    def clickedProgrammedUp(self):
        self.clickedCalculateButton()
        self.clickedEngageButton()
        [Time,Acceleration] = self.clickedCalculateButton()
        ch.setAcceleration(Acceleration)
        ch.setVelocityLimit(self.FinalSpeedSpinBox.value())
        print("Waiting for ", Time, " seconds")
        BackgroundThread = Thread(target=ProgrammedDisengage(self,Time), args=(4,))
        BackgroundThread.start()
 
    def clickedProgrammedDown(self):
        self.clickedCalculateButton()
        self.clickedEngageButton()
        [Time,Acceleration] = self.clickedCalculateButton()
        ch.setAcceleration(Acceleration)
        ch.setVelocityLimit(-self.FinalSpeedSpinBox.value())
        print("Waiting for ", Time, " seconds")
        BackgroundThread = Thread(target=ProgrammedDisengage(self,Time), args=(4,))
        BackgroundThread.start()
        
    # End code insertion    
    #            
    ###########################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DipPy (Alaric Taylor, 2017)"))
        self.ManualControlLabel.setText(_translate("MainWindow", "Manual control"))
        self.EngageButton.setText(_translate("MainWindow", "Engage"))
        self.DisengageButton.setText(_translate("MainWindow", "Disengage"))
        self.VelocityLimitLabel.setText(_translate("MainWindow", "Velocity limit"))
        self.VelocityLimitUnits.setText(_translate("MainWindow", "mm/min"))
        self.AcceleratioLabel.setText(_translate("MainWindow", "Acceleration"))
        self.AccelerationUnits.setText(_translate("MainWindow", "mm/min^2"))
        self.ManualUpButton.setText(_translate("MainWindow", "Up"))
        self.PositionLabel.setText(_translate("MainWindow", "Position"))
        self.PositionUnits.setText(_translate("MainWindow", "mm"))
        self.ZeroButton.setText(_translate("MainWindow", "Zero"))
        self.ManualDownButton.setText(_translate("MainWindow", "Down"))
        self.ProgrammedMoveLabel.setText(_translate("MainWindow", "Programmed move"))
        self.ProgrammedUpButton.setText(_translate("MainWindow", "Up"))
        self.StrokeLengthLabel.setText(_translate("MainWindow", "Total stroke length"))
        self.StrokeLengthUnits.setText(_translate("MainWindow", "mm"))
        self.RampDistanceLabel.setText(_translate("MainWindow", "Ramp distance"))
        self.RampDistanceUnits.setText(_translate("MainWindow", "mm"))
        self.FinalSpeedLabel.setText(_translate("MainWindow", "Final speed"))
        self.FinalSpeedUnits.setText(_translate("MainWindow", "mm/min"))
        self.ProgrammedDownButton.setText(_translate("MainWindow", "Down"))
        self.CalculateButton.setText(_translate("MainWindow", "Calculate"))
        self.StrokeTimeLabel.setText(_translate("MainWindow", "Stroke time"))
        self.StrokeTimeUnits.setText(_translate("MainWindow", "mins"))

###############################################################################
#
# Begin inserted code

# Function with the timer
def ProgrammedDisengage(self,seconds):
    time.sleep(seconds)
    self.clickedDisengageButton()

# End inserted code
#
###############################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    #sys.exit(app.exec_())
    ###########################################################################
    #
    # Begin inserted code
    app.exec_()    
    try:
        ch.close()
        print("Closed Stepper device")
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)
    exit(0)
    # End inserted code
    #
    ###########################################################################
