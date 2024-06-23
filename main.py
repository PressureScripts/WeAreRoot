import logging
from file_encryption import simulate_encryption
from network_activity import simulate_network_activity
from ml_evasion import train_evasion_model, simulate_evasion_behavior

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    # File Encryption Simulation
    logging.info("Starting file encryption simulation...")
    simulate_encryption("test_files")

    # Network Activity Simulation
    logging.info("Starting network activity simulation...")
    simulate_network_activity("http://example.com/command")

    # ML Evasion Simulation
    logging.info("Training evasion model...")
    model = train_evasion_model()
    logging.info("Starting evasion behavior simulation...")
    simulate_evasion_behavior(model, 120, 1)
    simulate_evasion_behavior(model, 250, 0)

if __name__ == "__main__":
    main()