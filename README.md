#Fitness session analyzer

Option A - Fitness session analyzer
Student: Hanna Linnea Østern
Student number: 385548

## About the project
This project is a Python program for analyzing fitness sessions using simulated data from wearable devices. The program uses sensor measurements such as heart rate, temperature, skin response, signal quality and activity level to analyze a training session. 

The observations are validated before they are added to a session. The program
calculates statistics, compares measurements with reference values and classifies
the fitness session.
The possible classifications are:
- Resting
- Moderate activity
- High activity
- Recovering
- Insufficient data

## Classes 
The project currently has four main classes: Participant (represent a participant in the session with name and reference measurements), ReferenceMeasurements (stores reference values), Observation (stores information about one observation for the wearable sensor), and Session (represents a complete session containing a participant and a list of valid observation objects). 

## Composition, encapsulation and inheritance
Composition is used with Participant having ReferenceMeasurements, and a Session has a Participant and multiple Observation objects.

Encapsulation is used when the reference measurements are stored in the protected-style attribute "_reference_measurements" and accessed through a propoerty.

Inheritance is not used bc there's no natural "is-a" relationship between the classes.

## Assumptions and classification rules
There are many assumptions in this project regarding to numbers and when to accept or reject and so on.
Observations with a signal quality below 0.5 are rejected. Heart rate must be greater than 0 and activity level cannot be negative. At least two usable observations are required to classify a session.

The classification rules are:
- Average activity below 0.3: Resting
- Average activity from 0.3 to below 0.7: Moderate activity
- Average activity of 0.7 or higher: High activity
- If heart rate and activity level both decrease at the end of the session: Recovering

Recovery is checked before the activity-level classification

## How to run
Clone the repository: 
git clone https://github.com/hannal2002/Oblig-1-Fitness-session-analyzer.git

Go to the project folder: 
cd Oblig-1-Fitness-session-analyzer

Run the program: 
python main.py

Run the tests: 
python tests.py

On my Windows system, Python is run with only 'python' insted of 'python3'.

## Example output
When running `main.py`, the program analyzes five different scenarios:
resting, moderate activity, high activity, recovery and invalid sensor data.
Example output from the resting session:

    ==============================
    Resting session
    ==============================

    Fitness session report:
    Usable observations: 2
    Classification: Resting
    Explanation: The average activity level is below 0.3.

    Heart rate:
     Average: 71.0
     Minimum: 70
     Maximum: 72

    Activity level:
     Average: 0.125
     Minimum: 0.1
     Maximum: 0.15

    Comparison with reference:
     Heart rate difference: 1.0
     Activity level difference: 0.024999999999999994

The other scenarios are classified as moderate activity, high activity,
recovering or insufficient data depending on the observations.

## Known limitations
The project uses simulated sensor data and simple fixed thresholds.
Recovery detection only compares the final observations and is therefore a
simplified model of real fitness recovery. 
The program does not connect to real wearable sensors and does not store data
between program runs.