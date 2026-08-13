"""
=========================================================
CONFIGURATION FILE
EOG Based 3D Target Selection
=========================================================
"""

# =====================================================
# SERIAL
# =====================================================

COM_PORT = "COM17"
BAUD_RATE = 115200

#compatibility 
PORT = COM_PORT
BAUD = BAUD_RATE

BUFFER_SIZE = 500
# =====================================================
# SAMPLING
# =====================================================

FS = 250

# =====================================================
# FILTERS
# =====================================================

NOTCH_FREQ = 50
NOTCH_Q = 30

LOWCUT = 0.1
HIGHCUT = 10

FILTER_ORDER = 4

# =====================================================
# KALMAN FILTER
# =====================================================

KALMAN_Q = 0.001
KALMAN_R = 2.0

# =====================================================
# CALIBRATION
# =====================================================

CALIBRATION_WAIT = 2.0
CALIBRATION_TIME = 3.0

# =====================================================
# EYE DETECTOR
# =====================================================

MIN_DEADZONE = 120

CENTER_LOCK = 40

CENTER_HYSTERESIS = 25

MAX_VELOCITY = 6

SMOOTHING = 0.30

# =====================================================
# BLINK DETECTOR
# =====================================================

# Moving average window
BLINK_WINDOW = 5

# Minimum slope to start blink
BLINK_RISE_THRESHOLD = 60

# Minimum negative slope
BLINK_FALL_THRESHOLD = 60

# Blink duration (250 Hz)

BLINK_MIN_WIDTH = 12      # 48 ms

BLINK_MAX_WIDTH = 60      # 240 ms

# Ignore new blink for

BLINK_REFRACTORY = 0.30

# Wait before deciding
# Double / Triple Blink

BLINK_GROUP_TIMEOUT = 0.70

# Minimum threshold allowed

MIN_BLINK_THRESHOLD = 400

# Calibration multiplier

BLINK_THRESHOLD_SCALE = 1.10

# =====================================================
# POSITION CONTROLLER
# =====================================================

STEP_SIZE = 2

MIN_X = 0
MAX_X = 100

MIN_Y = 0
MAX_Y = 100

MIN_Z = 0
MAX_Z = 100

# =====================================================
# GUI
# =====================================================

GUI_REFRESH = 20