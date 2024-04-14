class Statistics:
    def __init__(self, speed):
        self.speed = speed

    def changed_by(self, speed = 0):
        return Statistics(self.speed + speed)

