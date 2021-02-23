import sys
import time
import Phidget22
from Phidget22.Devices.Stepper import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
from ControlInterface import *
import asyncio
from PyQt5.QtWidgets import QApplication, QProgressBar
from quamash import QEventLoop, QThreadExecutor
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
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


# def PositionChangeHandler(e, position):
#     print("Position: %f" % position, "Speed: ", ch.getVelocity())
#     ui.PositionLineEdit.setText(str(round(position / 60, 3)))

    # print( ch.getVelocity() )


try:
    ch.setOnAttachHandler(StepperAttached)
    ch.setOnDetachHandler(StepperDetached)
    ch.setOnErrorHandler(ErrorEvent)
    # ch.setOnPositionChangeHandler(PositionChangeHandler)

    print("Waiting for the Phidget Stepper Object to be attached...")
    ch.setDeviceLabel("pump")
    ch.openWaitForAttachment(1000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

time.sleep(1)

StepsPerRevolution = 200
MicrosteppingDivision = 16  # Microstepping at 1/16th
LeadscrewPitch = 5.0  # millimeters per rotation
GearingRatio = 99  # :1
SecondsPerMinute = 60  # i.e. per minute

MicrostepsPerMillimeter = StepsPerRevolution * MicrosteppingDivision * GearingRatio / LeadscrewPitch

RescaleFactor = 1 / MicrosteppingDivision * (360/StepsPerRevolution/GearingRatio) / (360/LeadscrewPitch)
ch.setRescaleFactor(RescaleFactor)  # All units are now in millimeters and minutes
print("Rescale Factor: ", ch.getRescaleFactor(), "\n")

# Supply, 20V DC rated at 3.25A
# Reccommended motor current, 2.8A (at 12V)
ch.setCurrentLimit(2.8)  # Current limit in Amps

# Motor datasheet, 25rpm max
MaxVelocityMicrostepsPerSecond = (25 / 60) * StepsPerRevolution * MicrosteppingDivision * GearingRatio
MaxVelocity = 50.0
# ch.setVelocityLimit(MaxVelocity)

MaxAcceleration = 100
ch.setAcceleration(MaxAcceleration)

StepResolution = LeadscrewPitch / (GearingRatio * StepsPerRevolution)
print("\n")
print("Step resolution: ")
# print(StepResolution, "mm")
# print(StepResolution*1E3, "um")
print(StepResolution * 1E6, "nm\n")

MicrostepResolution = LeadscrewPitch / (GearingRatio * StepsPerRevolution * MicrosteppingDivision)
print("Microstep resolution: ")
# print(MicrostepResolution, "mm")
# print(MicrostepResolution*1E3, "um")
print(MicrostepResolution * 1E6, "nm\n")
    
ch.setControlMode(StepperControlMode.CONTROL_MODE_STEP)  # Step mode


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)  # NEW must set the event loop
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(ch)
    # ui.setupUi(MainWindow)
    ui.show()

    # sys.exit(app.exec_())
    ###########################################################################
    #
    # Begin inserted code

    with loop:
        loop.run_forever()
    # app.exec_()
    try:
        ch.close()
        print("Closed Stepper device")
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)
    exit(0)