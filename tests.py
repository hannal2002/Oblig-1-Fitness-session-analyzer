import unittest

from main import (
    Participant,
    ReferenceMeasurements,
    Observation,
    Session,
    analyze_session
)

from sample_data import (
    resting_data,
    moderate_data,
    high_data,
    recovery_data,
    invalid_data
)


class TestFitnessSessionAnalyzer(unittest.TestCase):

    def create_session(self, data):
        reference = ReferenceMeasurements(70, 32.5, 0.1)
        participant = Participant("Test Participant", reference)
        session = Session(participant)

        for item in data:
            observation = Observation.from_dict(item)
            session.add_observation(observation)

        return session

    def test_resting_session(self): #Forventer resting fra denne testen
        session = self.create_session(resting_data)
        result = analyze_session(session)

        self.assertEqual(result["classification"], "Resting")

    def test_moderate_session(self):
        session = self.create_session(moderate_data)
        result = analyze_session(session)

        self.assertEqual(result["classification"], "Moderate activity")

    def test_high_activity_session(self):
        session = self.create_session(high_data)
        result = analyze_session(session)

        self.assertEqual(result["classification"], "High activity")

    def test_recovery_session(self):
        session = self.create_session(recovery_data)
        result = analyze_session(session)

        self.assertEqual(result["classification"], "Recovering")

    def test_invalid_data(self):
        session = self.create_session(invalid_data)
        result = analyze_session(session)

        self.assertEqual(result["classification"], "Insufficient data")
        self.assertEqual(result["usable_observations"], 0)


if __name__ == "__main__":
    unittest.main()