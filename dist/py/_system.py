# Autogenerated file for Common registers and commands
# Add missing from ... import const
_JD_ANNOUNCE_INTERVAL = const(0x1f4)

_JD_READING_THRESHOLD_NEUTRAL = const(0x1)
_JD_READING_THRESHOLD_INACTIVE = const(0x2)
_JD_READING_THRESHOLD_ACTIVE = const(0x3)
_JD_STATUS_CODES_READY = const(0x0)
_JD_STATUS_CODES_INITIALIZING = const(0x1)
_JD_STATUS_CODES_CALIBRATING = const(0x2)
_JD_STATUS_CODES_SLEEPING = const(0x3)
_JD_STATUS_CODES_WAITING_FOR_INPUT = const(0x4)
_JD_STATUS_CODES_CALIBRATION_NEEDED = const(0x64)
_JD_CMD_ANNOUNCE = const(0x0)
_JD_CMD_GET_REGISTER = const(0x1000)
_JD_CMD_SET_REGISTER = const(0x2000)
_JD_CMD_EVENT = const(0x1)
_JD_CMD_CALIBRATE = const(0x2)
_JD_REG_INTENSITY = const(0x1)
_JD_REG_VALUE = const(0x2)
_JD_REG_MIN_VALUE = const(0x110)
_JD_REG_MAX_VALUE = const(0x111)
_JD_REG_MAX_POWER = const(0x7)
_JD_REG_STREAMING_SAMPLES = const(0x3)
_JD_REG_STREAMING_INTERVAL = const(0x4)
_JD_REG_READING = const(0x101)
_JD_REG_READING_RANGE = const(0x8)
_JD_REG_SUPPORTED_RANGES = const(0x10a)
_JD_REG_MIN_READING = const(0x104)
_JD_REG_MAX_READING = const(0x105)
_JD_REG_READING_ERROR = const(0x106)
_JD_REG_READING_RESOLUTION = const(0x108)
_JD_REG_INACTIVE_THRESHOLD = const(0x5)
_JD_REG_ACTIVE_THRESHOLD = const(0x6)
_JD_REG_STREAMING_PREFERRED_INTERVAL = const(0x102)
_JD_REG_VARIANT = const(0x107)
_JD_REG_STATUS_CODE = const(0x103)
_JD_REG_INSTANCE_NAME = const(0x109)
_JD_EV_ACTIVE = const(0x1)
_JD_EV_INACTIVE = const(0x2)
_JD_EV_CHANGE = const(0x3)
_JD_EV_STATUS_CODE_CHANGED = const(0x4)
_JD_EV_NEUTRAL = const(0x7)