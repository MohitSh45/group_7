# group_7_util.py
import random
import time

# Start ID
start_id = 111
_patient_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona']

def create_data():
    global start_id
    patient = random.choice(_patient_names)
    data = {
        'id': start_id,
        'patient': patient,
        'time': time.asctime(),
        'heart_rate': int(random.gauss(80, 1)),
        'respiratory_rate': int(random.gauss(12, 2)),
        'heart_rate_variability': int(random.uniform(50, 80)),
        'body_temperature': round(random.gauss(98.6, 0.5), 1),
        'blood_pressure': {
            'systolic': int(random.gauss(110, 5)),
            'diastolic': int(random.gauss(75, 3))
        },
        'activity': random.choice(['Walking', 'Sleeping', 'Running', 'Sitting'])
    }
    start_id += 1
    return data

def print_data(data):
    print(f"\n--- Patient Health Data ---")
    print(f"ID: {data['id']}")
    print(f"Patient: {data['patient']}")
    print(f"Timestamp: {data['time']}")
    print(f"Heart Rate: {data['heart_rate']} bpm")
    print(f"Respiratory Rate: {data['respiratory_rate']} breaths/min")
    print(f"Heart Rate Variability: {data['heart_rate_variability']} ms")
    print(f"Body Temperature: {data['body_temperature']} °F")
    print(f"Blood Pressure: {data['blood_pressure']['systolic']}/{data['blood_pressure']['diastolic']} mmHg")
    print(f"Activity: {data['activity']}")
    print("----------------------------\n")
