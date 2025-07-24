# Alarm-Clock

Custom built alarm clock. I was partly inspired by this https://busy.bar/. I also just wanted ot make a cool custom project and right now I only have an Alexa next to my bed so I can't actually see the current time, but with this it should both wake me up and it should tell me the time :) 

What this basically is its an ESP32 controlled alarm clock that connects to Wifi has a 1.9" LCD display and a snooze bar. It serves as a clock and an alarm (as of now, but I want to program it a bit more in the future!)

When I first learned about making PCBs this (along with a keyboard [which I already made!]) was one of the projects I wanted to try my hand at so I am happy I got to do it!

The plan to make the case a bit easier to print is to print the top part out and then the bottom part out and connect the two with a soldering iron. This will use a lot less plastic (if not I will basically be printing a solid block of plastic).

# Photos

![image](https://github.com/user-attachments/assets/4e5bb61c-47e1-4444-8f99-453aa80d3cd4)
![image](https://github.com/user-attachments/assets/80e9fbce-8971-47c7-9332-39027cc3fba1)
![image](https://github.com/user-attachments/assets/a8e63787-a606-4243-9073-25941b7e3b01)
![image](https://github.com/user-attachments/assets/1c70145e-44f7-451b-9ec1-bf2e765dd925)

# BOM

| Item | Quantity Used | Quantity Purchased | Designator | Part Number / Description | Link | Cost |
|------|--------------|-------------------|------------|--------------------------|------|------|
| Case | 1 | | | Custom Case | | |
| PCB | 1 | 5 | | Custom PCB | | $8.90 |
| JST Connector | 4 | 5 | | JST-XH-A 5 | [LCSC](https://lcsc.com/product-detail/Wire-To-Board-Connector_JST-B5B-XH-A-LF-SN_C157991.html) | $0.42 |
| JST Connector | 2 | 5 | | JST-XH-A 8 | [LCSC](https://lcsc.com/product-detail/Wire-To-Board-Connector_JST-B8B-XH-A-LF-SN_C157972.html) | $0.66 |
| MCU | 1 | 1 | | ESP-32-S3-MINI-1 | [LCSC](https://lcsc.com/product-detail/WiFi-Modules_Espressif-Systems-ESP32-S3-MINI-1-N8_C2913206.html) | $5.11 |
| Buzzer | 2 | 5 | | TMB12A05 | [LCSC](https://lcsc.com/product-detail/Buzzers_Jiangsu-Huaneng-Elec-TMB12A05_C96093.html) | $0.90 |
| Capacitor | 1 | 100 | C1 | 0603 1uF (100nF) | [LCSC](https://lcsc.com/product-detail/image/CC0603KRX7R9BB104_C14663.html) | $0.24 |
| USB Connector | 1 | 1 | J1 | USB-C USB4105-GF-A | [LCSC](https://lcsc.com/product-detail/USB-Connectors_Global-Connector-Technology-USB4105-GF-A_C3020560.html) | $1.16 |
| LCD Display | 1 | 10 | | 1.9" LCD | [AliExpress](https://www.aliexpress.us/item/3256807182983606.html) | $3.25 |
| Diodes | 2 | 10 | | 40V 200mA NPN TO-92 | [LCSC](https://lcsc.com/product-detail/image/2N3904X_C5156722.html) | $0.38 |
| Resistor | 1 | 100 | R1 | 10k Ohm 0603 | [LCSC](https://lcsc.com/product-detail/image/RC0603FR-0710KL_C98220.html) | $0.11 |
| Resistor | 2 | 100 | R2, R3 | 5.1k Ohm 0603 | [LCSC](https://lcsc.com/product-detail/image/RC0603FR-075K1L_C105580.html) | $0.12 |
| Resistor | 2 | 100 | R4, R5 | 1k Ohm 0603 | [LCSC](https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_YAGEO-RC0603FR-071KL_C22548.html) | $0.11 |
| Switch | 1 | 10 | SW1 | Gateron Low Profile | [AliExpress](https://www.aliexpress.us/item/3256808635477539.html) | $5.79 |
| Encoder | 1 | 5 | ENC1 | EC11 Rotary Encoder | [AliExpress](https://www.aliexpress.us/item/3256801237549169.html) | $0.99 |
| Voltage Regulator | 1 | 5 | U1 | AMS1117-3.3 | [LCSC](https://lcsc.com/product-detail/Voltage-Regulators-Linear-Low-Drop-Out-LDO-Regulators_Advanced-Monolithic-Systems-AMS1117-3-3_C6186.html) | $0.87 |
| SXH-001T-P0.6 | | 100 | | Terminal pin (x100) | [LCSC](https://lcsc.com/product-detail/Housing-Contact_JST-SXH-001T-P0-6_C140573.html) | $1.08 |
| XHP-5 | | 20 | | 5-pin housing (x20) | [LCSC](https://lcsc.com/product-detail/Housings-Wire-To-Board-Wire-To-Wire_JST-XHP-5_C144404.html) | $0.46 |
| XHP-8 | | 20 | | 8-pin housing (x20) | [LCSC](https://lcsc.com/product-detail/Housings-Wire-To-Board-Wire-To-Wire_JST-XHP-8_C144407.html) | $0.65 |
| Connector Kit (Amazon) | | | | SXH-001T-P0.6, XHP-5, XHP-8 Assortment | [Amazon](https://a.co/d/gTI01NR) | $6.97 |
| Shipping JLC PCB | | | | | | $22.73 |
| Shipping LCSC | | | | | | $17.39 |
| Shipping AliExpress | | | | | | $0.00 |
| Hotplate | 1 | 1 | | Soldering Hotplate | [AliExpress](https://www.aliexpress.us/item/3256806325004979.html) | $20.05 |
| **Total** | | | | | | **$77.72** |

