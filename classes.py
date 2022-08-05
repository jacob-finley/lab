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
