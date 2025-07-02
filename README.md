# Alarm-Clock

Custom built alarm clock. I was partly inspired by this https://busy.bar/. I also just wanted ot make a cool custom project and right now I only have an Alexa next to my bed so I can't actually see the current time, but with this it should both wake me up and it should tell me the time :) 

What this basically is its an ESP32 controlled alarm clock that connects to Wifi has a 1.9" LCD display and a snooze bar. It serves as a clock and an alarm (as of now, but I want to program it a bit more in the future!)

When I first learned about making PCBs this (along with a keyboard [which I already made!]) was one of the projects I wanted to try my hand at so I am happy I got to do it!

# Photos

![image](https://github.com/user-attachments/assets/4e5bb61c-47e1-4444-8f99-453aa80d3cd4)
![image](https://github.com/user-attachments/assets/80e9fbce-8971-47c7-9332-39027cc3fba1)
![image](https://github.com/user-attachments/assets/a8e63787-a606-4243-9073-25941b7e3b01)

# BOM

| Item                 | Quantity | Designator | Part Number / Description | Link                                                                                                                              |
|----------------------|----------|------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Case                 | 1        |            | Custom Case               |                                                                                                                                   |
| PCB                  | 1        |            | Custom PCB                |                                                                                                                                   |
| JST Connector        | 4        |            | JST-XH-A 5                | [LCSC](https://lcsc.com/product-detail/Wire-To-Board-Connector_JST-B5B-XH-A-LF-SN_C157991.html)                                     |
| JST Connector        | 2        |            | JST-XH-A 8                | [LCSC](https://www.google.com/search?q=https://lcsc.com/product-detail/Wire-To-Board-Connector_JST-B8B-XH-A-LF-SN_C157972.html) |
| MCU                  | 1        |            | ESP-32-S3-MINI-1          | [LCSC](https://lcsc.com/product-detail/WiFi-Modules_Espressif-Systems-ESP32-S3-MINI-1-N8_C2913206.html)                             |
| Buzzer               | 2        |            | TMB12A05                  | [LCSC](https://lcsc.com/product-detail/Buzzers_Jiangsu-Huaneng-Elec-TMB12A05_C96093.html)                                           |
| Capacitor            | 1        | C1         | 0603 1uF (100nF)          | [LCSC](https://lcsc.com/product-detail/image/CC0603KRX7R9BB104_C14663.html)                                                        |
| USB Connector        | 1        | J1         | USB-C USB4105-GF-A        | [LCSC](https://www.google.com/search?q=https://lcsc.com/product-detail/USB-Connectors_Global-Connector-Technology-USB4105-GF-A_C3020560.html) |
| LCD Display          | 1        |            | 1.9" LCD                  | [AliExpress](https://www.aliexpress.us/item/3256807182983606.html)                                                                 |
| Diode                | 2        | D1, D2     | 2N3904                    | [LCSC](https://lcsc.com/product-detail/image/2N3904X_C5156722.html)                                                                |
| Resistor             | 1        | R1         | 10k Ohm 0603              | [LCSC](https://lcsc.com/product-detail/image/RC0603FR-0710KL_C98220.html)                                                          |
| Resistor             | 2        | R2, R3     | 5.1k Ohm 0603             | [LCSC](https://lcsc.com/product-detail/image/RC0603FR-075K1L_C105580.html)                                                         |
| Resistor             | 2        | R4, R5     | 1k Ohm 0603               | [LCSC](https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_YAGEO-RC0603FR-071KL_C22548.html)                                |
| Switch               | 1        | SW1        | Gateron Low Profile       | [AliExpress](https://www.aliexpress.us/item/3256808635477539.html)                                                                 |
| Encoder              | 1        | ENC1       | EC11 Rotary Encoder       | [AliExpress](https://www.aliexpress.us/item/3256801237549169.html)                                                                 |
| Voltage Regulator    | 1        | U1         | AMS1117-3.3               | [LCSC](https://lcsc.com/product-detail/Voltage-Regulators-Linear-Low-Drop-Out-LDO-Regulators_Advanced-Monolithic-Systems-AMS1117-3-3_C6186.html) |

- 1x case
- 1x PCB
- connectors:
- - x4 JST-XH-A 5 https://lcsc.com/product-detail/Wire-To-Board-Connector_JST-B5B-XH-A-LF-SN_C157991.html?s_z=n_B5B-XH-A
- - x2 JS-XH-A 8 https://lcsc.com/product-detail/Wire-To-Board-Connector_JST-B8B-XH-A-LF-SN_C157972.html?s_z=n_B8B-XH-A
- x1 ESP-32-S3-MINI-1 https://lcsc.com/product-detail/WiFi-Modules_Espressif-Systems-ESP32-S3-MINI-1-N8_C2913206.html?s_z=n_ESP32-S3-MINI-1
- x2 Buzzers https://lcsc.com/product-detail/Buzzers_Jiangsu-Huaneng-Elec-TMB12A05_C96093.html?s_z=n_Buzzer_12x9.5RM7.6
- x1 0603 1uF (100nF) capacitor https://lcsc.com/product-detail/image/CC0603KRX7R9BB104_C14663.html
- x1 USB-C connector https://lcsc.com/product-detail/USB-Connectors_Global-Connector-Technology-USB4105-GF-A_C3020560.html?s_z=n_USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal
- 1x 1.9" LCD display https://www.aliexpress.us/item/3256807182983606.html
- 2x 2N3904 Diodes https://lcsc.com/product-detail/image/2N3904X_C5156722.html
- 1x 10k ohm resistor https://lcsc.com/product-detail/image/RC0603FR-0710KL_C98220.html
- 2x 5.1k Ohm resistor https://lcsc.com/product-detail/image/RC0603FR-075K1L_C105580.html
- 2x 1k Ohm resistor https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_YAGEO-RC0603FR-071KL_C22548.html?s_z=n_resistor
- 1x Gateron low profile switch https://www.aliexpress.us/item/3256808635477539.html
- 1x ec11 encoder https://www.aliexpress.us/item/3256801237549169.html
- 1x AMS1117 https://lcsc.com/product-detail/Voltage-Regulators-Linear-Low-Drop-Out-LDO-Regulators_Advanced-Monolithic-Systems-AMS1117-3-3_C6186.html?s_z=n_AMS1117

