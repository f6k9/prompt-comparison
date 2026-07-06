# ESP32 Prompt Engineering and Llama 3.1 Evaluation

This repository documents an experiment in prompt engineering using the Llama 3.1 model (`llama-3.1-8b-instant`) via the Groq API. Five variations of a prompt—ranging from basic to highly constrained—were executed back-to-back using a hardcoded static context architecture to evaluate how prompt structure influences LLM response quality.

---

## Raw Execution Logs & Outputs

### --- Running Prompt 1 ---
* **Prompt Type:** Basic (Very Simple)
* **Prompt Sent:** `Give me some cool ESP32 project ideas.`

#### Llama Response:
The ESP32 is a versatile and powerful microcontroller that offers a wide range of possibilities for various projects. Here are some cool ESP32 project ideas:

1. **Home Automation System**: Create a smart home system that controls lights, temperature, and security using the ESP32 as a central hub. You can use Wi-Fi or Bluetooth connectivity to control devices remotely.
2. **Weather Station**: Build a weather station that displays temperature, humidity, pressure, and other environmental data on an LCD screen or sends it to the cloud for monitoring.
3. **IoT Robot**: Design and build a robot that can navigate through a space, detect obstacles, and interact with its environment using sensors and the ESP32's Wi-Fi capabilities.
4. **Smart Gardening System**: Create a system that monitors soil moisture, temperature, and light levels, and sends notifications when the garden needs watering or other attention.
5. **GPS Tracker**: Build a GPS tracker that sends the device's location to a server or cloud service, allowing you to track its movement in real-time.
6. **Voice Assistant**: Create a voice assistant that can recognize voice commands and perform tasks using the ESP32's Wi-Fi connectivity and a speech recognition library.
7. **Automated Pet Feeder**: Design an automated pet feeder that dispenses food at set times or based on the pet's weight, using the ESP32's Wi-Fi capabilities and a sensor to track the pet's weight.
8. **Environmental Monitoring System**: Build a system that monitors air quality, noise pollution, and other environmental factors, sending the data to a server or cloud service for analysis.
9. **Smart Lighting System**: Create a smart lighting system that adjusts its brightness and color based on the time of day, ambient light, and user preferences, using the ESP32's Wi-Fi capabilities.
10. **IoT Energy Monitor**: Build a system that monitors energy consumption in real-time, sending the data to a server or cloud service for analysis and providing insights on energy-saving opportunities.
11. **Automated Camera**: Design an automated camera that takes photos at set intervals, using the ESP32's Wi-Fi capabilities and a sensor to detect motion or changes in the scene.
12. **Smart Bike Lock**: Create a smart bike lock that can be unlocked and locked using a smartphone app, using the ESP32's Wi-Fi capabilities and a sensor to detect the lock's status.
13. **Automated Plant Watering System**: Build a system that monitors soil moisture and water plants when needed, using the ESP32's Wi-Fi capabilities and a sensor to track the soil's moisture level.
14. **Smart Door Lock**: Design a smart door lock that can be unlocked and locked using a smartphone app, using the ESP32's Wi-Fi capabilities and a sensor to detect the lock's status.
15. **IoT Fire Alarm**: Build a system that detects smoke and heat, sending an alert to users and authorities in case of a fire.

---

### --- Running Prompt 2 ---
* **Prompt Type:** Improved
* **Prompt Sent:** `Act as an embedded systems expert. Give me a list of 5 intermediate-level ESP32 project ideas that utilize both its Wi-Fi and Bluetooth capabilities. Include a brief description of what each project does.`

#### Llama Response:
As an embedded systems expert, I can suggest the following 5 intermediate-level ESP32 project ideas that utilize both its Wi-Fi and Bluetooth capabilities:

1. **Smart Home Automation Hub**: Create a central hub that connects to multiple devices in your home using ESP32's Bluetooth Low Energy (BLE) and Wi-Fi capabilities. This hub can receive commands from a smartphone app and send them to various devices such as lights, thermostats, and security cameras. You can also implement voice control using Google Assistant or Amazon Alexa.
2. **ESP32-based IoT Weather Station**: Build a weather station that collects temperature, humidity, and atmospheric pressure data from sensors and sends it to a cloud platform like AWS or Google Cloud using Wi-Fi. The ESP32 module also connects to a smartphone app via Bluetooth, allowing users to view real-time weather data and receive notifications when conditions change.
3. **Smart Speaker with Voice Assistant**: Develop a smart speaker that integrates Google Assistant or Amazon Alexa using ESP32's Bluetooth capabilities. This speaker can play music, provide information, and control smart devices using voice commands. You can also add Wi-Fi to enable streaming services like Spotify or Apple Music.
4. **BLE-based Indoor Navigation System**: Create an indoor navigation system that uses ESP32's BLE capabilities to create a mesh network of beacons. These beacons provide location information to a smartphone app, allowing users to navigate complex environments like museums, offices, or shopping centers. The system can also be integrated with Wi-Fi to provide navigation information to users without BLE-enabled devices.
5. **IoT-based Vehicle Tracking System**: Design a vehicle tracking system that uses ESP32's Wi-Fi and Bluetooth capabilities to track the location of vehicles in real-time. The system can collect data from GPS, accelerometer, and other sensors and send it to a cloud platform or a smartphone app using Wi-Fi. The ESP32 module also connects to a BLE-enabled device, allowing users to receive alerts and track vehicle locations remotely.

---

### --- Running Prompt 3 ---
* **Prompt Type:** Detailed
* **Prompt Sent:** `I want to build a practical hardware project using an ESP32 development board. Provide 3 comprehensive project concepts focused on home automation or IoT. For each project, please include: a descriptive title, required hardware components, software libraries needed, and potential real-world challenges.`

#### Llama Response:
Here are three comprehensive project concepts focused on home automation or IoT using an ESP32 development board:

**Project 1: Smart Lighting System with RGB Color Control**
* **Descriptive Title:** "ESPSmartLamp - A Wi-Fi Controlled Smart Light Bulb"
* **Required Hardware Components:**
  1. ESP32 Development Board (e.g., ESP32 DevKitC)
  2. RGB LED (e.g., WS2812B or APA102)
  3. Power Supply (e.g., USB Cable or Battery)
  4. Wi-Fi Antenna (optional)
  5. Jumper Wires for connections
* **Software Libraries Needed:**
  1. Arduino IDE (with ESP32 Board Support)
  2. Adafruit_NeoPixel library for RGB LED control
  3. WiFi library (built-in with ESP32 Board Support)
* **Potential Real-World Challenges:**
  1. Color calibration: Ensuring that the RGB LED displays accurate colors.
  2. Brightness control: Maintaining consistent brightness across different color settings.
  3. Network connectivity: Establishing reliable Wi-Fi connections for remote control.

**Project 2: Temperature and Humidity Monitoring with Alert System**
* **Descriptive Title:** "ESPWeatherStation - A Home Weather Monitoring System"
* **Required Hardware Components:**
  1. ESP32 Development Board (e.g., ESP32 DevKitC)
  2. DHT11 or DHT22 Temperature and Humidity Sensor
  3. OLED Display (e.g., SSD1306 or SH1106)
  4. Power Supply (e.g., USB Cable or Battery)
  5. Jumper Wires for connections
* **Software Libraries Needed:**
  1. Arduino IDE (with ESP32 Board Support)
  2. DHT library for temperature and humidity sensing
  3. OLED library (e.g., U8g2 or Adafruit_GFX)
  4. Firebase Realtime Database library (optional) for cloud storage
* **Potential Real-World Challenges:**
  1. Sensor calibration: Ensuring accurate temperature and humidity readings.
  2. Network connectivity: Establishing reliable Wi-Fi connections for data transmission.
  3. Alert system implementation: Designing an effective alert system for temperature or humidity thresholds.

**Project 3: Smart Home Security System with Motion Detection**
* **Descriptive Title:** "ESPSecurityCam - A Motion-Detected Security System"
* **Required Hardware Components:**
  1. ESP32 Development Board (e.g., ESP32 DevKitC)
  2. PIR Motion Sensor (e.g., HC-SR501 or HC-SR505)
  3. Camera Module (e.g., OV7670 or ESP32-CAM)
  4. MicroSD Card for storage
  5. Power Supply (e.g., USB Cable or Battery)
  6. Jumper Wires for connections
* **Software Libraries Needed:**
  1. Arduino IDE (with ESP32 Board Support)
  2. PIR library for motion detection
  3. Camera library (e.g., ESP32-CAM or OV7670)
  4. SD library for microSD card storage
  5. WiFi library (built-in with ESP32 Board Support)
* **Potential Real-World Challenges:**
  1. Motion detection tuning: Adjusting the motion sensor's sensitivity and range.
  2. Camera image quality: Improving image resolution and brightness.
  3. Storage management: Managing microSD card storage for recorded images and videos.

---

### --- Running Prompt 4 ---
* **Prompt Type:** Creative
* **Prompt Sent:** `Imagine it's the year 2045, and the ESP32 is considered vintage tech, but a global power grid failure means we have to rely on low-power mesh networks to survive. Brainstorm 3 sci-fi, 'cyberpunk-survivalist' project ideas that a hobbyist could build using an ESP32 to help their local community. Give them gritty, creative names.`

#### Llama Response:
Here are 3 sci-fi, cyberpunk-survivalist project ideas that a hobbyist could build using an ESP32 to help their local community:

1. **"EchoFlux"**: A low-power mesh network-based emergency alert system that utilizes ESP32 nodes to broadcast critical information to community members. The system would be capable of detecting and alerting people in the event of a grid failure, water contamination, or other life-threatening situations. EchoFlux nodes would be solar-powered, durable, and water-resistant, and could be installed in strategic locations throughout the community.
2. **"GreenSight"**: A community-built sensor network that uses ESP32 modules to monitor local environmental conditions, such as air quality, water quality, and temperature. GreenSight would allow community members to access real-time data on the health of their environment, enabling them to make informed decisions about their daily lives.
3. **"RavenNet"**: A peer-to-peer mesh network that enables community members to share resources, such as food, water, and medical supplies, in the aftermath of a disaster. RavenNet would use ESP32 nodes to facilitate secure, low-power communication between neighbors, allowing them to coordinate relief efforts and prioritize resource allocation.

---

### --- Running Prompt 5 ---
* **Prompt Type:** With Clear Constraints
* **Prompt Sent:** `Generate 3 ESP32 project ideas under the following strict constraints: 1. Must use a camera module or NFC/RFID module, but CANNOT use an SD card reader. 2. Must operate entirely on a local network (LAN) with no external cloud APIs. 3. Output the results in a Markdown table with columns: Project Name, Primary Sensor/Module, and Local Data Handling Method. Do not write any introductory or concluding text.`

#### Llama Response:
| Project Name | Primary Sensor/Module | Local Data Handling Method |
| --- | --- | --- |
| Smart Photo Frame | OV2640 Camera Module | SQLite Database on ESP32 |
| Attendance Tracker | MFRC522 NFC Module | MySQL Database on Raspberry Pi (connected to ESP32) |
| Motion-Triggered Video Recorder | OV7670 Camera Module | Local File System with Logging to Serial Console |

---

## Prompt Performance Comparison & Analysis

### Which prompt gave the best result?
**Prompt 3 (Detailed)** and **Prompt 5 (With Clear Constraints)** yielded the highest-quality, most practical results, depending on your end goal.

* For an actual engineering implementation plan, **Prompt 3** is the best.
* For a highly optimized, targeted development idea session, **Prompt 5** is the best.

### Why?

1. **Precision and Actionability (Prompt 3 vs Prompt 1 & 2):**
   * **Prompt 1 (Basic)** produced a generic list of high-level ideas, many of which are repetitive (e.g., listing a "Weather Station", a "Smart Gardening System", and an "Automated Plant Watering System" as entirely separate projects, or separating "Smart Lighting" and "Home Automation").
   * **Prompt 2 (Improved)** forced the model to leverage dual radios (Wi-Fi + BLE), but the project scopes remained vague.
   * **Prompt 3 (Detailed)** forced the model to deliver a practical blueprint. It provided actionable information (specifying real chips like the `WS2812B` and libraries like `Adafruit_NeoPixel`), and accurately called out critical embedded bottlenecks like *sensor calibration* and *local storage limits*.

2. **Strict Adherence to Logical Architecture (Prompt 5):**
   * Small LLMs like Llama 3.1 8B frequently fall back on "uploading to AWS/Firebase" or "saving to an SD Card" whenever a camera module is mentioned. By forcing strict negative constraints (*"CANNOT use an SD card reader"*, *"no external cloud APIs"*), Prompt 5 forced the model to think like a true local-network edge systems engineer.
   * The model adapted correctly by suggesting a local **SQLite instance on the ESP32**, offloading to a **local Raspberry Pi via LAN**, or streaming directly over the **Serial console interface**. 
   * It also flawlessly executed the structural layout constraints (raw Markdown table output without any conversational filler phrases).