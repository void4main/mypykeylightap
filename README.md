# My Python (Elgato) Key Light AccessPoint

A simple mobile access point for my Elgato Key Lights based on an ESP32.

If you are having trouble getting your Key Lights to work with your local infrastructure, or if you need a mobile solution, check this out.

The idea: you create an AP with your ESP32 and add your Key Lights to that AP.
Then you can control the lights anywhere with your cell phone, which is also connected to the AP.

1. Install MicroPython on your ESP32
2. Replace the boot.py
3. Connect your phone to the ESP32 AP
4. Connect your Elgato Key Light to the AP via the Control Center app.
5. Manage your Key Lights through the ESP32 AP.
