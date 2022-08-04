class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        self.Channel = 0
        self.Volume = 0
        self.on = False
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """

    def power(self):
        if self.on:
            self.on = False
        else:
            self.on = True
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """

    def channel_up(self):
        if self.on:
            if self.Channel < 3:
                self.Channel += 1
            else:
                self.Channel = 0
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """

    def channel_down(self):
        if self.on:
            if self.Channel > 0:
                self.Channel -= 1
            else:
                self.Channel = 3
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """

    def volume_up(self):
        if self.on:
            if self.Volume < 2:
                self.Volume += 1
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """

    def volume_down(self):
        if self.on:
            if self.Volume > 0:
                self.Volume -= 1
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """

    def __str__(self):
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """
        return f'TV status: Is on = {self.on}, Channel = {self.Channel}, Volume = {self.Volume}'
        # TV status: Is on = False, Channel = 0, Volume = 0
