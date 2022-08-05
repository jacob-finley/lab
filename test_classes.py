import pytest
from classes import *


class Test:
    def setup_method(self) -> None:
        self.TV = Television()

    def teardown_method(self):
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