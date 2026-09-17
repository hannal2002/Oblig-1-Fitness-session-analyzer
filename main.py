class Participant:
    def _init_(self, name): #En deltaker må ha et navn
        self.name = name
        self.reference_measurements = reference_measurements #Composition: en participant har referansemålinger

class ReferenceMeasurements:
    def _init_(self, heart_rate, temperature, activity_level): #Målingene inneholder puls, temp, aktivitetsnivå
        self.heart_rate = heart_rate
        self.temperature = temperature
        self.activity_level = activity_level

class Observation: #Inneholder alle de forskjellige observasjonene
    def _init_(self, timestamp, heart_rate, skin_response, temperature, acitvity_level, signal_quality):
        self.timestamp = timestamp
        self.heart_rate = heart_rate
        self.skin_response = skin_response
        self.temperature = temperature
        self.activity_level = acitvity_level
        self.signal_quality = signal_quality

class Session: #Composition: session inneholder observation-objekter
    def _init_(self, participant):
        self.participant = participant
        self.observations = [] #I hver sesjon er det observert forskjellig ting. Lagres her 
    
    def add_observation(self, observation):
        self.observations.append(observation) #Legger observasjonene i lista