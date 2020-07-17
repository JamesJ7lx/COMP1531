class Member:
    def __init__(self):
        self.host_stays = []
        self.guest_stays = []

    def add_host_stay(self, guest, nights):
        self.host_stays.append(Stay(self, guest, nights))

    def add_guest_stay(self, guest, nights):
        self.guest_stays.append(Stay(guest, self, nights))

    def get_average_rating(self):
        total = 0
        for s in self.host_stays:
            total += s.review_of_host.rating

        for s in self.guest_stays:
            total += s.review_of_guest.rating

        return total/(len(self.host_stays) + len(self.guest_stays))

class Stay:
    def __init__(self, host, guest, nights):
        self.host = host
        self.guest = guest
        self.review_of_guest = None
        self.review_of_host = None
        self.nights = nights

    def review_as_guest(self, description, rating):
        self.review_of_host = Review(self.guest, self.host, description, rating)

    def review_as_host(self, description, rating):
        self.review_of_guest = Review(self.host, self.guest, description, rating)

class Review:
    def __init__(self, reviewer, reviewee, description, rating):
        self.reviewer = reviewer
        self.reviewee = reviewee
        self.description = description
        self.rating = rating

    def exceptional(self):
        return self.rating >= self.reviewer.get_average_rating()

    def dubious(self):
        return self.rating - self.reviewee.get_average_rating() > 2