
class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def info(self):
        print('{} can go {} mph.'.format(self.name, self.speed))

class MotorVehicle(TransportMode):
    def __init__(self, name, speed, mpg):
        TransportMode.__init__(self, name, speed)
        self.mpg = mpg
        self.fuel_gal = 0 

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def drive(self, distance):
        required_fuel = distance / self.mpg
        if self.fuel_gal < required_fuel:
            print('Not enough gas.')
        else:
            self.fuel_gal -= required_fuel
            print('{:f} gallons remaining.'.format(self.fuel_gal))

class MotorCycle(MotorVehicle):
    def __init__(self, name, speed, mpg):
        MotorVehicle.__init__(self, name, speed, mpg)

    def wheelie(self):
        print('That is too dangerous.')


scooter = MotorCycle('Vespa', 55, 40)
dirtbike = MotorCycle('KX450F', 80, 25)

scooter.info()
dirtbike.info()
choice = input('Select scooter (s) or dirtbike (d): ')
bike = scooter if (choice == 's') else dirtbike

menu = '\nSelect add fuel(f), go(g), wheelie(w), quit(q): '
command = input(menu)
while command != 'q':
    if command == 'f':
        fuel = int(input('Enter amount: '))
        bike.add_fuel(fuel)
    elif command == 'g':
        distance = int(input('Enter distance: '))
        bike.drive(distance)
    elif command == 'w':
        bike.wheelie()
    elif command == 'q':
        break
    else:
        print('Invalid command.')

    command = input(menu)

