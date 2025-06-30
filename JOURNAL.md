---
title: "Alarm Clock"
author: "John"
description: "Alarm clock with an LCD display and a speaker."
created_at: "2025-06-04"
---

# June 26th
Its important to me that this thing is kinda cools so I am thinking of some features I want it to have
- google calendar integration where it wakes me up 30 minutes before the first event on my calendar
- Gives me a preview of my day and everything I gotta do (all the stuff on my calendar)

Still thinking of some features but planning on writing those as I go

# June 29th
Haven't updated in a while but i finished my schematic so far and my pcb. The design is currently 4 different pcb modules which will all be connected by cables so I can create a "3d case." One module for the main board with the ESP32-s3-mini, another one for the snooze button, and 2 rotary encoders.

I am in a bit of a rush to get the invite to highway, but yeah.

![](https://github.com/jpt1729/Alarm-Clock/blob/main/photos/schematic-6-29-2025.png?raw=true)
![](https://github.com/jpt1729/Alarm-Clock/blob/main/photos/PCB-6-29-2025.png?raw=true)

The PCB has some errors and for some reason says I need to connect the ground even though there is a powerflag, but those are issues I feel fine ignoring lol.

I am starting to work on the case in fusion360.

# June 30th

I've been starting to work on the case and I realised that 2 ec11 encoders doesn't really make any sense and that the current structure makes the clock look werid lol.

I have to do some redesign to support the buzzer which will wake me up. Its going to be on the snooze bar and there will be 2 big of them.

I also made a mistake and accidentally deleted the correct copy of the pcb 🤦‍♂️🤦‍♂️🤦‍♂️ so now I gotta redo some sizing changes and stuff.

![image](https://github.com/user-attachments/assets/c1908e37-8d26-4349-a8ea-e5550934ca8f)
![image](https://github.com/user-attachments/assets/e3f39c6e-8c78-4c0e-915d-c89c86d6700a)

Here is the before. As you can see the dial on the side is just too tall this is because I had 2 screws to secure it. Now it is only one with a hook at the top to make sure it doesn't moove and shake around.

Here it is now! I like the cases structure and how it looks ngl.
![image](https://github.com/user-attachments/assets/ff4bed27-d774-4eb3-8080-7569e63502f8)

Some stuff I added are beepers to help me actually wake up they are placed on the snooze button (Not sure if you can see them but they are there)
After this, I have only the hard part which is just making the code!

