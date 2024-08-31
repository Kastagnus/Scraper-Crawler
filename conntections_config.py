import time

import requests

# send web request to ckeck if there is internet connection
def is_connected():
    """Check internet connection by sending a request to a stable website."""
    try:
        # Make a request to a fast-loading site (like Google).
        response = requests.get("http://www.google.com", timeout=10)
        # If the request is successful, no error is raised.
        return True
    except requests.ConnectionError as e:
        # ConnectionError raised if internet connection is down.
        print(f"No internet connection: {e}")
        return False
    except requests.Timeout as e:
        # Timeout error checking can also indicate connection issues.
        print(f"Request timed out: {e}")
        return False

# wait and check connection until connection is established again
def handle_connection(connection):
    if not connection():
        print("Connection lost. Pausing...")
        while not connection():
            time.sleep(10)  # Continuously check until connection is restored
        print("Connection restored.")
        return True
    else:
        print("Connection established.")
        return True
