# Author: Fransiskus Agapa

from abc import ABC, abstractmethod


class Vehicle:

    @abstractmethod                          # this class can no longer be instantiated
    def create(self):
        print("Create new vehicle")

    @abstractmethod
    def use(self):
        print("Use the new vehicle")

    @abstractmethod
    def stop(self):
        print("Stop the vehicle")


class AirPlane(Vehicle):

    def create(self):                       # method must be overwritten
        print("An airplane is built")

    def use(self):
        print("Airplane is flying")

    def stop(self):
        print("Air plane is stopped")


class Ship(Vehicle):

    def create(self):
        print("A ship is built")

    def use(self):
        print("Ship is shipping")

    def stop(self):
        print("Ship is stopped")


print("\n== Basic Usage of Vehicle ==")
print("1. Air Plane")
print("2. Ship")
print("e. Exit")
choice = input("choice: ").lower()           # make user input to lower case to make while-loop condition easier

while choice != 'e':
    if choice == '1':
        print("\n[ Air Place ]\n")
        airplane = AirPlane()
        airplane.create()
        airplane.use()
        airplane.stop()

    elif choice == '2':
        print("\n[ Ship ]\n")
        ship = Ship()
        ship.create()
        ship.use()
        ship.stop()

    else:
        print("\n[ Invalid choice ]")

    print("\n== Basic Usage of Vehicle ==")
    print("1. Air Plane")
    print("2. Ship")
    print("e. Exit")
    choice = input("choice: ").lower()       # make user input to lower case to make while-loop condition easier

print("\n== Exit Program ==")
