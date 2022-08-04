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

    def channel_up(self, MAX_CHANNEL: int, MIN_CHANNEL: int) -> None:
        """
        method that will increment the channel by one or set to the minimum channel if the channel
        is already at the maximum

        :param MAX_CHANNEL: int that sets the upper bounds of possible channels
        :param MIN_CHANNEL: int that sets the lower bounds of possible channels
        :return: None
        """
        if self.__On:
            if self.__Channel < MAX_CHANNEL:
                self.__Channel += 1
            else:
                self.__Channel = MIN_CHANNEL

    def channel_down(self, MAX_CHANNEL: int, MIN_CHANNEL: int) -> None:
        """
        method that will decrement the channel by one or set to the maximum channel if the channel
        is already at the minimum

        :param MAX_CHANNEL: int that sets the upper bounds of possible channels
        :param MIN_CHANNEL: int that sets the lower bounds of possible channels
        :return: None
        """
        if self.__On:
            if self.__Channel > MIN_CHANNEL:
                self.__Channel -= 1
            else:
                self.__Channel = MAX_CHANNEL

    def volume_up(self, MAX_VOLUME: int) -> None:
        """
        method that will increment the volume of the tv until it hits its maximum volume

        :param MAX_VOLUME: int that sets the upper bounds of the volume
        :return: None
        """
        if self.__On:
            if self.__Volume < MAX_VOLUME:
                self.__Volume += 1

    def volume_down(self, MIN_VOLUME: int):
        """
        method that will decrement the volume of the tv until it hits its minimum volume

        :param MIN_VOLUME: int that sets the lower bounds of the volume
        :return: None
        """
        if self.__On:
            if self.__Volume > MIN_VOLUME:
                self.__Volume -= 1

    def __str__(self) -> str:
        """
        print statement that tells the user if the tv is on, what channel it is on,
        and what the current volume is

        :return: str
        """
        return f'TV status: Is on = {self.__On}, Channel = {self.__Channel}, Volume = {self.__Volume}'