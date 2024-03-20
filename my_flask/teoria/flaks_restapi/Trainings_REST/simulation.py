import requests

requests.post(
    "http://localhost:5000/training",
    json={
        "name": "Push 1",
        "duration": 120,
        "note": "1. BenchPress 120 kg x 4 x 4 x 4, "
        "2. Squat 140 kg x 5 x 5 x 5, "
        "3. Hip thrust 150 kg x 10 x 10 x 10",
    },
)

requests.post(
    "http://localhost:5000/training",
    json={
        "name": "Pull 2",
        "date": "01/04/21",
        "duration": 90,
        "note": "1. Pull-ups 20 kg x 5 x 5 x 5, "
        "2. Rowing 70 kg x 10 x 10 x 10, "
        "3. Biceps 15 kg x 15 x 15 x 15",
    },
)
