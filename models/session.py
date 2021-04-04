class Session:

    def __init__(self, name, type, date, start_time, end_time, capacity, id = None):
        self.name = name
        self.type = type
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.capacity = capacity
        self.id = id