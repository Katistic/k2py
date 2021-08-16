from Microsoft.Kinect import KinectSensor as _ks
from k2py.audiosource import AudioSource
from k2py.enum import KinectCapabilities

class KinectSensor:
    """Represents a KinectSensor device."""

    @staticmethod
    def get_default():
        return KinectSensor(_ks.GetDefault())

    def __init__(self, sensor: _ks):
        self._ks = sensor

        ## Generate attrs

        for attr in dir(sensor):
            if not attr.startswith("__") and not attr.startswith("get_"):
                if not attr.startswith("remove_") and not attr.startswith("add_"):
                    attr_name = ""

                    first = True
                    for c in attr:
                        if first:
                            attr_name += c.lower()
                            first = False
                            continue

                        if c.isupper() and c != c.lower():
                            attr_name += "_" + c.lower()
                            continue

                        attr_name += c
                    if not hasattr(self, attr_name):
                        setattr(self, attr_name, getattr(sensor, attr))
                        print(f"Generated alias for {attr}: KinectSensor.{attr_name}")

    def open(self):
        self._ks.Open()

    def close(self):
        self._ks.Close()

    @property
    def audio_source(self):
        return AudioSource(self, self._ks.AudioSource)

    @property
    def is_available(self) -> bool:
        return self._ks.IsAvailable

    @property
    def is_open(self) -> bool:
        return self._ks.IsOpen

    @property
    def kinect_capabilities(self) -> KinectCapabilities:
        try:
            return KinectCapabilities(self._ks.KinectCapabilities)
        except ValueError:
            return None

    @property
    def unique_kinect_id(self) -> str:
        return self._ks.UniqueKinectId

    # TODO

