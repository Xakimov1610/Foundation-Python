import sys
import os

class Team:
    def __init__(self):
        self.sides = ["up", "right", "down", "left"]
        self.current_side = None

    def main_part(self):
        self.clear_everything()
        self.print_sides()
        while self.current_side not in self.sides:
            self.clear_everything()
            self.print_sides()

        self.print_text()
        input_tag = input("Enter[side] [step]: ").strip().lower().split(" ")

        while True:
            if input_tag[0] == "right" or input_tag[0] == "left":
                self.to_right_or_left(input_tag)
            elif input_tag[0] == "up" or input_tag[0] == "down":
                self.to_up_or_to_down(int(float(input_tag[1])))

            if input_tag[0] == "q" or input_tag[0] == "quit" and len(input_tag) != 1:
                self.clear_everything()
                print(self.current_side)
                sys.exit()
            self.print_text()
            input_tag = input("Enter[side] [step]: ").strip().lower().split(" ")

    def to_right_or_left(self, input_tag):
        step = int(float(input_tag[1]))
        if input_tag[0] == "right":
            self.current_side = self.sides[(self.sides.index(self.current_side) + step) % 4]
        else:
            self.current_side = self.sides[self.sides.index(self.current_side) - (step % 4)]

    def to_up_or_to_down(self, step):
        step = int(float(step))
        if step % 2 == 1:
            self.to_right_or_left(["right", 2 * step])

    def print_text(self):
        self.clear_everything()
        print("""                                                                                     
        Enter sides and numbers.
        Like this!
        Right 5
        Down 3                                                                                        
    
        ############################
        ######### Quit [q] #########
        ############################
        """)

    def print_sides(self):
        self.current_side = input("""
    UP
    RIGHT
    DOWN
    LEFT
        
    Please, first enter your current side: """).strip()

    @staticmethod
    def clear_everything():
        os.system("clear")


user = Team()
user.main_part()
