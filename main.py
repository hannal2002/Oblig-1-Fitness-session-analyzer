class Participant:
    def _init_(self, name): #En deltaker må ha et navn
        self.name = name

class ReferenceMeasurements:
    def _init_(self, heart_rate, temperature, activity_level): #Målingene inneholder puls, temp, aktivitetsnivå
        self.heart_rate = heart_rate
        self.temperature = temperature
        self.activity_level = activity_level

class Observation:
    pass

class Session: 
    pass