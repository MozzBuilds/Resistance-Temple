class Customer:

    def __init__(self, forename, surname, alias, membership_status, membership_type, id = None):
        self.forename = forename
        self.surname = surname
        self.alias = alias
        self.membership_status = membership_status
        self.membership_type = membership_type
        self.id = id
        self.membership_status_types = ['Active', 'Inactive']
        self.membership_types = ['None', 'Silver', 'Gold', 'Platinum']


    # def full_name(self, forename, surname):
    #     return '{forename} {surname}'

