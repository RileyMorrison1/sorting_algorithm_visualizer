import pygame
import random
import time
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

    # Initialised with the array and interface.
    def __init__(self, array, interface):
        self.array = array
        self.interface = interface
        self.i = 0
        self.j = 0
        self.steps = []
        self.current_step = 0
        self.finished = False

    # sort_next method goes to the next step in the steps array.
    def sort_next(self):
        # Adds one to the current step if it is not at the last value of the steps array.
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1

        # Sets the finished variable to true if the current step is at the last value of the steps array.
        else:
            self.finished = True

        # Sets the values to the next step.
        self.array.numbers = self.steps[self.current_step][0]
        self.i = self.steps[self.current_step][1]
        self.j = self.steps[self.current_step][2]

    # sort_back method makes the array go back to the prior states.
    def sort_back(self):
        if self.current_step >= 1:
            self.current_step -= 1

            # Sets the values to the previous step.
            self.array.numbers = self.steps[self.current_step][0]
            self.i = self.steps[self.current_step][1]
            self.j = self.steps[self.current_step][2]
            self.finished = False

    # finish method skips to the end of the steps array.
    def finish(self):
        self.current_step = len(self.steps) - 1
        self.array.numbers = self.steps[self.current_step][0]
        self.i = self.steps[self.current_step][1]
        self.j = self.steps[self.current_step][2]
        self.finished = True

    # start method skips to the start of the steps array.
    def start(self):
        self.current_step = 0
        self.array.numbers = self.steps[self.current_step][0]
        self.i = self.steps[self.current_step][1]
        self.j = self.steps[self.current_step][2]
        self.finished = False

    # bubble_sort sorts the array with the bubble sort algorith.
    def bubble_sort(self):
        # Every time the method is called the steps array is reset.
        self.steps = []
        for i in range(self.array.get_length() - 1):

            for j in range(self.array.get_length() - 1 - i):

                if self.array.numbers[j] > self.array.numbers[j + 1]:
                    self.array.numbers[j], self.array.numbers[j + 1] = self.array.numbers[j + 1], self.array.numbers[j]

                # Saves every step to the steps array.
                self.steps.append([self.array.numbers.copy(), i, j])

    # I am going to add more sorting algorithms below.


# Interface class draws everything onto the screen and also has a method that drives the program.
class Interface:

    # Initialises the window and array going to be used.
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 750))
        self.running = True
        self.array = Array(50)
        self.array.randomize()
        self.sorting = SortArray(self.array, self)
        self.starting_position = 100
        self.gap = 5
        self.sorting.bubble_sort()
        pygame.display.set_caption("Sorting Algorithm Visualizer")

    # write_text method writes text to the screen at a given location.
    def write_text(self, text, text_colour, x, y):
        text_font = pygame.font.SysFont("Arial", 15)
        writing = text_font.render(text, True, text_colour)
        self.screen.blit(writing, (x, y))

    # draw_array method draws the array onto the screen.
    def draw_array(self):
        self.screen.fill("cadetblue")

        # Assigns the bars which will be highlighted.
        num1, num2 = self.array.numbers[self.sorting.j], self.array.numbers[self.sorting.j + 1]
        colour = "grey25"

        # Loops through every number in the array.
        for number in self.array.get_numbers():

            # Alternates between the colours of the numbers
            if colour == "grey25":
                colour = "black"

            elif colour == "black":
                colour = "grey25"

            # If number is the current number selected in the sorting it is represented as orange.
            if (number == num1) | (number == num2):
                pygame.draw.line(self.screen, "orange", (self.starting_position + self.gap, 650), (self.starting_position + self.gap, 650 - (number + 1) * 10), 10)

            # If number is not the current number selected in the sorting it is represented as green.
            else:
                pygame.draw.line(self.screen, "green", (self.starting_position + self.gap, 650), (self.starting_position + self.gap, 650 - (number + 1) * 10), 10)

            # Writes the value of the number underneath the bar.
            self.write_text(str(number), colour, (self.starting_position + self.gap - 5, 650), (self.starting_position + self.gap - 5, 650 - (number + 1) * 10))
            self.gap += 20

        # Resets to the default starting x position of the bars.
        self.gap = 10

    # Runs the programs
    def run(self):
        pygame.init()
        timer = Timer(.05, 5)
        stop_button = Button(self.screen, "Stop", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black", 500, 685, 100, 50, 5, 1, timer.stop)
        go_button = Button(self.screen, "Start", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black", 600, 685, 100, 50, 5, 1, timer.start)

        fast_speed_button = Button(self.screen, "Fast", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black", 1080, 685,110, 50, 5, 1, timer.increase_speed)
        slow_speed_button = Button(self.screen, "Slow", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black", 860, 685,110, 50, 5, 1, timer.decrease_speed)
        default_speed_button = Button(self.screen, "Default", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black", 970, 685,110, 50, 5, 1, timer.default_speed)

        finish_button = Button(self.screen, "Finish", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black", 340, 685,110, 50, 5, 0.1, self.sorting.finish)
        next_step_button = Button(self.screen, "Next", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black", 230, 685,110, 50, 5, 0.1, self.sorting.sort_next)
        back_step_button = Button(self.screen, "Back", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black",120, 685, 110, 50, 5, .1, self.sorting.sort_back)
        start_button = Button(self.screen, "Start", "lightsteelblue4", "lightsteelblue", "lightsteelblue3", "black",10, 685, 110, 50, 5, .1, self.sorting.start)

        go_button.on_or_off = True

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

            # Stops going to the next step if at the last step.
            if self.sorting.finished:
                timer.on = False

            # Goes to the next step if the desired amount of time has passed.
            if timer.ready():
                self.sorting.sort_next()

            self.draw_array()

            # Creates the menu background.
            pygame.draw.rect(self.screen, "azure3", (0, 675, 1200, 100))

            # Refreshes the buttons. (Might need to make a method to refresh all the buttons at the same time.)
            go_button.refresh()
            stop_button.refresh()
            fast_speed_button.refresh()
            slow_speed_button.refresh()
            back_step_button.refresh()
            next_step_button.refresh()
            start_button.refresh()
            finish_button.refresh()
            default_speed_button.refresh()
            pygame.display.flip()

        pygame.quit()


# Button class creates buttons that can be interacted with. Each button can call a certain function.
# Note that the timer when initialized has already started.
class Button:

    # Initializes a button with all the values it needs.
    def __init__(self, screen, text, border_colour, colour, highlight_colour, text_colour, x, y, width, height, border_width, time_between, function):
        self.screen = screen
        self.text = text
        self.border_colour = border_colour
        self.colour = colour
        self.text_colour = text_colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width
        self.function = function
        self.time_between = time_between
        self.timer = Timer(self.time_between, 0)
        self.highlight_colour = highlight_colour
        self.on_or_off = False

    # refresh method makes sure the button is on the screen and adds functionality to the button if highlighted
    # or clicked on. Needs to be placed in the main loop.
    def refresh(self):
        colour = self.colour

        if self.highlight():
            colour = self.highlight_colour

            if self.click():

                if self.timer.ready():

                    # Alternates between on and off.
                    match self.on_or_off:

                        case True:
                            self.on_or_off = False

                        case False:
                            self.on_or_off = True

                    if self.function != 0:
                        self.function()

        pygame.draw.rect(self.screen, self.border_colour, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.screen, colour, (self.x + (self.border_width / 2), self.y + (self.border_width / 2), self.width - self.border_width, self.height - self.border_width))
        self.write_text(self.text, self.text_colour, self.x + 20, self.y + (self.height/ 7))

    # highlight method returns true if the cursor is over the button.
    def highlight(self):

        if (pygame.mouse.get_pos()[0] > self.x) & (pygame.mouse.get_pos()[0] < (self.x + self.width)):

            if (pygame.mouse.get_pos()[1] > self.y) & (pygame.mouse.get_pos()[1] < (self.y + self.height)):
                return True

        return False

    # click method returns true if the button is clicked and highlighted simultaneously.
    def click(self):

        if self.highlight() & pygame.mouse.get_pressed()[0]:
            return True

        else:
            return False

    # Writes text in the button.
    def write_text(self, text, text_colour, x, y):
        text_font = pygame.font.SysFont("Arial", 30)
        writing = text_font.render(text, True, text_colour)
        self.screen.blit(writing, (x, y))


# Timer class is used to delay the sorting process and the buttons.
class Timer:

    # Initializes the timer with max seconds between operations and max delay.
    def __init__(self, seconds, max):
        self.default = seconds
        self.seconds = self.default
        self.start_time = time.localtime().tm_sec
        self.max = max
        # on instance variable determines if the array is being sorted.
        self.on = True

    # ready method returns true if it has been how many seconds. Only works if the timer is on.
    def ready(self):

        if self.on:
            current_time = time.localtime().tm_sec

            # Calculates the difference from the start time and current time.
            if current_time < self.start_time:
                time_difference = (current_time + 60) - self.start_time

            else:
                time_difference = current_time - self.start_time

            if time_difference >= self.seconds:
                self.start_time = time.localtime().tm_sec
                return True

        return False

    # decrease_speed method reduces the speed of sorting by adding some time to the seconds.
    def decrease_speed(self):
        self.seconds = 2

    # increase_speed method sets the seconds to 0 to make the sorting go fast.
    def increase_speed(self):
        self.seconds = 0

    # default_speed method sets the seconds to the default seconds.
    def default_speed(self):
        self.seconds = self.default

    # stop method stops the timer.
    def stop(self):
        self.on = False

    # start method starts the timer.
    def start(self):
        self.on = True


# Initiates interface and uses the run method.
gui = Interface()
gui.run()
