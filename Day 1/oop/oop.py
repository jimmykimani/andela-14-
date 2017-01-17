class phone(object):

    def __init__(self):
        self.operating_system = 'Unknown'
        self.cost = 0

    def operating_system(self):

        return self.operating_system

    def get_cost(self):

        return self.cost


class samsung(phone):

    def __init__(self):
        super(samsung, self).__init__()
        self.operating_system = 'Android phone'
        self.cost = 45000

    def operating_system(self):

        return super(samsung, self).operating_system()

    def get_cost(self):
        return super(samsung, self).get_cost()


class iphone(phone):
    def __init__(self):
        super(iphone, self).__init__()
        self.operating_system = 'apple ios'
        self.cost = 50000

    def operating_system(self):
        return super(iphone, self).operating_system()

    def get_cost(self):

        return super(iphone, self).get_cost()

class earphones(phone_accessories):

    def get_cost(self):

        return self.phone.get_cost() + 50

    def get_description(self):

        return self.phone_accessories() + ' which' + ' color'
