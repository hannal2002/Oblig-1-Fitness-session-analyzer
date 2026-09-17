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

    #Må validere observasjoner
    def is_valid(self): #En metode som sjekker gyldighetene til de ulike målingene
        if self.heart_rate is None or self.signal_quality is None or self.activity_level is None: #Sjekker om verdien i det hele tatt finnes
            return False
        if self.signal_quality < 0.5: #En antakelse at 0.5 kan funke som en grense
            return False
        if self.heart_rate <= 0:
            return False
        if self.activity_level < 0:
            return False

        return True

class Session: #Composition: session inneholder observation-objekter
    def _init_(self, participant):
        self.participant = participant
        self.observations = [] #I hver sesjon er det observert forskjellig ting. Lagres her 
    
    def add_observation(self, observation):
        if observation.is_valid(): #Bare hvis det er gyldig så blir det lagt til i lista
            self.observations.append(observation) #Legger observasjonene i lista


#Behøver 4 standalone funksjoner
def calculate_average(values): #Funksjon for å beregne gjennomsnitt
    if len(values) == 0: #Hvis listen er tom, returner ingenting
        return None
    return sum(values) / len(values) #Summerer tallene, teller tallene. Får gjennomsnitt

def calculate_minimum(values): #Funksjon for minimum verdi
    if len(values) == 0:
        return None
     return min(values)

def calculate_maximum(values):
    if len(values) == 0:
        return None
    return max(values)