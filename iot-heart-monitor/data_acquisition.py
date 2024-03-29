# Python Code for Data Acquisition and Transmission

import requests
import time

# Replace these variables with your IoT platform details
iot_platform_url = "https://your-iot-platform-api-endpoint.com"
iot_api_key = "your-api-key"

def send_data_to_iot_platform(data):
    # Craft the payload with the heart rate data
    payload = {
        "heart_rate": data,
        "timestamp": int(time.time())  # Unix timestamp for data synchronization
    }

    # Set headers including your API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {iot_api_key}"
    }

    try:
        # Send POST request to the IoT platform
        response = requests.post(f"{iot_platform_url}/send_data", json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print(f"Failed to send data. Error: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {str(e)}")

# Assuming you have a function to read heart rate from Arduino
def read_heart_rate_from_arduino():
    # Replace this line with actual function call to get heart rate data
    return 75  # Example heart rate value

# Main loop for continuous data transmission
while True:
    heart_rate = read_heart_rate_from_arduino()
    send_data_to_iot_platform(heart_rate)

    # Adjust the time interval based on your requirements
    time.sleep(60)  # Send data every 60 seconds

send_data_to_iot_platform function is responsible for sending heart rate data to your IoT platform.
read_heart_rate_from_arduino function is a placeholder for the actual function that reads heart rate data from the Arduino.
Please replace the placeholder values for iot_platform_url and iot_api_key with your specific IoT platform details.

#For the Arduino part, you'll need to use the Arduino IDE and write a sketch to read data from the pulse sensor and send it to the Wi-Fi module. 
#This sketch will interact with the Python code shown above. If you're not familiar with writing Arduino sketches, there are many resources and tutorials available online to help you get started.
