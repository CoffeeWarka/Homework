class Horse:
    def __init__(self, x_distance, sound):
        super.__init__()
        self.x_distance = x_distance
        self.sound = sound
        sound = 'Frrr'

    def run(self,dx):
        self.x_distance += dx

class Eagle:
    def __init__(self, y_distance, sound):
        self.y_distance = y_distance
        self.sound = sound
        sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    super().__init__()

    def move(self, dx, dy):
        self.run()
        self.fly()

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)
