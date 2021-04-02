class Session:

    def __init__(self, name, type, date, start_time, end_time, id = None):
        self.name = name
        self.type = type
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.id = id

        # Extensions:
        # self.room = room