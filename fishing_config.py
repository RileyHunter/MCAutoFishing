# Needs to match GUI scale from in-game
# Default: 4 (matches in-game default of Auto at standard res)
gui_scale = 4

# Fishing timings:
# From splash to reel-in.
# Default: 0.1
time_to_reel = 0.1
# From reel-in to recast
# Default: 0.1
time_to_recast = 0.4
# From recast to starting to check subtitles for splash
# Default: 1
time_to_pause_sampling = 1

# Sampling frequency
# Turn up for faster responses, higher CPU load and vice-versa
# Default: 5
sample_per_second = 5 

# If True, overrides the window-finding behaviour and assumes
# a 1920x1040 (fullscreen windowed) MC window on monitor 1,
# or other values should you specify them below.
# Useful for tricky multi-monitor setups or if you're running multiple MC windows.
# Default: False
override_resolution = False
# Vals for override
override_top_left_x = 0
override_top_left_y = 0
override_bottom_right_x = 1920
override_bottom_right_y = 1040