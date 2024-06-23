import time
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def simulate_network_activity(c2_server_url, interval=10):
    while True:
        try:
            response = requests.get(c2_server_url)
            logging.info(f"Simulated network request to C&C server: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Network request failed: {e}")
        time.sleep(interval)  # Wait before the next request

def main():
    C2_SERVER_URL = "http://example.com/command"
    logging.info("Starting network activity simulation...")
    simulate_network_activity(C2_SERVER_URL)

if __name__ == "__main__":
    main()