# -*- coding: utf-8 -*-
import sys
import Phidget22
from Phidget22.Devices.Stepper import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
from Phidget22.StepperControlMode import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Phidget22.Devices.Stepper import *
import numpy as np
import asyncio
import time
import json


class Ui_MainWindow(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        try:
            with open('data.json', 'w') as fp:
                setting_dict = {
                    'displacement_volume': self.DisplacementVolumeSpinBox.value(),
                    'plunger_throw': self.PlungerThrowSpinBox.value(),
                    'syringe_volume': self.SyringeVolumeSpinBox.value(),
                    'syringe_internal_diameter': self.SyringeInternalDiameterSpinBox.value(),
                    'calibration': self.CalibrationSpinBox.value(),
                    'current_plunger_position': self.CurrentPlungerPositionSpinBox.value(),
                    'pumping_rate': self.SpeedSpinBox.value(),
                    'ramp_time': self.RampSpinBox.value(),
                    'displacement_target_volume': self.DisplacementTargetVolumeSpinBox.value(),
                    'speed_unit_index': self.SpeedUnitComboBox.currentIndex(),
                    'target_volume_unit_index': self.DisplacementTargetVolumeComboBox.currentIndex(),
                }
                json.dump(setting_dict, fp)
        except IOError as e :
            sys.stderr.write('Failed to write setting file\n')

    def __init__(self, ch_obj: Stepper):
        super(Ui_MainWindow, self).__init__()
        uic.loadUi("ControlInterface.ui", self)

        # Dependency injection of the phidget object ch
        self._ch = ch_obj
        self._ch.setOnPositionChangeHandler(self.PositionChangeHandler)

        # Initialise variables
        self._operation_tag = None
        self._operation_wait_time = None
        self._is_manual_control = False
        self._paused = False
        self._saved_velocity = 0

        # Try to load saved parameters from file
        try:
            with open('data.json', 'r') as fp:
                setting_dict = json.load(fp)
                self.DisplacementVolumeSpinBox.setValue(setting_dict['displacement_volume'])
                self.PlungerThrowSpinBox.setValue(setting_dict['plunger_throw'])
                self.SyringeVolumeSpinBox.setValue(setting_dict['syringe_volume'])
                self.SyringeInternalDiameterSpinBox.setValue(setting_dict['syringe_internal_diameter'])
                self.CalibrationSpinBox.setValue(setting_dict['calibration'])
                self.CurrentPlungerPositionSpinBox.setValue(setting_dict['current_plunger_position'])
                self.SpeedSpinBox.setValue(setting_dict['pumping_rate'])
                self.RampSpinBox.setValue(setting_dict['ramp_time'])
                self.DisplacementTargetVolumeSpinBox.setValue(setting_dict['displacement_target_volume'])
                self.SpeedUnitComboBox.setCurrentIndex(setting_dict['speed_unit_index'])
                self.DisplacementTargetVolumeComboBox.setCurrentIndex(setting_dict['target_volume_unit_index'])

        except FileNotFoundError as e:
            sys.stderr.write('Setting file not found\n')
        except ValueError as e:
            sys.stderr.write('Saved value is problematic\n')
        except:
            sys.stderr.write('Setting file exists but not readable\n')

        # Load parameters
        self._calibration_factor = self.CalibrationSpinBox.value()
        self._syringe_volume = self.SyringeVolumeSpinBox.value()
        self._syringe_internal_diameter = self.SyringeInternalDiameterSpinBox.value()
        self._syringe_cross_sec = np.pi * self._syringe_internal_diameter ** 2 / 4
        self._max_distance = self._syringe_volume * 1e3 / self._syringe_cross_sec

        # Connect slots
        self.EngageButton.clicked.connect(self.clickedEngageButton)
        self.DisengageButton.clicked.connect(self.clickedDisengageButton)
        self.ManualWithdrawButton.pressed.connect(self.pressedManualWithdrawButton)
        self.ManualWithdrawButton.released.connect(self.releasedManualWithdrawButton)
        self.ManualInfuseButton.pressed.connect(self.pressedManualInfuseButton)
        self.ManualInfuseButton.released.connect(self.releasedManualInfuseButton)
        self.Step2ApplyButton.clicked.connect(self.clickedApplyButton)
        self.CurrentPlungerPositionSetButton.clicked.connect(self.clickedCurrentPlungerPositionSetButton)
        self.Step1CalculateButton.clicked.connect(self.clickedCalculateButton)
        self.WithdrawTargetButton.clicked.connect(self.clickedWithdrawTargetButton)
        self.InfuseTargetButton.clicked.connect(self.clickedInfuseTargetButton)
        self.PauseButton.clicked.connect(self.clickedPauseButton)
        self.StopButton.clicked.connect(self.clickedStopButton)

    # Engage button and disengage button
    def clickedEngageButton(self):
        self._ch.setTargetPosition(self._ch.getPosition())
        self._ch.setEngaged(1)

    def clickedDisengageButton(self):
        self.reset_tags()
        self._ch.setEngaged(0)
        self._ch.setTargetPosition(self._ch.getPosition())

    def reset_tags(self):
        self._operation_wait_time = None
        self._operation_tag = None
        self._paused = False

    # Manual control
    def pressedManualWithdrawButton(self):
        self._ch.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
        self._ch.setVelocityLimit(0)  # mm/min
        rate, acceleration, operation_time, distance = self._get_pump_target()
        if acceleration == 0:
            sys.stderr.write('Zero acceleration, abort')
            self._ch.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
            return
        self._ch.setAcceleration(acceleration)  # Change! mm/s
        self._ch.setEngaged(1)
        self._ch.setVelocityLimit(rate)
        self._is_manual_control = True

    def releasedManualWithdrawButton(self):
        self._ch.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
        self._ch.setVelocityLimit(0)
        self._ch.setTargetPosition(self._ch.getPosition())
        self._is_manual_control = False

    def pressedManualInfuseButton(self):
        self._ch.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
        self._ch.setEngaged(1)
        self._ch.setVelocityLimit(0)
        rate, acceleration, operation_time, distance = self._get_pump_target()
        if acceleration == 0:
            sys.stderr.write('Zero acceleration, abort')
            self._ch.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
            return
        self._ch.setAcceleration(acceleration)  # Change! mm/s
        self._ch.setEngaged(1)
        self._ch.setVelocityLimit(-rate)
        print(f'Manual infuse rate {-rate}')
        self._is_manual_control = True

    def releasedManualInfuseButton(self):
        self._ch.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
        self._ch.setVelocityLimit(0)
        self._ch.setTargetPosition(self._ch.getPosition())
        self._is_manual_control = False

    # Step 1
    def clickedCalculateButton(self):
        diameter = np.sqrt(self.DisplacementVolumeSpinBox.value() * 1e3 / self.PlungerThrowSpinBox.value() / np.pi) * 2
        self.SyringeInternalDiameterSpinBox.setValue(diameter)

    # Step 2
    def clickedApplyButton(self):
        self._syringe_internal_diameter = self.SyringeInternalDiameterSpinBox.value()
        self._syringe_volume = self.SyringeVolumeSpinBox.value()
        self._calibration_factor = self.CalibrationSpinBox.value()
        self._syringe_cross_sec = np.pi * self._syringe_internal_diameter ** 2 / 4
        self._max_distance = self._syringe_volume * 1000 / self._syringe_cross_sec

    # Define current absolute position of the syringe
    def clickedCurrentPlungerPositionSetButton(self):
        self._ch.addPositionOffset(self.CurrentPlungerPositionSpinBox.value() * 1000 / self._syringe_cross_sec \
                                   - self._ch.getPosition())
        # self.PositionLineEdit.setText("0.000")

    def PositionChangeHandler(self, e, position):
        print("Position: %f" % position, "Speed: ", self._ch.getVelocity())
        self.CurrentPlungerPositionSpinBox.setValue(position * self._syringe_cross_sec / 1e3)

        # If exceeds limit then stop
        if not self._is_manual_control:
            current_position = self._ch.getPosition()
            if current_position < 0:
                self._ch.setTargetPosition(0)
                self.reset_tags()
                self._ch.setEngaged(0)
                sys.stderr.write('Pump position exceeds lower limit, reset!\n')
            elif current_position > self._max_distance:
                self._ch.setTargetPosition(self._max_distance)
                self.reset_tags()
                self._ch.setEngaged(0)
                sys.stderr.write('Pump position exceeds lower limit, reset!\n')

    # Pause continue button
    def clickedPauseButton(self):
        print('Pause button clicked')
        if not self._paused:
            print('Internal variable shows the system is in running status')
            print(f'Current position {self._ch.getPosition()}, velocity {self._ch.getVelocity()}')
            if (not self._ch.getPosition() == self._ch.getTargetPosition()) and self._ch.getVelocity() != 0:
                print('Velocity and target check shows the system is in running status')
                self._paused = True
                self._saved_velocity = self._ch.getVelocityLimit()
                self._ch.setVelocityLimit(0)
            else:
                print('Velocity and target check failed')
        else:
            print('Internal variable shows the system is paused')
            if (not self._ch.getPosition() == self._ch.getTargetPosition()) and self._ch.getVelocity() == 0:
                print('Velocity is zero but target is not reached')
                self._ch.setVelocityLimit(self._saved_velocity)
                self._paused = False

    # Stop button
    def clickedStopButton(self):
        self.clickedDisengageButton()

    # Programmed buttons
    def clickedWithdrawTargetButton(self):
        # self.clickedCalculateButton()
        rate, acceleration, operation_time, distance_mm = self._get_pump_target()
        # self.move_to_target_time_control(rate, acceleration, operation_time)
        if self._max_distance < distance_mm + self._ch.getPosition():
            sys.stderr.write('Target exceeds maximum syringe volume, abort\n')
            return
        self.move_to_target_distance_control(rate, acceleration, distance_mm)

    def clickedInfuseTargetButton(self):
        rate, acceleration, operation_time, distance_mm = self._get_pump_target()
        # self.move_to_target_time_control(-rate, acceleration, operation_time)
        if self._ch.getPosition() - distance_mm < 0:
            sys.stderr.write('Target exceeds minimum syringe volume, abort\n')
            return
        self.move_to_target_distance_control(rate, acceleration, -distance_mm)

    def move_to_target_time_control(self, rate, acceleration, operation_time):
        self.clickedEngageButton()
        self._ch.setAcceleration(acceleration)
        self._ch.setVelocityLimit(rate)
        print("Waiting for ", operation_time, " seconds")
        event_loop = asyncio.get_event_loop()
        # event_loop.run_in_executor(None,lambda :ProgrammedDisengage(self,Time))
        tag = time.clock()
        self._operation_tag = tag
        self._operation_wait_time = operation_time
        event_loop.create_task(self.scheduled_disengage(operation_time, tag))

    def move_to_target_distance_control(self, rate, acceleration, target_distance):
        self._ch.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
        self.clickedEngageButton()
        self._ch.setAcceleration(acceleration)
        self._ch.setVelocityLimit(rate)
        input_distance = self._ch.getPosition() + target_distance
        self._ch.setTargetPosition(input_distance)
        print(f'Target distance {target_distance}, target position {input_distance}')
        self._paused = False

    def _get_pump_target(self):
        """
        Get converted pump target to feed to ch object
        :return: rate, acceleration, operation_time, distance
        """
        # Operation time to be implemented!!!
        pumping_rate_value = self.SpeedSpinBox.value()
        pumping_rate_unit_index = self.SpeedUnitComboBox.currentIndex()

        # The universal unit is mm/s

        """
        pumping rate unit index:
        0: ul/s
        1: ul/min
        2: ml/s
        3: ml/min
        """
        # Firstly convert everything to mm and s
        pumping_rate_unit_conversion_list = np.array([1, 1 / 60, 1000, 1000 / 60])
        pumping_rate = pumping_rate_value * pumping_rate_unit_conversion_list[pumping_rate_unit_index]

        ramp_time_value = self.RampSpinBox.value()

        target_volume_value = self.DisplacementTargetVolumeSpinBox.value()
        target_volume_unit = self.DisplacementTargetVolumeComboBox.currentIndex()
        """
        pumping target unit index:
        0: ul
        1: ml
        """
        if target_volume_unit == 0:
            target_volume = target_volume_value
        else:
            target_volume = target_volume_value * 1000

        if ramp_time_value <= 0:
            sys.stderr.write('Infeasible ramp time\n')
            return 0, 0, 0, 0

        syringe_cross_sec = self._syringe_internal_diameter ** 2 / 4 * np.pi
        rate = pumping_rate / syringe_cross_sec
        acceleration = rate / ramp_time_value
        distance_mm = target_volume / syringe_cross_sec

        # Assume the pump reaches maximum speed set
        acceleration_time = rate / acceleration

        # The velocity does not reach maximum, at2 > x
        if acceleration_time ** 2 * acceleration >= distance_mm:
            operation_time = np.sqrt(distance_mm / acceleration)
        else:
            operation_time = acceleration_time * 2 + (distance_mm - acceleration * acceleration_time ** 2) / rate
        return rate, acceleration, operation_time, distance_mm

    async def scheduled_disengage(self, wait_time, tag=None):
        await asyncio.sleep(wait_time)
        if tag is not None:
            if tag == self._operation_tag:
                self.clickedDisengageButton()
        else:
            self.clickedDisengageButton()
