class Displayer:

    def __init__(self, country_title):
        self.country_title = country_title

    def print(self, days, values):
        print(self.country_title + "\n")
        for k in range(len(days)):
            print("Day " + str(days[k]) + ": " + str(values[k]))
