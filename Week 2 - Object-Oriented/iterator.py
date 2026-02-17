class Countdown:
    # A Class that implements an iterator for a countdown.
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        # Initialize the iterator and return the object itself.
        return self
    
    def __next__(self):
        # Define what happens on each iteration.
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1
        
countdown = Countdown(5)

print("Countdown:")
for number in countdown:
    print(number)