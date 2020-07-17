class Advertisement:
    def __init__(self, seller, price, description, categories):
        self.seller = seller
        self.price = price
        self.description = description
        self.enquiries = []
        self.categories = categories
        for c in categories:
            c.add_advertisement(self)

    def place_enquiry(self, question):
        self.enquiries.append(Enquiry(question))

class Enquiry:
    def __init__(self, question):
        self.question = question
        self.response = None

    def respond(self, seller, answer):
        if (self.response is None):
            raise Exception
        else:
            self.response = Response(answer)

class Response:
    def __init__(self, answer):
        self.answer = answer
        self.accepted = False

    def accept(self):
        self.accepted = True

class Category:
    def __init__(self, description):
        self.description = description
        self.advertisements = []

class Buyer:
    def __init__(self):
        self.subscriptions = []

    def subscribe(self, category):
        self.subscriptions.append(category)

class Seller:
    def __init__(self):
        pass

    def advertise(self, price, description, categories):
        return Advertisement(self, price, description, categories)