import pygame
import random

# Array class stores an array full of numbers, that will be sorted.
class Array:

    # Initialises with a given amount of numbers.
    def __init__(self, size):
        self.size = size
        self.numbers = []
        for number in range(size):
            self.numbers.append(number + 1)

    # randomize method randomizes the array.
    def randomize(self):
        random.shuffle(self.numbers)

    # get_numbers returns the array.
    def get_numbers(self):
        return self.numbers

    # get_length method returns the length of the array.
    def get_length(self):
        return len(self.numbers)

# SortArray class sorts the given array full of numbers, using the selected type of sort.
class SortArray:

    #Initialised with the array and interface.
    def __init__(self, array, interface):
        self.array = array
        self.interface = interface

    # bubble_sort method uses bubble sort to sort the array.
    def bubble_sort(self):

        for i in range(self.array.get_length() - 1):

            for j in range(self.array.get_length() -1 - i):

                if self.array.numbers[j] > self.array.numbers[j + 1]:
                    self.array.numbers[j], self.array.numbers[j + 1] = self.array.numbers[j + 1], self.array.numbers[j]
                    self.interface.draw_array(self.array.numbers[j], self.array.numbers[j + 1])
                    pygame.time.wait(500)

    # I am going to add more sorting algorithms below.


# Interface class draws everything onto the screen and also has a method that drives the program.
class Interface:

    # Initialises the window and array going to be used.
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.running = True
        self.array = Array(50)
        self.array.randomize()
        self.sorting = SortArray(self.array, self)
        self.starting_position = 100
        self.gap = 5

    # write_text method writes text to the screen at a given location.
    def write_text(self, text, text_colour, x, y):
        text_font = pygame.font.SysFont("Arial", 12)
        writing = text_font.render(text, True, text_colour)
        self.screen.blit(writing, (x, y))

    # draw_array method draws the array onto the screen.
    def draw_array(self, num1, num2):
        self.screen.fill("cadetblue")

        # Loops through every number in the array.
        for number in self.array.get_numbers():

            # If number is the current number selected in the sorting it is represented as orange.
            if (number == num1) | (number == num2):
                pygame.draw.line(self.screen, "orange", (self.starting_position + self.gap, 700), (self.starting_position + self.gap, 700 - (number + 1) * 10), 5)

            # If number is not the current number selected in the sorting it is represented as green.
            else:
                pygame.draw.line(self.screen, "green", (self.starting_position + self.gap, 700), (self.starting_position + self.gap, 700 - (number + 1) * 10), 5)

            # Writes the value of the number underneath the bar.
            self.write_text(str(number), "black", (self.starting_position + self.gap - 5, 700), (self.starting_position + self.gap - 5, 700 - (number + 1) * 10))
            self.gap += 20

        # Updates display
        pygame.display.flip()

        self.gap = 5

    # Runs the programs
    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

            self.sorting.bubble_sort()
            pygame.quit()

# Initiates interface and uses the run method.
interface = Interface()
interface.run()

