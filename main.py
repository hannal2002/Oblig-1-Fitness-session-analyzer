from sample_data import resting_data, moderate_data, high_data, recovery_data, invalid_data #Tester dette først

#Klasse for en deltaker og at den deltakeren har personlige referanseverdier
class Participant:
    def __init__(self, name, reference_measurements): #En deltaker må ha et navn
        self.name = name
        #Composition: en participant har et referenceMeasurements-objekt
        #Protected-style attributt brukes som en del av encapsulation
        self._reference_measurements = reference_measurements #Composition: en participant har referansemålinger

    @property #Kontrollert tilgang. Behandles som internt
    def reference_measurements(self):
        return self._reference_measurements

#Her er deltakerens personlige referanseverdier
class ReferenceMeasurements:
    def __init__(self, heart_rate, temperature, activity_level): #Målingene inneholder puls, temp, aktivitetsnivå
        self.heart_rate = heart_rate
        self.temperature = temperature
        self.activity_level = activity_level

#èn observasjon fra de simulerte sensorene
class Observation: #Inneholder alle de forskjellige observasjonene
    def __init__(self, timestamp, heart_rate, skin_response, temperature, acitvity_level, signal_quality):
        self.timestamp = timestamp
        self.heart_rate = heart_rate
        self.skin_response = skin_response
        self.temperature = temperature
        self.activity_level = acitvity_level
        self.signal_quality = signal_quality
    
    #Gjør om dictionary-data fra sample_data om til et Observation-objekt
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["timestamp"],
            data["heart_rate"],
            data["skin_response"],
            data["temperature"],
            data["activity_level"],
            data["signal_quality"]
        )

    #Må validere observasjoner. Avviser manglende, umulige eller for dårlige sensorverdier
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

#Composition: en Session inneholder en Participant og en liste med Observation-objekter
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

#Klassifiserer hele økta ut fra brukbare observasjoner
def classify_session(observations):
    if len(observations) < 2:
        return "Insufficient data"
    
    activity_levels = []

    for observation in observations: #Gå gjennom listen
        activity_levels.append(observation.activity_level) #Får ny liste
    
    average_activity = calculate_average(activity_levels) #Beregner gjennomsnittet for nivået

#Recovery sjekkes først fordi utviklingen på slutten av økta er viktigere enn gjennomsnittlig aktivitetsnivå
    if detect_recovery(observations): #Sjekker om det er recovery her
        return "Recovering"
    
    #Aktivitetsnivå: lav, moderat og høy
    if average_activity < 0.3: #Bare en antakelse med 0.3
        return "Resting"
    
    if average_activity < 0.7: #Enda en antakelse
        return "Moderate activity"
    
    return "High activity" #Alt annet er høyt

#En forklaring på hvorfor økten fikk sin klassifisering
def explain_classification(observations): 
    classification = classify_session(observations)

    if classification == "Insufficient data":
        return "There are fewer than two usable observations."

    if classification == "Recovering":
        return "Heart rate and activity level decreased at the end of the session."

    activity_levels = []

    for observation in observations:
        activity_levels.append(observation.activity_level)

    average_activity = calculate_average(activity_levels)

    if classification == "Resting":
        return "The average activity level is below 0.3."

    if classification == "Moderate activity":
        return "The average activity level is between 0.3 and 0.7."

    return "The average activity level is 0.7 or higher."


#Samle resultene fra økta på ett sted
def analyze_session(session): #Tar imot en økt
    heart_rates = [] 
    activity_levels = []

    for observation in session.observations:#Legger verdiene i de tilhørene listene
        heart_rates.append(observation.heart_rate)
        activity_levels.append(observation.activity_level)
    
    #Returnere samme struktur selv om ingen observasjoner kunne brukes
    if len(session.observations) == 0: 
        return {
            "usable_observations": 0,
            "classification": "Insufficient data", 
            "explanation": explain_classification(session.observations),
            "heart_rate": {
                "average": None, 
                "minimum": None, 
                "maximum": None
            }, 
            "activity_level": {
                "average": None, 
                "minimum": None, 
                "maximum": None
            },
            "reference_comparison": {
                "heart_rate_difference": None, 
                "activity_difference": None
            }
        }
    
    result = { #Lager en dictionary med resultatene som også kan brukes senere
        "usable_observations": len(session.observations),
        "classification": classify_session(session.observations),
        "explanation": explain_classification(session.observations),
        "heart_rate": {
            "average": calculate_average(heart_rates),
            "minimum": calculate_minimum(heart_rates),
            "maximum": calculate_maximum(heart_rates)
        },
        "activity_level": {
            "average": calculate_average(activity_levels),
            "minimum": calculate_minimum(activity_levels),
            "maximum": calculate_maximum(activity_levels)
        },
        #Sammenligner gjennomsnittet fra økten med deltakerens egne referanseverdier
        "reference_comparison":{
            "heart_rate_difference": calculate_average(heart_rates) - session.participant.reference_measurements.heart_rate,
            "activity_difference": calculate_average(activity_levels) - session.participant.reference_measurements.activity_level
        }
    }
    return result

#Lage noe lesbart for utskriften
def print_report(result):
    print("\nFitness session report:")
    print("Usable observations:", result["usable_observations"])
    print("Classification:", result["classification"])
    print("Explanation:", result["explanation"])

    print("\nHeart rate:") 
    print(" Average:", result["heart_rate"]["average"]) #Går inn i dictionary og finner puls og så average
    print(" Minimum:", result["heart_rate"]["minimum"])
    print(" Maximum:", result["heart_rate"]["maximum"])

    print("\nActivity level:")
    print(" Average:", result["activity_level"]["average"])
    print(" Minimum:", result["activity_level"]["minimum"])
    print(" Maximum:", result["activity_level"]["maximum"])

    print("\nComparison with reference:")
    print(" Heart rate difference:", result["reference_comparison"]["heart_rate_difference"])
    print(" Activity level difference:", result["reference_comparison"]["activity_difference"])


#Kjøres kun når bare main.py kjører direkte
if __name__ == "__main__":
    reference = ReferenceMeasurements(70,32.5,0.1)
    participant = Participant("Test Participant", reference)

    #Kjører alle scenarioene for å se
    scenarios = {
            "Resting session": resting_data,
            "Moderate activity": moderate_data,
            "High activity": high_data,
            "Recovery": recovery_data,
            "Invalid data": invalid_data
        }

    for scenario_name, data_set in scenarios.items():
        print("\n==============================")
        print(scenario_name)
        print("==============================")


        session = Session(participant)

        for data in data_set:
            observation = Observation.from_dict(data)
            session.add_observation(observation)

        result = analyze_session(session)
        print_report(result)

