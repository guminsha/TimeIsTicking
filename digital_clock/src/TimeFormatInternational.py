from TimeFormat import TimeFormat


class TimeFormatInternational(TimeFormat):
    def __init__(self):
        super().__init__("%I:%M:%S %p", "%B %d %Y, %A", 'en_US', "12AM/PM")
