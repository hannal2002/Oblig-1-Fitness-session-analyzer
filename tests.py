import unittest

from main import (
    Participant,
    ReferenceMeasurements,
    Observation,
    Session,
    analyze_session
)

from data_generator import generate_fitness_data


class TestFitnessSessionAnalyzer(unittest.TestCase):

    #Lager en komplett Session ved hjelp av data_generator
    def create_session(self, scenario):
        profile, observations = generate_fitness_data(
            participant_id="TEST001",
            scenario=scenario,
            seed=42,
            number_of_windows=10
        )

        reference = ReferenceMeasurements(
            profile["baseline_heart_rate"],
            profile["baseline_skin_response"],
            profile["baseline_temperature"]
        )

        participant = Participant(
            profile["participant_id"],
            reference
        )

        session = Session(participant)

        for data in observations:
            observation = Observation.from_dict(data)
            session.add_observation(observation)

        return session

    #Tester et normalt hvilescenario
    def test_resting_session(self):
        session = self.create_session("resting")
        result = analyze_session(session)

        self.assertEqual(result["classification"], "Resting")
        self.assertEqual(result["usable_observations"], 10)

    #Tester moderat aktivitet
    def test_moderate_activity(self):
        session = self.create_session("moderate_activity")
        result = analyze_session(session)

        self.assertEqual(result["classification"], "Moderate activity")
        self.assertEqual(result["usable_observations"], 10)

    #Tester høy aktivitet
    def test_high_activity(self):
        session = self.create_session("high_activity")
        result = analyze_session(session)

        self.assertEqual(result["classification"], "High activity")
        self.assertEqual(result["usable_observations"], 10)

    #Tester recovery der puls og aktivitet synker
    def test_recovery(self):
        session = self.create_session("recovery")
        result = analyze_session(session)

        self.assertEqual(result["classification"], "Recovering")
        self.assertEqual(result["usable_observations"], 10)

    #Tester ugyldige og dårlige sensordata
    def test_poor_quality(self):
        session = self.create_session("poor_quality")
        result = analyze_session(session)

        self.assertEqual(result["classification"], "Insufficient data")
        self.assertEqual(result["usable_observations"], 0)


if __name__ == "__main__":
    unittest.main()