from Microsoft.Kinect import AudioBeamFrame as _abf

class AudioBeamFrame:
    def __init__(self, source, beam, frame: _abf):
        self._abf = frame
        self.audio_beam = beam
        self.audio_source = source

    @property
    def duration(self):
        return self._abf.Duration

    @property
    def relative_time_start(self):
        return self._abf.RelativeTimeStart

    # TODO
    