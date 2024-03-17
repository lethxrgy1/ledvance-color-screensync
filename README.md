# Ledvance screen sync using tinytuya

It is a Python application designed to enhance your ambient environment by synchronizing a Tuya smart bulb's color with the dominant color on your computer screen. This project is perfect for setting the mood during gaming sessions, movies, or simply to create a dynamic lighting experience that complements your screen content.

## DEMO

![Macbook and bulb color sync](assets/demo.gif)
Cool right?

## Getting Started

Follow these instructions to get it up and running on your system.

### Prerequisites

- Python 3.x
- Pip (Python package installer)
- Access to a Tuya smart bulb and its credentials (Device ID, IP Address, and Local Key) using TinyTuya repo
- Local key from your LEDVANCE can be extracted using the method described here: https://community.home-assistant.io/t/ledvance-integration-this-is-how-to-do-it-as-per-08-22/449783

### Installation

**Clone the Repository:**

```bash
git clone https://github.com/lethxrgy/ledvance-color-screensync.git
cd ledvance-color-screensync
```

**Install Dependencies:**

```bash
pip install numpy pillow tinytuya
```

### Configuration

Before running the script, ensure you have your Tuya smart bulb's Device ID, IP Address, and Local Key. You can find these details using the Tuya IoT Platform or by following Tuya's documentation on linking your device for development.

Open the script with your favorite text editor and replace the placeholders in the setup_bulb function with your bulb's credentials:

```bash
def setup_bulb(device_id, ip, local_key):
    bulb = tinytuya.BulbDevice("YourDeviceID", "YourDeviceIP", "YourLocalKey")
    ...
```

### Running the ledvance-color-sync

With your bulb configured, run Main.py from your terminal:

```bash
python3.10 main.py
OR
python3 main.py
```

The script will continuously capture your screen's dominant color, enhance its vibrancy, and update your smart bulb's color to match.

### Usage Tips

- For the best experience, position the smart bulb where it can complement your screen well.
- Adjust the color enhancement factor in enhance_color_saturation function for personalized vibrancy.
- Consider running in the background during your multimedia sessions.
- Adjust the version 3.4 to the current firmware version of your bulb
- Refresh rate is every second to optimize the load on your CPU but you can change it to any value

### Contributing

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.
