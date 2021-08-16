from Microsoft.Kinect import AudioBeam as _ab
from System.IO import Stream
from k2py.enum import AudioBeamMode

class AudioBeam:
    def __init__(self, source, beam: _ab):
        self._ab = beam
        self.audio_source = source

    @property
    def audio_beam_mode(self) -> AudioBeamMode:
        return AudioBeamMode(self._ab.AudioBeamMode)

    @property
    def beam_angle(self) -> float:
        return self._ab.BeamAngle

    @property
    def beam_angle_confidence(self) -> float:
        return self._ab.BeamAngleConfidence

    @property
    def relative_time(self):
        return self._ab.RelativeTime

    def add_property_changed_listener(self, listener):
        self._ab.PropertyChanged += listener

    def remove_property_changed_listener(self, listener):
        self._ab.PropertyChanged -= listener

    def open_input_stream(self) -> Stream:
        return self._ab.OpenInputStream()