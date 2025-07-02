# Alarm-Clock

Custom built alarm clock. I was partly inspired by this https://busy.bar/. I also just wanted ot make a cool custom project and right now I only have an Alexa next to my bed so I can't actually see the current time, but with this it should both wake me up and it should tell me the time :) 

What this basically is its an ESP32 controlled alarm clock that connects to Wifi has a 1.9" LCD display and a snooze bar. It serves as a clock and an alarm (as of now, but I want to program it a bit more in the future!)

When I first learned about making PCBs this (along with a keyboard [which I already made!]) was one of the projects I wanted to try my hand at so I am happy I got to do it!

# Photos

![image](https://github.com/user-attachments/assets/4e5bb61c-47e1-4444-8f99-453aa80d3cd4)
![image](https://github.com/user-attachments/assets/80e9fbce-8971-47c7-9332-39027cc3fba1)
![image](https://github.com/user-attachments/assets/a8e63787-a606-4243-9073-25941b7e3b01)
![image](https://github.com/user-attachments/assets/1c70145e-44f7-451b-9ec1-bf2e765dd925)

# BOM

| Item                | Quantity Used   | Quantity Purchased   | Designator   | Part Number / Description   | Link       | Cost   |
|:--------------------|:----------------|:---------------------|:-------------|:----------------------------|:-----------|:-------|
| Case                | 1.0             |                      |              | Custom Case                 |            |        |
| PCB                 | 1.0             | 5.0                  |              | Custom PCB                  |            | $8.90  |
| JST Connector       | 4.0             | 5.0                  |              | JST-XH-A 5                  | LCSC       | $0.42  |
| JST Connector       | 2.0             | 5.0                  |              | JST-XH-A 8                  | LCSC       | $0.66  |
| MCU                 | 1.0             | 1.0                  |              | ESP-32-S3-MINI-1            | LCSC       | $5.11  |
| Buzzer              | 2.0             | 5.0                  |              | TMB12A05                    | LCSC       | $0.90  |
| Capacitor           | 1.0             | 100.0                | C1           | 0603 1uF (100nF)            | LCSC       | $0.24  |
| USB Connector       | 1.0             | 1.0                  | J1           | USB-C USB4105-GF-A          | LCSC       | $1.16  |
| LCD Display         | 1.0             | 10.0                 |              | 1.9" LCD                    | AliExpress | $3.25  |
| Diodes              | 2.0             | 10.0                 |              | 40V 200mA NPN TO-92         | LCSC       | $0.38  |
| Resistor            | 1.0             | 100.0                | R1           | 10k Ohm 0603                | LCSC       | $0.11  |
| Resistor            | 2.0             | 100.0                | R2, R3       | 5.1k Ohm 0603               | LCSC       | $0.12  |
| Resistor            | 2.0             | 100.0                | R4, R5       | 1k Ohm 0603                 | LCSC       | $0.11  |
| Switch              | 1.0             | 10.0                 | SW1          | Gateron Low Profile         | AliExpress | $5.79  |
| Encoder             | 1.0             | 5.0                  | ENC1         | EC11 Rotary Encoder         | AliExpress | $0.99  |
| Voltage Regulator   | 1.0             | 5.0                  | U1           | AMS1117-3.3                 | LCSC       | $0.87  |
| Shipping JLC PCB    |                 |                      |              |                             |            | $22.73 |
| Shipping LCSC       |                 |                      |              |                             |            | $17.39 |
| Shipping Aliexpress |                 |                      |              |                             |            | $0.00  |
|                     |                 |                      |              |                             |            | $69.13 |
