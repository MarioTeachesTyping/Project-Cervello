# Import necessary libraries
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
import time  # For adding delays to simulate real-time streaming

# Set up BrainFlow parameters
params = BrainFlowInputParams()
params.serial_port = 'synthetic'  # Use synthetic data mode

# Initialize the board (simulated EEG device)
board_id = BoardIds.SYNTHETIC_BOARD.value  # Use the synthetic board
board = BoardShim(board_id, params)

# Prepare the board for streaming
board.prepare_session()

# Start streaming data
board.start_stream()
print("Streaming synthetic EEG data...")

# Simulate real-time data acquisition
try:
    while True:
        # Get the latest EEG data (256 samples)
        data = board.get_current_board_data(256)

        # Print the data (for demonstration purposes)
        print(f"Received {len(data[0])} samples from {len(data)} channels")

        # Wait for 1 second before fetching the next batch
        time.sleep(1)

except KeyboardInterrupt:
    # Stop streaming when the user interrupts the program
    print("Stopping stream...")
    board.stop_stream()
    board.release_session()