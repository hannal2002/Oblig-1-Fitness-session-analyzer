from sample_data import resting_data, moderate_data, high_data, recovery_data, invalid_data #Tester dette først
class Participant:
    def __init__(self, name, reference_measurements): #En deltaker må ha et navn
        self.name = name
        self.reference_measurements = reference_measurements #Composition: en participant har referansemålinger

class ReferenceMeasurements:
    def __init__(self, heart_rate, temperature, activity_level): #Målingene inneholder puls, temp, aktivitetsnivå
        self.heart_rate = heart_rate
        self.temperature = temperature
        self.activity_level = activity_level

class Observation: #Inneholder alle de forskjellige observasjonene
    def __init__(self, timestamp, heart_rate, skin_response, temperature, acitvity_level, signal_quality):
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
    def __init__(self, participant):
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


#Må finne ut av recovery basert på puls og aktivitet på slutten av en økt
def detect_recovery(observations):
    if len(observations) < 2: #Har vi færre enn 2 observasjoner kan vi ikke finne ut av om verdien har sunket
        return False
    
    previous = observations[-2] #Hente nest siste element
    last = observations [-1] #Hente siste element

    #Sammenligner elementene. Begge må være synkende for recovery
    if last.heart_rate < previous.heart_rate and last.activity_level < previous.activity_level:
        return True
    return False

def classify_session(observations):
    if len(observations) < 2:
        return "Insufficient data"
    
    activity_levels = []

    for observation in observations: #Gå gjennom listen
        activity_levels.append(observation.activity_level) #Får ny liste
    
    average_activity = calculate_average(activity_levels) #Beregner gjennomsnittet for nivået

    if detect_recovery(observations): #Sjekker om det er recovery her
        return "Recovering"
    
    #Aktivitetsnivå: lav, moderat og høy
    if average_activity < 0.3: #Bare en antakelse med 0.3
        return "Resting"
    
    if average_activity < 0.7: #Enda en antakelse
        return "Moderate activity"
    
    return "High activity" #Alt annet er høyt


#Samle resultene fra økta på ett sted
def analyze_session(session): #Tar imot en økt
    heart_rates = [] 
    activity_levels = []

    for observation in session.observations:#Legger verdiene i de tilhørene listene
        heart_rates.append(observation.heart_rate)
        activity_levels.append(observation.activity_level)
    
    result = { #Lager en dictionary med resultatene
        "usable_observations": len(session.observations),
        "classification": classify_session(session.observations),
        "heart_rate": {
            "average": calculate_average(heart_rates),
            "minimum": calculate_minimum(heart_rates),
            "maximum": calculate_maximum(heart_rates)
        },
        "activity_level": {
            "average": calculate_average(activity_levels),
            "minimum": calculate_minimum(activity_levels),
            "maximum": calculate_maximum(activity_levels)
        }
    }
    return result

#Lage noe lesbart for utskriften
def print_report(result):
    print("\nFitness session report:")
    print("Usable observations:", result["usable_observations"])
    print("Classification:", result["classification"])

    print("\nHeart rate:") 
    print(" Average:", result["heart_rate"]["average"]) #Går inn i dictionary og finner puls og så average
    print(" Minimum:", result["heart_rate"]["minimum"])
    print(" Maximum:", result["heart_rate"]["maximum"])

    print("\nActivity level:")
    print(" Average:", result["activity_level"]["average"])
    print(" Minimum:", result["activity_level"]["minimum"])
    print(" Maximum:", result["activity_level"]["maximum"])










reference = ReferenceMeasurements(70,32.5,0.1)
participant = Participant("Test Participant", reference)
session = Session(participant)


#Ulike dataer fra sample_data

for data in resting_data:
    observation = Observation(
        data["timestamp"],
        data["heart_rate"],
        data["skin_response"],
        data["temperature"],
        data["activity_level"],
        data["signal_quality"]
    )

    session.add_observation(observation)

#Legger til utregning for de ulike relevante
heart_rates = []

for observation in session.observations:
    heart_rates.append(observation.heart_rate)

average_heart_rate = calculate_average(heart_rates)
heart_rate_difference = average_heart_rate - participant.reference_measurements.heart_rate
minimum_heart_rate = calculate_minimum(heart_rates)
maximum_heart_rate = calculate_maximum(heart_rates)

print("Average heart rate:", average_heart_rate)
print("Heart rate difference from reference:", heart_rate_difference)
print("Minimum heart rate:", minimum_heart_rate)
print("Maximum heart rate:", maximum_heart_rate)

#Aktivitetsnivå
activity_levels = []

for observation in session.observations:
    activity_levels.append(observation.activity_level)

average_activity = calculate_average(activity_levels)
minimum_activity = calculate_minimum(activity_levels)
maximum_activity = calculate_maximum(activity_levels)

print("Average activity level:", average_activity)
print("Minimum activity level:", minimum_activity)
print("Maximum activity level", maximum_activity)


print(len(session.observations))
print(classify_session(session.observations))


result = analyze_session(session)
print_report(result)