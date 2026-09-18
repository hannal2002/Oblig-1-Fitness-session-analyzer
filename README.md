#Fitness session analyzer

Option A - Fitness session analyzer
Student: Hanna Linnea Østern
Student number: 385548

## About the project
This project is a Python program for analyzing fitness sessions using simulated data from wearable devices. The project uses the instructor-supplied `data_generator.py` to generate simulated participant profiles and observations. The supplied generator has not been modified. 

The observations are validated before they are added to a session. The program calculates statistics, compares measurements with the participant's reference values and classifies the fitness session.
The possible classifications are:
- Resting
- Moderate activity
- High activity
- Recovering
- Insufficient data

## Classes 
The project currently has four main classes: Participant (represent a participant in the session with name and reference measurements), ReferenceMeasurements (stores reference values), Observation (stores information about one observation for the wearable sensor), and Session (represents a complete session containing a participant and a list of valid observation objects).

The Observation class also has a class method called from_dict(). It is used to create Observation objects directly from the dictionaries in the sample data. This keeps the conversion from dictionary data to Observation objects inside the class that is responsible for the observations.

## Composition, encapsulation and inheritance
Composition is used with Participant having ReferenceMeasurements, and a Session has a Participant and multiple Observation objects.

Encapsulation is used when the reference measurements are stored in the protected-style attribute "_reference_measurements" and accessed through a propoerty.

Inheritance is not used bc there's no natural "is-a" relationship between the classes.

## Assumptions and classification rules
The project uses some assumed threshold values for validation and classification. An observation is rejected if required sensor values are missing or outside the accepted ranges. The validation rules are:
- Timestamp must be an integer of 0 or greater.
- Heart rate must be between 35 and 205 beats per minute.
- Skin response must be 0 or greater.
- Temperature must be between 25 and 42 degrees Celsius.
- Activity level must be between 0 and 1.
- Signal quality must be between 0 and 1.
- Observations with signal quality below 0.5 are rejected.
- At least two usable observations are required to classify a session.

The activity classification rules are:
- Average activity below 0.3: Resting
- Average activity from 0.3 to below 0.7: Moderate activity
- Average activity of 0.7 or higher: High activity

Recovery is checked before the activity-level classification. At least six usable observations are required for recovery detection. The average heart rate and activity level of the first three observations are compared with the last three observations. A session is classified as Recovering when heart rate decreases by at least 15 beats per minute and activity level decreases by at least 0.2.

## Project structure
Repository contains: 
- 'main.py': classes, validation, analysis, classification and the main program.
- 'data_generator.py': generator for simulated fitness data.
- `tests.py': unit tests for the five generated scenarios.
- `README.md': project documentation.
- `requirements.txt': mpty because the project only uses the Python standard library

## How to run
Clone the repository: 
git clone https://github.com/hannal2002/Oblig-1-Fitness-session-analyzer.git

Go to the project folder: 
cd Oblig-1-Fitness-session-analyzer

Run the program: 
python main.py

Run the tests: 
python tests.py

On my Windows system, Python is run with python. On systems where Python uses the python3 command, run python3 main.py instead.

## Example output
When running `main.py', the program analyzes five different scenarios:
resting, moderate activity, high activity, recovery and poor quality. 
Example output from the resting session:

    ==============================
    resting
    ==============================

    Fitness session report:
    Usable observations: 10
    Classification: Resting
    Explanation: The average activity level is below 0.3.

    Heart rate:
    Average: 80.4
    Minimum: 76
    Maximum: 85

    Activity level:
    Average: 0.11499999999999999
    Minimum: 0.04
    Maximum: 0.18

    Comparison with reference:
    Heart rate difference: 2.4000000000000057
    Temperature difference: 0.008000000000002672

The other scenarios are classified as moderate activity, high activity,
recovering or insufficient data depending on the observations.

## Known limitations
The project uses simulated sensor data and simple fixed thresholds.
Recovery detection only compares the final observations and is therefore a
simplified model of real fitness recovery. 
The program does not connect to real wearable sensors and does not store data
between program runs.