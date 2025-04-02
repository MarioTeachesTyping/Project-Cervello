# scripts/preprocess_eeg.py
import numpy as np
import pandas as pd
import mne  # For EEG preprocessing

# Load the synthetic EEG data
data = pd.read_csv('../data/synthetic_eeg.csv')
eeg_signal = data['eeg_signal'].values
time = data['time'].values
fs = 250  # Sampling rate (Hz)

# Convert to MNE Raw object
info = mne.create_info(ch_names=['EEG'], sfreq=fs, ch_types=['eeg'])
raw = mne.io.RawArray(eeg_signal[np.newaxis, :], info)

# Apply a bandpass filter (1-40 Hz)
raw.filter(1, 40, fir_design='firwin')

# Apply a notch filter to remove line noise (e.g., 50 Hz or 60 Hz)
raw.notch_filter(np.arange(50, 251, 50), fir_design='firwin')

# Plot the raw and filtered data
raw.plot(title='Raw EEG Data')
raw.filter(1, 40).plot(title='Filtered EEG Data')

# Save the preprocessed data
preprocessed_data = raw.get_data()[0]
pd.DataFrame({'time': time, 'eeg_signal': preprocessed_data}).to_csv('../data/preprocessed_eeg.csv', index=False)
print("Preprocessed EEG data saved to '../data/preprocessed_eeg.csv'")