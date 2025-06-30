import numpy as np
import matplotlib.pyplot as plt

# Define the binary sequence
binary_sequence = '110111011110101111111100111000111110000011101101111001001111001111110000'
bit_length = 1  # Length of each bit in seconds
bit_rate = 1000  # Bit rate in bits per second (example value)

# Calculate frequency parameters
f0 = bit_rate  # Fundamental frequency
fB = f0 / 2    # Upper frequency limit
fN = 0         # Lower frequency limit
f_avg = (fB + fN) / 2  # Average frequency
S = fB - fN    # Bandwidth

# Print frequency parameters
print("Frequency Parameters:")
print(f"Fundamental Frequency (f0): {f0} Hz")
print(f"Upper Frequency Limit (fB): {fB} Hz")
print(f"Lower Frequency Limit (fN): {fN} Hz")
print(f"Average Frequency (f_avg): {f_avg} Hz")
print(f"Bandwidth (S): {S} Hz")

# NRZ Encoding
nrz_signal = [1 if bit == '1' else 0 for bit in binary_sequence]

# NRZI Encoding
nrzi_signal = [0] * len(binary_sequence)
current_level = 0  # Start at low level (0)
for i, bit in enumerate(binary_sequence):
    if bit == '1':
        current_level = 1 - current_level  # Toggle level
    nrzi_signal[i] = current_level

# AMI Encoding
ami_signal = []
last_level = 1  # Start with positive level
for bit in binary_sequence:
    if bit == '1':
        ami_signal.append(last_level)
        last_level *= -1  # Alternate levels for next '1'
    else:
        ami_signal.append(0)  # Zero level for '0'

# Manchester Encoding
manchester_signal = []
for bit in binary_sequence:
    if bit == '1':
        manchester_signal.append(0)  # Low to high transition
        manchester_signal.append(1)    # High level
    else:
        manchester_signal.append(1)    # High to low transition
        manchester_signal.append(0)     # Low level

# Create time array for Manchester encoding
manchester_time = np.arange(0, len(manchester_signal) * (bit_length / 2), bit_length / 2)

# Plotting
plt.figure(figsize=(12, 8))

# NRZ Plot
plt.subplot(4, 1, 1)
plt.step(np.arange(len(nrz_signal)), nrz_signal, where='post', label='NRZ', color='blue')
plt.title('NRZ Encoding')
plt.ylim(-0.5, 1.5)
plt.xlim(0, len(binary_sequence)) 
plt.xticks(np.arange(0, len(binary_sequence)+1, 1))  
plt.grid()

# NRZI Plot
plt.subplot(4, 1, 2)
plt.step(np.arange(len(nrzi_signal)), nrzi_signal, where='post', label='NRZI', color='orange')
plt.title('NRZI Encoding')
plt.ylim(-0.5, 1.5)
plt.xlim(0, len(binary_sequence))
plt.xticks(np.arange(0, len(binary_sequence)+1, 1))
plt.grid()

# AMI Plot
plt.subplot(4, 1, 3)
plt.step(np.arange(len(ami_signal)), ami_signal, where='post', label='AMI', color='green')
plt.title('AMI Encoding')
plt.ylim(-2, 2)
plt.xlim(0, len(binary_sequence))
plt.xticks(np.arange(0, len(binary_sequence)+1, 1))
plt.grid()

# Manchester Plot
plt.subplot(4, 1, 4)
plt.step(manchester_time[:len(manchester_signal)], manchester_signal, where='post', label='Manchester', color='red')
plt.title('Manchester Encoding')
plt.ylim(-0.5, 1.5)
plt.xlim(0, len(binary_sequence)/2)  
plt.xticks(np.arange(0, len(binary_sequence)/2 + 1, 0.5))  
plt.grid()

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
