# Import necessary libraries
import numpy as np  # For numerical operations
import pandas as pd  # For saving data to CSV
from neurodsp.sim import sim_combined  # To simulate EEG signals
from neurodsp.utils import set_random_seed  # For reproducibility

# Set a random seed for reproducibility
set_random_seed(42)

# Define parameters for synthetic EEG
n_seconds = 10  # Duration of the signal in seconds
fs = 250  # Sampling rate (250 Hz is common for EEG)
components = {
    'sim_powerlaw': {'exponent': -2},  # Background noise (1/f^2)
    'sim_oscillation': {'freq': 10},  # Alpha wave at 10 Hz
    'sim_bursty_oscillation': {'freq': 20, 'enter_burst': 0.2}  # Beta wave at 20 Hz
}

# Generate synthetic EEG signal
eeg_signal = sim_combined(n_seconds, fs, components)

# Create a time vector for the signal
time = np.arange(0, n_seconds, 1/fs)

# Save the synthetic EEG data to a CSV file
data = pd.DataFrame({'time': time, 'eeg_signal': eeg_signal})
data.to_csv('data/synthetic_eeg.csv', index=False)

print("Synthetic EEG data saved to 'data/synthetic_eeg.csv'")