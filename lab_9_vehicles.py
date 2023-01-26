class Vehicle:

    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__state = "stopped"

    def move(self):
        print("I am moving!")
        self.__state = "moving"

    def stop(self):
        print("I now stoppped.")
        self.__state = "stopped"

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_state(self):
        return self.__state

    def set_state(self, new_state): # State setter
        self.__state = new_state
    
    def __str__(self):
        return f"{self.get_make()} {self.get_model()} is {self.get_state()}."





class Car(Vehicle):

    def __init__(selfself, make, model, doors):
        Vehicle.__init__(self, make, model)
        self.__doors_no = doors

    def set_doors_no(self, number):
        self.__doors_no = number

    def get_doors_no(self):
        return self.__doors_no

    def __str__(self):
        return f"{self.get_make()} {self.get_model()} with {self.get_doors_no()} doors is {self.get_state()}"





class Bus(Vehicle):

    def __init__(self, make, model, decks):
        Vehicle.__init__(self, make, model)
        self.__decks_no = decks
        self.__route_list = ["New Street"] # The bus will be at New Street at the beginning
        self.set_state("Not in use") # Updating the constructor and setting the state of bus
        

    def set_decks_no(self, deck):
        self.__decks_no = deck
    
    def get_decks_no(self):
        return self.__decks_no

    def get_route(self): # Adding a new getter of full route 
        full_route_in_string = ""
        for count, route in enumerate(self.__route_list):
            if count == 0:
                full_route_in_string += route
            else:
                full_route_in_string += f" - {route}"
        return full_route_in_string
    
    def move(self, next_stop): # Overriding move method
        if next_stop in ["BCU", "bcu"]:
            if "BCU" in self.__route_list or "bcu" in self.__route_list:
                print("I am finished for today!")
            else:
                previous_stop = self.__route_list[-1]
                print(f"The bus was at {previous_stop} and is moving to {next_stop}.")
                self.__route_list.append(next_stop) # Adding new stop to the routes list
        else:
            previous_stop = self.__route_list[-1]
            print(f"The bus was at {previous_stop} and is moving to {next_stop}.")
            self.__route_list.append(next_stop) # Adding new stop to the routes list

    def stop(self): # Overriding stop method
        print("I am a non-stop bus.")




def main(): # Function to test the made changes
    bus1 = Bus(2009, "Thomas Built Saf-T-Liner C2", 1)

    print(bus1.get_state()) #printing initial state; should be "Not in use"

    # Moving the bus 3 times
    bus1.move("Bullring")
    bus1.move("Moor Street")
    bus1.move("BCU") # This should print "The bus was at Moor Street and is moving to BCU."

    bus1.move("BCU") # This should print "I am finished for today!" because it is at the final stop

    print(bus1.get_route()) # This should print "New Street - Bullring - Moor Street - BCU."

if __name__ == "__main__":
    main()