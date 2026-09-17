#Tester med ulike scenario

resting_data = [ #Også aantakelser
    {
        "timestamp": 1, 
        "heart_rate": 70,
        "skin_response": 1.2, 
        "temperature": 32.5,
        "activity_level": 0.1,
        "signal_quality": 0.95
    },
    {
        "timestamp": 2, 
        "heart_rate": 72,
        "skin_response": 1.3, 
        "temperature": 32.6,
        "activity_level": 0.15,
        "signal_quality": 0.94
    }
]

moderate_date = [
    {
        "timestamp": 1, 
        "heart_rate": 105,
        "skin_response": 2.0, 
        "temperature": 33.0,
        "activity_level": 0.4,
        "signal_quality": 0.95
    },
    {
        "timestamp": 2, 
        "heart_rate": 115,
        "skin_response": 2.3, 
        "temperature": 33.2,
        "activity_level": 0.5,
        "signal_quality": 0.96
    }
]

high_data = [
    {
        "timestamp": 1, 
        "heart_rate": 155,
        "skin_response": 3.1, 
        "temperature": 33.8,
        "activity_level": 0.8,
        "signal_quality": 0.94
    },
    {
        "timestamp": 2, 
        "heart_rate": 165,
        "skin_response": 3.4, 
        "temperature": 34.0,
        "activity_level": 0.9,
        "signal_quality": 0.95
    }
]

recovery_data = [
    {
        "timestamp": 1, 
        "heart_rate": 160,
        "skin_response": 3.2, 
        "temperature": 34.0,
        "activity_level": 0.85,
        "signal_quality": 0.95
    },
    {
        "timestamp": 2, 
        "heart_rate": 150,
        "skin_response": 3., 
        "temperature": 33.8,
        "activity_level": 0.7,
        "signal_quality": 0.94
    },
    {
        "timestamp": 3, 
        "heart_rate": 125, #Synkende
        "skin_response": 2.5, 
        "temperature": 33.4,
        "activity_level": 0.4, #Synkende
        "signal_quality": 0.96
    }
]

invalid_data = [
    {
        "timestamp": 1, 
        "heart_rate": 120, 
        "skin_response": 2.1, 
        "temperature": 33.0,
        "activity_level": 0.5, 
        "signal_quality": 0.2
    },
    {
        "timestamp": 2, 
        "heart_rate": -10, 
        "skin_response": 2.0, 
        "temperature": 33.1,
        "activity_level": 0.4, 
        "signal_quality": 0.95
    }
]