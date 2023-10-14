from TimeFormat import TimeFormat


class TimeFormatBrazil(TimeFormat):
    def __init__(self):
        super().__init__("%H:%M:%S", "%d de %B %Y, %A", 'pt_BR', "24HRS")
