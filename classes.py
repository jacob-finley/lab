class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel
    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Sets the values of __Channel, __Volume, and __On for a TV as defaults

        :param self.__Channel: private variable to set a specific channel, set to 0 as default
        :param self.__Volume: private variable to set the volume, set to 0 as default
        :param self.__On: private variable to determine if the tv is on or off
        :return: None
        """
        self.__Channel = 0
        self.__Volume = 0
        self.__On = False

    def get_Channel(self) -> int:
        """
        :return: tv channel
        """
        return self.__Channel

    def set_Channel(self, channel) -> None:
        """
        will set the channel to any custom int value within the given channel range

        :param channel: custom channel number
        :return: None
        """
        if type(channel) != int:
            raise TypeError('Invalid data type')
        elif channel < self.MIN_CHANNEL or channel > self.MAX_CHANNEL:
            raise ValueError('Out of index')
        else:
            if self.__On:
                self.__Channel = channel

    def get_Volume(self) -> int:
        """
        :return: tv volume
        """
        return self.__Volume

    def set_Volume(self, volume) -> None:
        """
        will set the volume to something custom, within the given volume range
        :param volume: custom volume
        :return: None
        """
        if type(volume) != int:
            raise TypeError('Invalid data type')
        elif volume < self.MIN_VOLUME or volume > self.MAX_VOLUME:
            raise ValueError('Out of index')
        else:
            if self.__On:
                self.__Volume = volume

    def get_On(self) -> bool:
        """
        :return: the status of the tv (on or off)
        """
        return self.__On

    def power(self) -> None:
        """
        method that turns the tv on or off, when called it will turn
        the TV on if it is off or off when it is on

        :return: None
        """
        if self.__On:
            self.__On = False
        else:
            self.__On = True

    def channel_up(self) -> None:
        """
        method that will increment the channel by one or set to the minimum channel if the channel
        is already at the maximum

        :return: None
        """
        if self.__On:
            if self.__Channel < Television.MAX_CHANNEL:
                self.__Channel += 1
            else:
                self.__Channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        method that will decrement the channel by one or set to the maximum channel if the channel
        is already at the minimum

        :return: None
        """
        if self.__On:
            if self.__Channel > Television.MIN_CHANNEL:
                self.__Channel -= 1
            else:
                self.__Channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        method that will increment the volume of the tv until it hits its maximum volume

        :return: None
        """
        if self.__On:
            if self.__Volume < Television.MAX_VOLUME:
                self.__Volume += 1

    def volume_down(self) -> None:
        """
        method that will decrement the volume of the tv until it hits its minimum volume

        :return: None
        """
        if self.__On:
            if self.__Volume > Television.MIN_VOLUME:
                self.__Volume -= 1

    def __str__(self) -> str:
        """
        print statement that tells the user if the tv is on, what channel it is on,
        and what the current volume is

        :return: str
        """
        return f'TV status: Is on = {self.__On}, Channel = {self.__Channel}, Volume = {self.__Volume}'


if __name__ == '__main__':
    TV1 = Television()
    print(TV1.volume_down())

##################################################
import pytest
from classes import *


class Test:
    def setUp(self) -> None:
        self.TV = Television()

    def tearDown(self):
        del self.TV

    def test_init(self):
        assert self.TV.get_Channel() == 0
        assert self.TV.get_Volume() == 0
        assert self.TV.get_On() is False

    def test_set_Channel(self):
        assert self.TV.get_Channel() == 0           # checks the channel (0)
        self.TV.set_Channel(1)                      # sets the channel, will fail since the tv is off by defualt
        assert self.TV.get_Channel() == 0           # checks the channel (0)
        self.TV.power()                             # turns the tv on
        self.TV.set_Channel(1)                      # sets the channel (1)
        assert self.TV.get_Channel() == 1           # checks the channel (1)
        self.TV.set_Channel(3)                      # sets the chanel (3)
        assert self.TV.get_Channel() == 3           # checks the channel (3)
        self.TV.power()                             # turns the tv off
        self.TV.set_Channel(2)                      # sets the channel, will fail since the tv is off
        assert self.TV.get_Channel() == 3           # checks the channel, will still be 3
        with pytest.raises(TypeError):
            self.TV.set_Channel(1.5)
            self.TV.set_Channel('2')
        with pytest.raises(ValueError):
            self.TV.set_Channel(-3)
            self.TV.set_Channel(9)

    def test_set_Volume(self):
        assert self.TV.get_Volume() == 0        # checks the volume (0)
        self.TV.set_Volume(2)                   # sets the volume, will fail since tv is powered off by default
        assert self.TV.get_Volume() == 0        # checks the volume (0)
        self.TV.power()                         # powers tv on
        self.TV.set_Volume(2)                   # sets the volume (2)
        assert self.TV.get_Volume() == 2        # checks the volume
        self.TV.power()                         # powers the tv off
        self.TV.set_Volume(1)                   # sets the volume to 1 but will fail since the tv is off
        assert self.TV.get_Volume() == 2        # checks the volume is still 2
        with pytest.raises(TypeError):
            self.TV.set_Volume(1.4)
            self.TV.set_Volume('1')
        with pytest.raises(ValueError):
            self.TV.set_Volume(-1)
            self.TV.set_Volume(99)

    def test_power(self):
        assert self.TV.get_On() is False        # determine if the tv starts powered off
        self.TV.power()                         # turn the tv from off to on
        assert self.TV.get_On() is True         # determine if the tv is powered on
        self.TV.power()                         # turn the tv from on to off
        assert self.TV.get_On() is False        # determine if the tv is powered off

    def test_channel_up(self):
        self.TV.channel_up()                    # will turn the channel up, but tv is turned off so the channel will not change
        assert self.TV.get_Channel() == 0
        self.TV.power()                         # will turn the tv on
        self.TV.channel_up()                    # will turn the channel up, should be 1
        assert self.TV.get_Channel() == 1
        self.TV.channel_up()                    # will turn the channel up, should be 2
        assert self.TV.get_Channel() == 2
        self.TV.power()                         # will turn the tv off
        self.TV.channel_up()                    # will attempt to turn the channel up, but will remain 2 until the tv is turned back on
        assert self.TV.get_Channel() == 2
        self.TV.power()                         # will turn the tv on
        self.TV.channel_up()                    # will turn the channel up, should be 3
        assert self.TV.get_Channel() == 3
        self.TV.channel_up()                    # will turn the channel up, should go back down to 0 since 3 is the max channel
        assert self.TV.get_Channel() == 0

    def test_channel_down(self):
        self.TV.channel_down()                  # will turn the channel down, but the tv is turned off so the channel will not change
        assert self.TV.get_Channel() == 0
        self.TV.power()                         # will turn the tv back on
        self.TV.channel_down()                  # will turn the channel down, should be 3
        assert self.TV.get_Channel() == 3
        self.TV.power()                         # will turn the tv off
        self.TV.channel_down()                  # will attempt to turn the channel down, but will fail since the tv is off
        assert self.TV.get_Channel() == 3
        self.TV.power()                         # will turn the tv on
        self.TV.channel_down()                  # will turn the channel down, should be 2
        assert self.TV.get_Channel() == 2
        self.TV.channel_down()                  # will turn the channel down, should be 1
        assert self.TV.get_Channel() == 1
        self.TV.channel_down()                  # will turn the channel down, should be 0
        assert self.TV.get_Channel() == 0

    def test_volume_up(self):
        self.TV.volume_up()                     # will attempt to turn the volume up, but will fail since the tv is off
        assert self.TV.get_Volume() == 0
        self.TV.power()                         # will turn the tv on
        self.TV.volume_up()                     # will turn the volume up, should be 1
        assert self.TV.get_Volume() == 1
        self.TV.power()                         # will turn the tv off
        self.TV.volume_up()                     # will attempt to turn the volume up, but will fail since the tv is off
        assert self.TV.get_Volume() == 1
        self.TV.power()                         # will turn the tv on
        self.TV.volume_up()                     # will turn the volume up, should be 2
        assert self.TV.get_Volume() == 2
        self.TV.volume_up()                     # will attempt to turn the volume up, but the volume is at max of 2 so the volume will not change
        assert self.TV.get_Volume() == 2

    def test_volume_down(self):
        self.TV.volume_down()                   # will attempt to turn the volume down, but the volume is at the minimum, and the tv is off so the volume will not change
        assert self.TV.get_Volume() == 0
        self.TV.power()                         # will turn the tv on
        self.TV.volume_down()                   # will attempt to turn the volume down, but the volume is at the minimum, so the volume will not change
        assert self.TV.get_Volume() == 0
        self.TV.volume_up()                     # will turn up the volume, should be 1
        self.TV.volume_up()                     # will turn up the volume, should be 2
        assert self.TV.get_Volume() == 2
        self.TV.volume_down()                   # will turn down the volume, should be 1
        self.TV.volume_down()                   # will turn down the volume, should be 0
        assert self.TV.get_Volume() == 0

    def test__str__(self):
        assert self.TV.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        # test tv on normal status
        self.TV.power()                         # turns tv on
        self.TV.set_Channel(1)                  # sets channel to 1
        self.TV.set_Volume(1)                   # sets volume to 1
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 1'
        # test tv on set settings
        self.TV.power()