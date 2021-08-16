from Microsoft.Kinect import AudioSource as _as
from k2py.audiobeam import AudioBeam
from k2py.enum import KinectAudioCalibrationState
from System import TimeSpan

class AudioSource:
    def __init__(self, sensor, source: _as):
        self._as = source
        self.kinect_sensor = sensor
        
    @property
    def audio_beams(self):
        beam_list = []

        for beam in audio_beams:
            beam_list.append(AudioBeam(beam))

        return beam_list

    @property
    def audio_calibration_state(self) -> KinectAudioCalibrationState:
        return KinectAudioCalibrationState(self._as.AudioCalibrationState)

    @property
    def is_active(self) -> bool:
        return self._as.IsActive

    @property
    def max_sub_frame_count(self):
        return self._as.MaxSubFrameCount

    @property
    def sub_frame_duration(self) -> TimeSpan:
        return self._as.SubFrameDuration

    @property
    def sub_frame_length(self):
        return self._as.SubFrameLength

    def add_frame_captured_listener(self, listener):
        self._as.FrameCaptured += listener

    def remove_frame_captured_listener(self, listener):
        self._as.FrameCaptured -= listener

    def add_property_changed_listener(self, listener):
        self._as.PropertyChanged += listener

    def remove_property_changed_listener(self, listener):
        self._as.PropertyChanged -= listener