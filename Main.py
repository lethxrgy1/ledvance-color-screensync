import numpy as np
from PIL import ImageGrab
import tinytuya
import time
from collections import Counter
import colorsys

def capture_screen():
    return ImageGrab.grab()

def find_dominant_color(image, resize=(100, 100)):
    image = image.resize(resize)
    np_image = np.array(image)
    pixels = np_image.reshape(-1, np_image.shape[-1])
    color_count = Counter(map(tuple, pixels))
    dominant_color = color_count.most_common(1)[0][0]
    return dominant_color

def setup_bulb(device_id, ip, local_key):
    bulb = tinytuya.BulbDevice(device_id, ip, local_key)
    bulb.set_version(3.4)
    bulb.set_socketPersistent(True)
    return bulb

def enhance_color_saturation(r, g, b):
    r_scaled, g_scaled, b_scaled = r / 255.0, g / 255.0, b / 255.0
    h, s, v = colorsys.rgb_to_hsv(r_scaled, g_scaled, b_scaled)
    s = min(s * 1.5, 1.0)  # Increase saturation
    r_enhanced, g_enhanced, b_enhanced = colorsys.hsv_to_rgb(h, s, v)
    return int(r_enhanced * 255), int(g_enhanced * 255), int(b_enhanced * 255)

def rgb_to_hsv_scaled(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h_scaled = int(h * 360)
    s_scaled = int(s * 1000)
    v_scaled = int(v * 1000)
    return h_scaled, s_scaled, v_scaled

def set_bulb_color(bulb, r, g, b):
    # Convert RGB to HSV and scale HSV to bulb's expected range
    r_scaled, g_scaled, b_scaled = r / 255.0, g / 255.0, b / 255.0
    h, s, v = colorsys.rgb_to_hsv(r_scaled, g_scaled, b_scaled)
    h_scaled = int(h * 360)
    s_scaled = int(s * 1000)
    v_scaled = int(v * 1000)  # Ensure this variable is defined in this scope

    print(f"Debug - RGB: ({r}, {g}, {b}), Scaled HSV: ({h_scaled}, {s_scaled}, {v_scaled})")

    # Check for mostly black screen and adjust brightness to the lowest
    if max(r, g, b) < 10:
        print("Debug - Screen is mostly black, dimming bulb.")
        bulb.set_mode('white')
        bulb.set_value(22, 10)  # Assuming 10 is the lowest brightness value for dimming without turning off
        return

    # Determine action based on saturation
    if s_scaled < 100:  # If the saturation suggests a near-white color
        print("Debug - Setting to white mode with low saturation")
        bulb.set_mode('white')
        bulb.set_value(22, v_scaled)  # Use the correctly defined v_scaled here
    else:
        # Enhance color saturation for vivid colors outside of near-white or black conditions
        r_enhanced, g_enhanced, b_enhanced = enhance_color_saturation(r, g, b)
        print(f"Debug - Setting color using enhanced RGB: ({r_enhanced}, {g_enhanced}, {b_enhanced})")
        bulb.set_mode('colour')
        bulb.set_colour(r_enhanced, g_enhanced, b_enhanced)  # Apply enhanced RGB values

def main():
    device_id = 'bf180ec1fdb57452dfnbak'
    ip_address = '192.168.1.109'
    local_key = '&-~*@2Q+dwZ*RR!E'

    bulb = setup_bulb(device_id, ip_address, local_key)

    while True:
        screen_image = capture_screen()
        dominant_color = find_dominant_color(screen_image)
        rgb_dominant_color = dominant_color[:3]  # Use only RGB values
        set_bulb_color(bulb, *rgb_dominant_color)
        time.sleep(1)

if __name__ == "__main__":
    main()
