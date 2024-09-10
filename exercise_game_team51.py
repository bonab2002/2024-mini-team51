from machine import Pin
import time
import random
import json  # json is built-in in MicroPython
import urequests  # manually added urequests.py

# 10 flashes change
N = 10
sample_ms = 10.0
on_ms = 500

# Firebase credentials and endpoint
firebase_config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_PROJECT_ID.firebaseapp.com",
    "projectId": "YOUR_PROJECT_ID",
    "firestoreURL": "https://firestore.googleapis.com/v1/projects/YOUR_PROJECT_ID/databases/(default)/documents/your_collection_name"  # Firestore endpoint
}

def random_time_interval(tmin: float, tmax: float) -> float:
    """Return a random time interval between max and min."""
    return random.uniform(tmin, tmax)

def blinker(N: int, led: Pin) -> None:
    """Blink LED to indicate the start/end of the game."""
    for _ in range(N):
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)

def upload_to_firestore(data: dict) -> None:
    """Uploads JSON data to Firebase Firestore."""
    try:
        url = f"{firebase_config['firestoreURL']}/results"  # Document or collection name

        response = urequests.post(url, json=data, headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            print("Data uploaded successfully to Firestore.")
        else:
            print(f"Failed to upload data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to upload data to Firestore: {str(e)}")

def scorer(t: list[int | None]) -> None:
    """Collect and display results, then upload them as JSON data."""
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # Calculate min, max, and average times
    if t_good:
        min_t = min(t_good)
        max_t = max(t_good)
        avg_t = sum(t_good) / len(t_good)
    else:
        min_t = max_t = avg_t = None

    # Prepare the data to upload
    data = {
        "Minimum": min_t,
        "Maximum": max_t,
        "Average": avg_t,
        "Score": (len(t_good) / len(t)) if t else 0
    }

    # Upload JSON data to Firestore
    upload_to_firestore(data)

if __name__ == "__main__":
    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.on()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.off()
                break
        t.append(t0)

        led.off()

    blinker(5, led)

    scorer(t)
