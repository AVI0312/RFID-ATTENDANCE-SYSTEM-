# RFID-ATTENDANCE-SYSTEM
A comprehensive attendance management system utilizing RFID technology and Arduino for efficient and secure attendance tracking.

##  Project Overview

This project aims to create an RFID-based attendance system that integrates with an Arduino board to provide a robust solution for tracking attendance. The system reads unique RFID tags, logs attendance, and includes features to detect and prevent proxy attendance, ensuring data integrity and security.

###  Key Features

- **RFID Tag Reading:** Efficiently reads and processes RFID tags for attendance logging.
- **Arduino Integration:** Utilizes an Arduino board to control peripheral devices such as LEDs and buzzers for user feedback.
- **Proxy Detection:** Implements measures to detect and prevent unauthorized access, ensuring only registered tags are accepted.
- **GUI Interface:** A user-friendly interface built with Tkinter for easy interaction and system control.
- **Attendance Logging:** Records attendance with timestamps for accurate tracking and reporting.

##  Tech Stack

- **Frontend:** Tkinter for GUI development.
- **Backend:** Python for logic and data processing.
- **Hardware:** Arduino Uno for controlling peripherals.
- **Communication:** Serial communication for data transfer between RFID module and PC.

##  Installation

### Prerequisites

- Python 3.8 or higher.
- Arduino IDE for programming the Arduino board.
- PyFirmata library for Arduino communication.
- Tkinter for GUI components.
- Serial library for RFID communication.

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/rfid-attendance-system.git
   cd rfid-attendance-system
   ```

2. **Install Dependencies:**
   ```bash
   pip install pyfirmata tkinter serial
   ```

3. **Upload Arduino Code:**
   - Open the Arduino IDE.
   - Upload the provided `arduino_code.ino` to your Arduino board.

4. **Run the Application:**
   ```bash
   python3 ard.py
   ```

## 💻 Usage

1. **Launch the Application:**
   - The GUI will display buttons to control the LED and start/stop attendance logging.

2. **RFID Tag Reading:**
   - Hold the RFID tag near the RFID module to read the data.
   - The system will log the attendance with a timestamp.

3. **Proxy Detection:**
   - The system will alert if an unauthorized tag is detected.



![Image](https://github.com/user-attachments/assets/915d3876-491b-49a9-bcea-3acbcac56482)

![Image](https://github.com/user-attachments/assets/69900fa5-ed8e-498d-b4ca-3598d51ae899)

![Image](https://github.com/user-attachments/assets/188a85ed-d1b6-4336-a44d-5fc939ff5993)
