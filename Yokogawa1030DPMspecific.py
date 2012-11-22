import visa

#Create instance of class: ThisIsMyDPM = Yokogawa1030DPM.YDPM(instrument address)
#Example: asking for voltage -> voltage = instancename.getVoltage()

class YDPM(visa.Instrument):
	def __init__(self, address):
		visa.Instrument.__init__(self, "GPIB::"+str(address)) 
		#Turns on all of the normal outputs
		self.write("MEASURE:ITEM:NORMAL:PRESET ALL")
		self.__wAIndex = 0
		self.__wBIndex = 1
		# self.__wCIndex = 2
		self.__freqIndex = 2
	
	def getInstrumentInformation(self):
		return self.ask("*IDN?")
	
	def disableVoltageMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleVoltageMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleVoltageMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:V:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:V:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:V:ELEMENT2 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:V:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:V:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:V:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:V:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:V:SIGMA OFF")
			
	def disableCurrentMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleCurrentMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleCurrentMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:A:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:A:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:A:ELEMENT2 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:A:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:A:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:A:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:A:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:A:SIGMA OFF")

	def disableActivePowerMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleActivePowerMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleActivePowerMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:W:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:W:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:W:ELEMENT2 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:W:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:W:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:W:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:W:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:W:SIGMA OFF")			

	def disableApparentPowerMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleApparentPowerMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleApparentPowerMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:VA:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VA:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:VA:ELEMENT2 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VA:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:VA:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VA:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:VA:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VA:SIGMA OFF")

	def disableReactivePowerMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleReactivePowerMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleReactivePowerMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:VAR:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VAR:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:VAR:ELEMENT2 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VAR:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:VAR:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VAR:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:VAR:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VAR:SIGMA OFF")			
	
	def disablePowerFactorMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.togglePowerFactorMeasurements(phaseA,phaseB,phaseC,sigma)

	def togglePowerFactorMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:PF:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:PF:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:PF:ELEMENT2 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:PF:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:PF:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:PF:ELEMENT3 OFF")	
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:PF:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:PF:SIGMA OFF")
			
	def disablePhaseAngleMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.togglePhaseAngleMeasurements(phaseA,phaseB,phaseC,sigma)

	def togglePhaseAngleMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:DEG:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:DEG:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:DEG:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:DEG:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:DEG:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:DEG:ELEMENT3 OFF")	
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:DEG:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:DEG:SIGMA OFF")

	def disablePeakVoltageMeasurements(self, phaseA = False, phaseB = False, phaseC = False):
		self.togglePeakVoltageMeasurements(phaseA,phaseB,phaseC)

	def togglePeakVoltageMeasurements(self, phaseA, phaseB, phaseC):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:VPK:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VPK:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:VPK:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VPK:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:VPK:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:VPK:ELEMENT3 OFF")	
			
	def disablePeakCurrentMeasurements(self, phaseA = False, phaseB = False, phaseC = False):
		self.togglePeakCurrentMeasurements(phaseA,phaseB,phaseC)

	def togglePeakCurrentMeasurements(self, phaseA, phaseB, phaseC):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:APK:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:APK:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:APK:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:APK:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:APK:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:APK:ELEMENT3 OFF")	
			
			
	def disableWattHourMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleWattHourMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleWattHourMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:WH:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WH:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:WH:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WH:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:WH:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WH:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:WH:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WH:SIGMA OFF")
			
	def disableWattHourPeakMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleWattHourPeakMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleWattHourPeakMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:WHP:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WHP:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:WHP:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WHP:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:WHP:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WHP:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:WHP:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WHP:SIGMA OFF")

	def disableWattHourMeterMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleWattHourMeterMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleWattHourMeterMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:WHM:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WHM:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:WHM:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WHM:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:WHM:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WHM:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:WHM:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:WHM:SIGMA OFF")
		
	def disableAmpHourMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleAmpHourMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleAmpHourMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:AH:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AH:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:AH:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AH:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:AH:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AH:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:AH:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AH:SIGMA OFF")
			
	def disableAmpHourPeakMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleAmpHourPeakMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleAmpHourPeakMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:AHP:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AHP:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:AHP:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AHP:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:AHP:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AHP:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:AHP:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AHP:SIGMA OFF")
			
	def disableAmpHourMeterMeasurements(self, phaseA = False, phaseB = False, phaseC = False, sigma = False):
		self.toggleAmpHourMeterMeasurements(phaseA,phaseB,phaseC,sigma)

	def toggleAmpHourMeterMeasurements(self, phaseA, phaseB, phaseC, sigma):
		if phaseA == True:
			self.write("MEASURE:ITEM:NORMAL:AHM:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AHM:ELEMENT1 OFF")
		if phaseB == True:
			self.write("MEASURE:ITEM:NORMAL:AHM:ELEMENT1 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AHM:ELEMENT2 OFF")	
		if phaseC == True:
			self.write("MEASURE:ITEM:NORMAL:AHM:ELEMENT3 ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AHM:ELEMENT3 OFF")
		if sigma == True:
			self.write("MEASURE:ITEM:NORMAL:AHM:SIGMA ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:AHM:SIGMA OFF")
			
	def disableTimeMeasurements(self, time = False):
		self.toggleTimeMeasurements(time)

	def toggleTimeMeasurements(self, time):
		if time == True:
			self.write("MEASURE:ITEM:NORMAL:TIME ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:TIME OFF")
			
	def disableEfficiencyComputation(self, math = False):
		self.toggleEfficiencyComputation(math)
		
	def toggleEfficiencyComputation(self, math):
		if math == True:
			self.write("MEASURE:ITEM:NORMAL:MATH ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:MATH OFF")
			
	def disableTorque(self, torque = False):
		self.toggleTorque(torque)
		
	def toggleTorque(self, torque):
		if torque == True:
			self.write("MEASURE:ITEM:NORMAL:TORQUE ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:TORQUE OFF")
			
	def disableRPM(self, rpm = False):
		self.toggleRPM(rpm)
		
	def toggleRPM(self, rpm):
		if rpm == True:
			self.write("MEASURE:ITEM:NORMAL:RPM ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:RPM OFF")
			
	def disableSRPM(self, srpm = False):
		self.toggleSRPM(srpm)
		
	def toggleSRPM(self, srpm):
		if srpm == True:
			self.write("MEASURE:ITEM:NORMAL:SRPM ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:SRPM OFF")
			
	def disableSlip(self, slip = False):
		self.toggleSlip(slip)
		
	def toggleSlip(self, slip):
		if slip == True:
			self.write("MEASURE:ITEM:NORMAL:SLIP ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:SLIP OFF")
			
	def disableMPower(self, mPower = False):
		self.toggleMPower(mPower)
		
	def toggleMPower(self, mPower):
		if mPower == True:
			self.write("MEASURE:ITEM:NORMAL:MPOWER ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:MPOWER OFF")
			
	def disableMEfficiency(self, mEfficiency = False):
		self.toggleMEfficiency(mEfficiency)
		
	def toggleMEfficiency(self, mEfficiency):
		if mEfficiency == True:
			self.write("MEASURE:ITEM:NORMAL:MEFFICIENCY ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:MEFFICIENCY OFF")

	def disableTEfficiency(self, tEfficiency = False):
		self.toggleTEfficiency(tEfficiency)
		
	def toggleTEfficiency(self, tEfficiency):
		if tEfficiency == True:
			self.write("MEASURE:ITEM:NORMAL:TEFFICIENCY ON")
		else:
			self.write("MEASURE:ITEM:NORMAL:TEFFICIENCY OFF")

			
			
#####################################################################			
			
			
		
	def takeReading(self):
		#asks instrument for measurements and puts returned string into variable reading
		reading = self.ask("MEASURE:VALUE?")
		return self.parseResponse(reading)

	def parseResponse(self, str):
		#initialize list for the values read from instrument
		readvalues = []
		#split the string from the instrument into list of data
		readvalues = str.split(',') 
		return readvalues
		

	def getActivePowers(self, reading = None):
		if reading == None:
			reading = []
			reading = self.takeReading()
		activePowers = [reading[self.__wAIndex], reading[self.__wBIndex]]
		return activePowers

	def getThreePhaseActivePower(self, reading = None):
		if reading == None:
			reading = []
			reading = self.takeReading()
		activePowers = []
		activePowers = self.getActivePowers(reading)
		realPower = float(activePowers[0]) + float(activePowers[1])
		return realPower
		
	def getPhaseAActivePower(self, reading = None):
		if reading == None:
			reading = []
			reading = self.takeReading()
		activePowers = []
		activePowers = self.getActivePowers(reading)
		return activePowers[0]
	
	def getPhaseBActivePower(self, reading = None):
		if reading == None:
			reading = []
			reading = self.takeReading()
		activePowers = []
		activePowers = self.getActivePowers(reading)
		return activePowers[1]
		
	# def getPhaseCActivePower(self, reading = None):
		# if reading == None:
			# reading = []
			# reading = self.takeReading()
		# activePowers = []
		# activePowers = self.getActivePowers(reading)
		# return activePowers[2]
		
	# def getApparentPowers(self, reading = None):
		# if reading == None:
			# reading = []
			# reading = self.takeReading()
		# apparentPowers = []
		# apparentPowers[0] = reading[self.__vaaIndex]
		# apparentPowers[1] = reading[self.__vabIndex]
		# apparentPowers[2] = reading[self.__vacIndex]
		# return apparentPowers
		
	# def getPhaseAApparentPower(self, reading = None):
		# apparentPowers = []
		# apparentPowers = self.getApparentPowers(reading)
		# return apparentPowers[0]
		
	# def getPhaseBApparentPower(self, reading = None):
		# apparentPowers = []
		# apparentPowers = self.getApparentPowers(reading)
		# return apparentPowers[1]
	
	# def getPhaseCApparentPower(self, reading = None):
		# apparentPowers = []
		# apparentPowers = self.getApparentPowers(reading)
		# return apparentPowers[2]
		
	# def getReactivePowers(self, reading = None):
		# if reading == None:
			# reading = []
			# reading = self.takeReading()
		# apparentPowers = []
		# reactivePowers[0] = reading[self.__varaIndex]
		# reactivePowers[1] = reading[self.__varbIndex]
		# reactivePowers[2] = reading[self.__varcIndex]
		# return reactivePowers
		
	# def getPhaseAReactivePower(self, reading = None):
		# reactivePowers = []
		# reactivePowers = self.getReactivePowers(reading)
		# return reactivePowers[0]
		
	# def getPhaseBReactivePower(self, reading = None):
		# reactivePowers = []
		# reactivePowers = self.getReactivePowers(reading)
		# return reactivePowers[1]
		
	# def getPhaseCReactivePower(self, reading = None):
		# reactivePowers = []
		# reactivePowers = self.getReactivePowers(reading)
		# return reactivePowers[2]

	def getFrequency(self, reading = None):
		if reading == None:
			reading = []
			reading = self.takeReading()
		frequency = float(reading[self.__freqIndex])
		return frequency
	
		
	# def getThreePhaseApparentPower(self, reading):
		# apparent = self.getPhaseAApparentPower(reading) + self.getPhaseBApparentPower(reading) + self.getPhaseCApparentPower(reading)
		# return apparent
		
	# def getThreePhaseReactivePower(self, reading):
		# reactive = self.getPhaseAReactivePower(reading) + self.getPhaseBReactivePower(reading) + self.getPhaseCReactivePower(reading)
		# return reactive