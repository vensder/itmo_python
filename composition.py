class Wheel:
    def __init__(self):
        self.status = 'stopped'
        print(self.__class__.__name__, self.status)

    def spin(self):
        self.status = 'spinning'
        print(self.__class__.__name__,self.status)


class Engine:
    def __init__(self):
        self.status = 'stopped'
        print(self.__class__.__name__,self.status)

    def turn_on(self):
        self.status = 'running'
        print(self.__class__.__name__,self.status)


class Car:
    def __init__(self):
        # composition
        self.engine = Engine()
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]

    # delegating
    def drive(self):
        self.engine.turn_on()
        for wheel in self.wheels:
            wheel.spin()


if __name__ == '__main__':
    car = Car()
    car.drive()
