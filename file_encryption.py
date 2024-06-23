import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def simulate_encryption(target_dir, encrypted_extension=".encrypted"):
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            original_file = os.path.join(root, file)
            encrypted_file = original_file + encrypted_extension
            shutil.copyfile(original_file, encrypted_file)
            logging.info(f"Simulated encryption: {original_file} -> {encrypted_file}")

def main():
    TARGET_DIR = "test_files"
    logging.info("Starting file encryption simulation...")
    simulate_encryption(TARGET_DIR)

if __name__ == "__main__":
    main()