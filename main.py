class Destination:
    def __init__(self):
        self.destinations = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, dist):
        return self.destinations.get(dist, 0)
    
    def is_valid_destination(self, dist):
        return isinstance(dist, str)

class passenger:
    def __init__(self, num):
        self.num = num
    
    def is_valid_number(self):
        print("Is a valid number :)")
        return isinstance(self.num, int) and self.num > 0

    def calculate_discount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num <= 10:
            return 0.2
        else:
            return 0.0

class TotalTime:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_time(self):
        return isinstance(self.dur, int) and self.dur > 0

    def get_fee(self):
        return 200 if self.dur < 7 else 0

    def get_the_best_promo_ever(self):
        return 200 if self.dur > 30 else 0
    
    def get_weekend(self):
        return 100 if self.dur > 7 else 0

class Vacation:
    base_cost = 1000

    def __init__(self, dist, num, dur):
        self.destination = Destination()
        self.passenger = passenger(num)
        self.total_time = TotalTime(dur)
        self.dist = dist

    def sum(self):
        #sum the cost of the vacation package here
        if not self.destination.is_valid_destination(self.dist) or not self.passenger.is_valid_number() or not self.total_time.is_valid_total_time():
            return -1
        
        #sum the total cost
        number_total = self.base_cost
        number_total += self.destination.get_extra_cost(self.dist)
        number_total += self.total_time.get_fee()
        number_total -= self.total_time.get_the_best_promo_ever()

        discount = self.passenger.calculate_discount()
        number_total = number_total - (number_total * discount)
        
        return max(int(number_total), 0)

#this is main function
def main():
    #this are the inputs
    dist = "Paris"
    num = 5
    dur = 10

    #this are the outputs
    calculator = Vacation(dist, num, dur)
    cost = calculator.sum()

    #this will do some printing
    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")

#main event function
if __name__ == "__main__":
    main()
