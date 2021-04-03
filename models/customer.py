class Customer:

    def __init__(self, forename, surname, alias, membership_status, membership_type, id = None):
        self.forename = forename
        self.surname = surname
        self.alias = alias
        self.membership_status = membership_status
        self.membership_type = membership_type
        self.id = id

        # Extension:
        # self.monthly_sessions_had = monthly_sessions_had

    # def full_name(self, forename, surname):
    #     return '{forename} {surname}'