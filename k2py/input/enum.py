from enum import Enum

class HandType(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2

class KinectEngagementMode(Enum):
    NONE = 0
    SYSTEM_ONE_PERSON = 1
    SYSTEM_TWO_PERSON = 2
    MANUAL_ONE_PERSON = 3
    MANUAL_TWO_PERSON = 4

class KinectGestureSettings(Enum):
    NONE = 0
    TAP = 1
    MANIPULATION_TRANSLATE_X = 64
    MANIPULATION_TRANSLATE_Y = 128
    MANIPULATION_TRANSLATE_RAILS_X = 256
    MANIPULATION_TRANSLATE_RAILS_Y = 512
    MANIPULATION_SCALE = 2048
    MANIPULATION_TRANSLATE_INERTIA = 4096
    KINECT_HOLD = 65536

class KinectHoldingState(Enum):
    STARTED = 0
    COMPLETED = 1
    CANCELED = 2

class KinectInteractionMode(Enum):
    NORMAL = 0
    OFF = 1
    MEDIA = 2

class PointerDeviceType(Enum):
    TOUCH = 0
    PEN = 1
    MOUSE = 2
    KINECT = 3