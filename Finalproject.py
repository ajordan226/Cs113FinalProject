# Antonio Jordan (Afternoon Session) CSC 11300

from tkinter import *
from tkinter import messagebox
from collections import Counter
import turtle
from itertools import cycle

#Read text file
fileName = input('Enter file name: ')
my_File = open(fileName, 'r')

dictionary = {}
for i in my_File.read():
	dictionary[i] = dictionary.get(i, 0) + 1

my_File.close()


#Interface
root = Tk()
label = Label(root, text = 'Input number of number of letters (n): ')
label.grid(row = 0)
entry = Entry(root)
entry.grid(row = 0, column = 1)

n = 0
def callback():
	global n
	if int(entry.get()) <= 54:
		n = int(entry.get())
		root.destroy()
	else:
		messagebox.showwarning('Warning', 'n must be 54 or less')

button1 = Button(root, text = 'Submit', command = callback)
button1.grid(row = 1, column = 3)

root.mainloop()


#Handle whitespace characters
for k in dictionary.keys():
	if k == '\n':
		dictionary['\\n'] = dictionary.pop('\n')
	if k == '\t':
		dictionary["\\t"] = dictionary.pop('\t')
	if k == " ":
		dictionary['" "'] = dictionary.pop(" ")


SumOfAllFreq = 0
for v in dictionary.values():
	SumOfAllFreq += v


sorted_d = dict(Counter(dictionary).most_common(n))
probabilities = {}

#Probability of letters
for k in sorted_d.keys():
	probOfLetter = sorted_d[k] / SumOfAllFreq
	probabilities[k] = round(probOfLetter, 4)

#Probability of All Other Letters
SumOfAllFreq2 = 0
for values in probabilities.values():
	SumOfAllFreq2 += values


if SumOfAllFreq2 != 1:
	d = 1 - SumOfAllFreq2
	probabilities['All other letters'] = round(d, 4)


#Pie Chart
colors = cycle(['blue', 'yellow', 'green', 'purple', 'grey', 'black', 'magenta', 'pink'])

pie = turtle.Turtle()
pie.color('black')
pie.width(1)
pie.penup()
pie.setposition(0, -100)

for v in probabilities.values():
	pie.fillcolor(next(colors))
	pie.begin_fill()
	pie.pendown()
	pie.circle(100, v * 360)
	position = pie.position()
	pie.goto(0, 0)
	pie.end_fill()
	pie.setposition(position)

pie.penup()
pie.setposition(0, -150)

for k, v in probabilities.items():
	pie.circle(150, v * 360 / 2)
	pie.write(k + ', ' + str(v), align = 'center')
	pie.circle(150, v * 360 / 2)

pie.hideturtle()

turtle.mainloop()

	

