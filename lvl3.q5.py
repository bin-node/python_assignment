class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def add_time(self, hours, minutes):
        self.hours = self.hours + hours
        self.minutes = self.minutes + minutes
        
        if self.minutes / 60:
            self.hours +=1
            self.minutes = self.minutes % 60
    def display_time(self):
        print(f'{self.hours} hours and {self.minutes} minutes')
    def display_minutes(self):
        print(f'{self.hours *60 + self.minutes} minutes')

a = Time(2,50)
a.add_time(1,20)
a.display_time()
a.display_minutes()