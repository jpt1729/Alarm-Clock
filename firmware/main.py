import board
import displayio
import terminalio
from adafruit_display_text import label
from fourwire import FourWire
from adafruit_st7789 import ST7789
import time
import rtc
import digitalio
import rotaryio
import wifi
import socketpool
import adafruit_ntp

# Release any resources currently in use for the displays
displayio.release_displays()

# WiFi Configuration
WIFI_SSID = "YOUR_WIFI_SSID"  # TODO: Update with your WiFi name
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"  # TODO: Update with your WiFi password

# Setup buzzer
buzzer = digitalio.DigitalInOut(board.IO42)
buzzer.direction = digitalio.Direction.OUTPUT
buzzer.value = False  # Start with buzzer off

# Setup buttons
alarm_set_button = digitalio.DigitalInOut(board.IO3)
alarm_set_button.direction = digitalio.Direction.INPUT
alarm_set_button.pull = digitalio.Pull.UP

snooze_button = digitalio.DigitalInOut(board.IO2)
snooze_button.direction = digitalio.Direction.INPUT
snooze_button.pull = digitalio.Pull.UP

# Setup encoder
encoder = rotaryio.IncrementalEncoder(board.IO8, board.IO9)

spi = board.SPI()
tft_cs = board.IO40
tft_dc = board.IO39
tft_rst = board.IO41 

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

display = ST7789(display_bus, width=320, height=170, colstart=35, rotation=90)

# Make the display context
splash = displayio.Group()
display.root_group = splash

# Initialize RTC
rtc_instance = rtc.RTC()

# Set initial time (will be updated by NTP)
# Format: (year, month, day, hour, minute, second, weekday, yearday)
rtc_instance.datetime = time.struct_time((2024, 1, 1, 12, 0, 0, 0, 1, -1))

# Alarm variables
alarm_hour = 7
alarm_minute = 0
alarm_enabled = False
alarm_ringing = False
snooze_time = None
snooze_duration = 9 * 60  # 9 minutes in seconds

# Display mode
setting_alarm = False
setting_hour = True  # True for hour, False for minute

# WiFi and sync variables
wifi_connected = False
last_sync = 0
sync_interval = 3600  # Sync every hour

# Create time label
time_label = label.Label(
    terminalio.FONT,
    text="",
    color=0xFFFFFF,  # White text
    scale=4,
    anchor_point=(0.5, 0.5),
    anchored_position=(display.width // 2, display.height // 2),
)
splash.append(time_label)

# Create date label (smaller, below time)
date_label = label.Label(
    terminalio.FONT,
    text="",
    color=0xFFFFFF,  # White text
    scale=2,
    anchor_point=(0.5, 0.5),
    anchored_position=(display.width // 2, display.height // 2 + 80),
)
splash.append(date_label)

# Create alarm status label
alarm_label = label.Label(
    terminalio.FONT,
    text="",
    color=0x00FF00,  # Green text
    scale=1,
    anchor_point=(0.5, 0.5),
    anchored_position=(display.width // 2, 20),
)
splash.append(alarm_label)

def connect_wifi():
    """Connect to WiFi and sync time with NTP"""
    try:
        # Show connecting message
        time_label.text = "Connecting..."
        date_label.text = "to WiFi"
        alarm_label.text = ""
        
        # Connect to WiFi
        wifi.radio.start_ap("AlarmClock", "password123")
        wifi.radio.stop_ap()
        wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
        
        # Show connected message
        time_label.text = "Connected!"
        date_label.text = "Syncing time..."
        time.sleep(1)
        
        # Setup NTP
        pool = socketpool.SocketPool(wifi.radio)
        ntp = adafruit_ntp.NTP(pool, tz_offset=-6)  # CST timezone
        
        # Get time from NTP
        ntp_time = ntp.datetime
        rtc_instance.datetime = ntp_time
        
        # Show success message
        time_label.text = "Time Synced!"
        date_label.text = format_date(rtc_instance.datetime)
        time.sleep(2)
        
        return True
        
    except Exception as e:
        # Show error message
        time_label.text = "WiFi Error"
        date_label.text = "Check settings"
        alarm_label.text = str(e)[:20]  # Show first 20 chars of error
        time.sleep(3)
        return False

def sync_time():
    """Sync time with NTP server"""
    try:
        pool = socketpool.SocketPool(wifi.radio)
        ntp = adafruit_ntp.NTP(pool, tz_offset=0)  # Change 0 to your timezone
        ntp_time = ntp.datetime
        rtc_instance.datetime = ntp_time
        return True
    except:
        return False

def turn_buzzer_on():
    """Turn on the buzzer"""
    buzzer.value = True

def turn_buzzer_off():
    """Turn off the buzzer"""
    buzzer.value = False

def buzz_alarm(duration=5):
    """Buzz the alarm for a specified duration in seconds"""
    turn_buzzer_on()
    time.sleep(duration)
    turn_buzzer_off()

def format_time(t):
    """Format time as HH:MM AM/PM"""
    hour = t.tm_hour
    minute = t.tm_min
    
    # Convert to 12-hour format
    if hour == 0:
        hour = 12
        ampm = "AM"
    elif hour < 12:
        ampm = "AM"
    elif hour == 12:
        ampm = "PM"
    else:
        hour -= 12
        ampm = "PM"
    
    return f"{hour:02d}:{minute:02d} {ampm}"

def format_date(t):
    """Format date as Month DD, YYYY"""
    months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{months[t.tm_mon]} {t.tm_mday}, {t.tm_year}"

def format_alarm_time():
    """Format alarm time as HH:MM AM/PM"""
    hour = alarm_hour
    minute = alarm_minute
    
    # Convert to 12-hour format
    if hour == 0:
        hour = 12
        ampm = "AM"
    elif hour < 12:
        ampm = "AM"
    elif hour == 12:
        ampm = "PM"
    else:
        hour -= 12
        ampm = "PM"
    
    return f"{hour:02d}:{minute:02d} {ampm}"

def check_alarm():
    """Check if alarm should go off"""
    global alarm_ringing, snooze_time
    
    if not alarm_enabled and snooze_time is None:
        return
    
    now = rtc_instance.datetime
    current_time = now.tm_hour * 60 + now.tm_min
    
    # Check regular alarm
    if alarm_enabled and not alarm_ringing:
        alarm_time = alarm_hour * 60 + alarm_minute
        if current_time == alarm_time and now.tm_sec == 0:
            alarm_ringing = True
            turn_buzzer_on()
    
    # Check snooze alarm
    if snooze_time is not None and not alarm_ringing:
        snooze_hour = snooze_time // 60
        snooze_minute = snooze_time % 60
        snooze_current = snooze_hour * 60 + snooze_minute
        if current_time == snooze_current and now.tm_sec == 0:
            alarm_ringing = True
            turn_buzzer_on()

def handle_buttons():
    """Handle button presses"""
    global setting_alarm, setting_hour, alarm_enabled, alarm_ringing, snooze_time
    
    # Alarm set button (first button)
    if not alarm_set_button.value:  # Button pressed (active low)
        time.sleep(0.1)  # Debounce
        if not alarm_set_button.value:
            if alarm_ringing:
                # Turn off alarm
                alarm_ringing = False
                turn_buzzer_off()
                snooze_time = None
            elif not setting_alarm:
                # Enter alarm setting mode
                setting_alarm = True
                setting_hour = True
            else:
                # Toggle between hour and minute setting
                if setting_hour:
                    setting_hour = False
                else:
                    # Exit alarm setting mode and enable alarm
                    setting_alarm = False
                    alarm_enabled = True
    
    # Snooze button (second button)
    if not snooze_button.value:  # Button pressed (active low)
        time.sleep(0.1)  # Debounce
        if not snooze_button.value:
            if alarm_ringing:
                # Snooze for 9 minutes
                alarm_ringing = False
                turn_buzzer_off()
                now = rtc_instance.datetime
                current_minutes = now.tm_hour * 60 + now.tm_min
                snooze_time = (current_minutes + 9) % (24 * 60)  # Wrap around midnight

def handle_encoder():
    """Handle encoder rotation for alarm setting"""
    global alarm_hour, alarm_minute
    
    if not setting_alarm:
        return
    
    position = encoder.position
    encoder.position = 0  # Reset position
    
    if position != 0:
        if setting_hour:
            # Adjust hour
            alarm_hour = (alarm_hour + position) % 24
        else:
            # Adjust minute
            alarm_minute = (alarm_minute + position) % 60

def update_display():
    """Update the display with current information"""
    now = rtc_instance.datetime
    
    if setting_alarm:
        # Show alarm setting mode
        if setting_hour:
            time_label.text = f"Set Hour: {alarm_hour:02d}"
        else:
            time_label.text = f"Set Min: {alarm_minute:02d}"
        date_label.text = f"Alarm: {format_alarm_time()}"
        alarm_label.text = "SETTING ALARM"
    else:
        # Show normal time
        time_label.text = format_time(now)
        date_label.text = format_date(now)
        
        if alarm_ringing:
            alarm_label.text = "ALARM!"
        elif alarm_enabled:
            alarm_label.text = f"Alarm: {format_alarm_time()}"
        elif snooze_time is not None:
            snooze_hour = snooze_time // 60
            snooze_minute = snooze_time % 60
            alarm_label.text = f"Snooze: {snooze_hour:02d}:{snooze_minute:02d}"
        else:
            alarm_label.text = "No Alarm Set"

last_update = 0
update_interval = 1  # Update every second

# Initial WiFi connection and time sync
wifi_connected = connect_wifi()

while True:
    current_time = time.time()
    
    # Periodic time sync (every hour)
    if wifi_connected and (current_time - last_sync) >= sync_interval:
        if sync_time():
            last_sync = current_time
    
    # Handle input
    handle_buttons()
    handle_encoder()
    
    # Check alarm
    check_alarm()
    
    # Update display every second
    if current_time - last_update >= update_interval:
        update_display()
        last_update = current_time
    
    time.sleep(0.1)  # Small delay to prevent excessive CPU usage