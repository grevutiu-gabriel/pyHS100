import enum

class SmartDeviceException(Exception):
    """
    SmartPlugException gets raised for errors reported by the plug.
    """
    pass


class SocketException(SmartDeviceException):
    """
    SocketException gets raised when there is a connectivity problem with a
     device.
    """


class NotSupportedException(SmartDeviceException):
    """
    NotSupportedException gets raised when there is a feature that is not
     supported by a device.
    """


class DeviceType(enum.Enum):
    Unknown = -1,
    Plug = 0,
    Switch = 1
    Bulb = 2
