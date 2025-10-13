import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    logging.info("Background worker started")
    while True:
        # Example task: print something every 10 seconds
        logging.info("Worker is doing its job...")
        time.sleep(10)  # sleep for 10 seconds

if __name__ == "__main__":
    main()
