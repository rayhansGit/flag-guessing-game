"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150161349
Name:       Md Rayhan Al Islam
Email:      md.islam@tuni.fi

Project for programming 1 course:
I have designed a flag guessing game using the tkinter ui library. The game is simple and fun to play
First step is providing the number of rounds you want to play. After that, the flag images will start poping and
you have to guess the name of that country.
After finishing the round, the result window will pop up and show you the total right guesses you made. You are allowed
to write the country name in caps or lower case.
The system is designed in such a way that it will show random flags everytime you run this
"""
import os
import random
from tkinter import *
directory = 'flags'

class flag_guessing:
    def __init__(self):
        self.__mainwindow = Tk()
        self.correct_answers = Entry(self.__mainwindow)
        self.__total_questions = 0
        self.__rounds = Entry(self.__mainwindow)
        self.__rounds.grid(row=2, column=1)
        self.__get_round_btn = Button(self.__mainwindow, text="Set round", command=self.run_rounds, bg='#A877BA')
        self.__get_round_btn.grid(row=3, column=1)
        self.__top_msg = Label(self.__mainwindow, text="How many rounds you want to play?")
        self.__top_msg.grid(row=0, column=0, columnspan=6)
        self.__currentFlagName = ""
        self.__enteredFlagName = ""
        self.__result = []
        self.__question_window = ""
        self.__result_window = ""

    def run_rounds(self):
        """
        this method starts the execution of showing flags depending on the number of rounds user wants to play
        """
        self.__total_questions = self.__rounds.get()
        # remove the number of round window
        self.__mainwindow.destroy()

        #storage for all the country names
        countries = []
        #storage for randomly picked country names
        selected_countries = []

        #traverse the directory and store the country names in the countries list
        for filename in os.listdir(directory):
            countries.append(filename)

        #store the randomly picked countries by the system
        for i in range(0, int(self.__total_questions)):
            random.randint(0, len(countries))
            selected_countries.append(countries[random.randint(0, len(countries))])

        #start showing country images
        for i in range(0, len(selected_countries)):
            self.__question_window = Tk()
            image = PhotoImage(file=directory+"/"+selected_countries[i])
            label = Label(image=image)
            label.grid(row=0,column=0)
            button = Button(self.__question_window, text="Next", bg='#f1f1f1', command=self.save_result)
            button.grid(row=1,column=1)
            self.__enteredFlagName = Entry(self.__question_window)
            self.__enteredFlagName.grid(row=1, column=0)
            self.__currentFlagName = selected_countries[i]
            self.__question_window.mainloop()
        self.__result_window = Tk()
        result = Label(self.__result_window, text="Your Total Score is "+str(sum(self.__result))+"/"+str(len(self.__result)))
        result.pack()
        self.__result_window.mainloop()

    def save_result(self):
        """
        compare the country named entered by user with the correct answer
        """
        if self.__enteredFlagName.get() != "":
            if self.__currentFlagName.lower() == "flag_of_"+self.__enteredFlagName.get().lower()+".png":
                self.__result.append(1)
            else:
                self.__result.append(0)

            # destroy current flag window after user is done inputing the country name and clicked the next button
            self.__question_window.destroy()

    def stop(self):
        self.__mainwindow.destroy()

    def start(self):
        self.__mainwindow.mainloop()


def main():
    ui = flag_guessing()
    ui.start()


if __name__ == "__main__":
    main()
