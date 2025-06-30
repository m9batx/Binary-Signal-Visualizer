# 🔌 Digital Line Coding Visualizer

Script provides a simple and intuitive way to visualize how a binary data sequence can be encoded using four classic digital line coding techniques: **NRZ**, **NRZI**, **AMI**, and **Manchester encoding**. These techniques are commonly used in digital communications to represent binary data as physical electrical signals.

---

## 📸 What It Does

* Takes a binary bitstream (hardcoded in the script).
* Encodes it using:

  * **NRZ (Non-Return to Zero)**
  * **NRZI (Non-Return to Zero Inverted)**
  * **AMI (Alternate Mark Inversion)**
  * **Manchester Encoding**
* Displays each encoding as a time-domain waveform using `matplotlib`.
* Also prints out **frequency-related parameters** (bit rate, bandwidth, etc.).

---

## 🧠 Why It's Useful

Line coding is **fundamental in networking, hardware design, and telecommunications**. This project is especially helpful if you're:

* A student learning digital communications.
* An instructor wanting to show how different line codes behave.
* A hobbyist curious about signal representation.

---

## 📦 Requirements

* Python 3.x
* NumPy
* Matplotlib

Install dependencies using pip:

```bash
pip install numpy matplotlib
```

---

You will see four waveform plots:

1. **NRZ** – High for 1, low for 0.
2. **NRZI** – Level changes for 1, stays for 0.
3. **AMI** – 0 is zero voltage, 1 alternates between + and - voltage.
4. **Manchester** – Each bit is split with a transition in the middle (clock sync friendly).

You’ll also get printed info about bit rate, average frequency, and bandwidth.

---
## 🏗️ Project Structure

* `binary_sequence` – The input bitstream (you can change this).
* `bit_rate` – Controls signal timing and frequency calculations.
* `plt.step()` – Used to simulate digital signal transitions.
* Each encoding type is implemented with intuitive logic for easy learning.


