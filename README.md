# 🚰 HydraSense Automation

> **Smart Water-Level Monitoring & Automated Refill System for Humidifiers**  
> Powered by Ultrasonic Sensor, Relay, OLED Display & NeoPixel LEDs  

---

![GitHub Repo stars](https://img.shields.io/github/stars/yourusername/hydrasense-automation?style=social) ![GitHub forks](https://img.shields.io/github/forks/yourusername/hydrasense-automation?style=social) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## 📋 Table of Contents  
- [✨ Introduction](#-introduction)  
- [⚙️ Features](#-features)  
- [🧩 Components Used](#-components-used)  
- [🔧 How It Works](#-how-it-works)  
- [🚀 Installation](#-installation)  
- [🎛️ Usage](#-usage)  
- [👍 Advantages](#-advantages)  
- [🔮 Future Scope](#-future-scope)  
- [🤝 Contributing](#-contributing)  
- [📄 License](#-license)  

---

## ✨ Introduction  
HydraSense Automation is a smart home automation project that **automatically monitors and refills water** in your humidifier or water tank. Using an ultrasonic sensor to detect water levels, it controls a solenoid valve via a relay, ensuring a spill-free, hassle-free operation with real-time visual feedback on an OLED display and NeoPixel LEDs.

---

## ⚙️ Features  
- 🌊 Real-time water level measurement using ultrasonic sensor  
- 🔄 Automated refill via relay-controlled solenoid valve  
- 📟 OLED display showing water level & system status  
- 🌈 NeoPixel LED strip for smooth water-level animations  
- ⚠️ Error detection & alerts for sensor issues  
- 🛑 Safety stop to prevent overflow  

---

## 🧩 Components Used  

| Component          | Model/Type           | Quantity | Purpose                             |  
|--------------------|----------------------|----------|-----------------------------------|  
| 🧠 Microcontroller  | Arduino Uno (or similar) | 1        | Core control & processing          |  
| 🌀 Ultrasonic Sensor | HC-SR04               | 1        | Measures water level distance       |  
| 🔌 Relay Module     | 5V Relay              | 1        | Controls solenoid valve power       |  
| 🚰 Solenoid Valve   | 12V DC Valve          | 1        | Controls water refill flow          |  
| 📺 OLED Display     | SH1106 0.96 inch      | 1        | Displays water level and status     |  
| 🌈 NeoPixel LEDs    | WS2812B (19 LEDs)     | 1        | Visual water level indicator        |  
| ⚡ Power Supply     | 5V/12V (as needed)    | 1        | Powers all components               |  

---

## 🔧 How It Works  
1. 📏 Ultrasonic sensor sends pulses and measures echo time to find water distance.  
2. 📊 Converts distance to water level percentage.  
3. 💧 If water level < threshold, relay switches ON solenoid valve to refill.  
4. 🖥 OLED shows current level, refill status, and warnings.  
5. 🌈 NeoPixel LEDs animate water level with smooth color gradients.  
6. 🛑 Stops refill automatically at max water level.  
7. 🚨 Error alerts shown on OLED & LEDs if sensor data is abnormal.  

---

## 🚀 Installation  
1. 🔗 Connect components as per wiring diagram (included in repo).  
2. 💾 Upload `HydraSense_Automation.ino` to your Arduino board.  
3. 🔌 Power the system and verify functionality via OLED and LEDs.  

---

## 🎛️ Usage  
- Place the ultrasonic sensor above your humidifier’s water tank.  
- Connect relay and solenoid valve correctly for refill control.  
- Watch the OLED display & NeoPixel strip for live water level updates.  
- System runs autonomously to maintain water levels and avoid overflow.  

---

## 👍 Advantages  
- ⏳ Saves time with automated water refilling.  
- 🚫 Prevents water spillage & overflow accidents.  
- 👁 Real-time visual feedback enhances user interaction.  
- 🔄 Modular & expandable for future upgrades.  

---

## 🔮 Future Scope  
- 📡 Add Wi-Fi/Bluetooth for remote monitoring & notifications.  
- 📱 Mobile app integration for alerts & control.  
- 💧 Extend for multi-tank or industrial water management.  
- 🔋 Power-saving modes for battery-powered setups.  

---

## 🤝 Contributing  
Contributions and suggestions are welcome! Feel free to fork, improve, and send pull requests.  

---

## 📄 License  
This project is licensed under the [MIT License](LICENSE).  

---

# ⚡ Happy Automating with HydraSense! ⚡
