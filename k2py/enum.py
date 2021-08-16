from enum import Enum

class Activity(Enum):
    EYE_LEFT_CLOSED = 0
    EYE_RIGHT_CLOSED = 1
    LOOKING_AWAY = 2
    MOUTH_MOVED = 3
    MOUTH_OPEN = 4

class Appearance(Enum):
    WEARING_GLASSES = 0

class AudioBeamMode(Enum):
    AUTOMATIC = 0
    MANUAL = 1

class ColorImageFormat(Enum):
    NONE = 0
    RGBA = 1
    YUV = 2
    BGRA = 3
    BAYER = 4
    YUV2 = 5

ColourImageFormat = ColorImageFormat

class DetectionResult(Enum):
    UNKNOWN = 0
    NO = 1
    MAYBE = 2
    YES = 3

class Expression(Enum):
    NEUTRAL = 0
    HAPPY = 1

class FrameCapturedStatus(Enum):
    UNKNOWN = 0
    QUEUED = 1
    DROPPED = 2

class FrameEdges(Enum):
    NONE = 0
    RIGHT = 1
    LEFT = 2
    TOP = 4
    BOTTOM = 8

class FrameSourceTypes(Enum):
    NONE = 0
    COLOR = 1
    COLOUR = 1
    INFRARED = 2
    LONG_EXPOSURE_INFRARED = 4
    DEPTH = 8
    BODY_INDEX = 16
    BODY = 32
    AUDIO = 64

class HandState(Enum):
    UNKNOWN = 0
    NOT_TRACKED = 1
    OPEN = 2
    CLOSED = 3
    LASSO = 4

class JointType(Enum):
    ANKLE_LEFT = 14
    ANKLE_RIGHT = 18
    ELBOW_LEFT = 5
    ELBOW_RIGHT = 9
    FOOT_LEFT = 15
    FOOT_RIGHT = 19
    HAND_LEFT = 7
    HAND_RIGHT = 11
    HAND_TIP_LEFT = 21
    HAND_TIP_RIGHT = 23
    HEAD = 3
    HIP_LEFT = 12
    HIP_RIGHT = 16
    KNEE_LEFT = 13
    KNEE_RIGHT = 17
    NECK = 2
    SHOULDER_LEFT = 4
    SHOULDER_RIGHT = 8
    SPINE_BASE = 0
    SPINE_MID = 1
    SPINE_SHOULDER = 20
    THUMB_LEFT = 22
    THUMB_RIGHT = 24
    WRIST_LEFT = 6
    WRIST_RIGHT = 10

class KinectAudioCalibrationState(Enum):
    UNKNOWN = 0
    CALIBRATION_REQUIRED = 1
    CALIBRATED = 2

class KinectCapabilities(Enum):
    NONE = 0
    VISION = 1
    AUDIO = 2
    FACE = 4
    EXPRESSIONS = 8
    GAMECHAT = 16

class TrackingConfidence(Enum):
    LOW = 0
    HIGH = 1

class TrackingState(Enum):
    NOT_TRACKED = 0
    INFERRED = 1
    TRACKED = 2