import tkinter as tk
import re
import math


root = tk.Tk()

#variable to store previous answer
ans_value="0"

#calculation string
calc_value="0"
calc_var = tk.StringVar()
calc_var.set(calc_value)

def update_calc():
    calc_var.set(calc_value)

#result string
result_value="0"
result_var = tk.StringVar()
result_var.set(result_value)

def update_result():
    result_var.set(result_value)

#method to clear calculation string for eval method
def replace(expression):
    # find ²
    squared_pattern = re.compile(r'(\d+)²')
    expression = re.sub(squared_pattern, lambda match: str(float(match.group(1)) ** 2), expression)

    # find power n
    power_pattern = re.compile(r'(\d+)\^(\d+)')
    expression = re.sub(power_pattern, lambda match: str(float(match.group(1)) ** float(match.group(2))), expression)

    # find square root
    sqrt_pattern = re.compile(r'\u221a(\d+)')
    expression = re.sub(sqrt_pattern, lambda match: f'math.sqrt({float(match.group(1))})', expression)

    #replace : with /
    expression = expression.replace(":", "/")
    return expression

# called by equal button
# calculate result value
# round to three decimal points
# genereal error catching
def result():
    global calc_value
    global result_value
    global ans_value
    try:
        calc_value = replace(calc_value)
        result_value = eval(calc_value, {'math': math})
        result_value = round(result_value, 3)
        result_var.set(result_value)
        ans_value = result_value
    except Exception as e:
        print(f"An error occurred: {e}")
        result_value = "Error!"
        update_result()
    calc_value = "0"
    update_calc()

#add numbers and opperators to calculation field 
#input depends on calculation field 
def add_value(value):
    global calc_value
    global result_value
    result_value="0"
    update_result()
    if len(calc_value)==1 and calc_value[0]=="0":
        switch={
            'zero' : lambda : assign_value("0"),
            'one' : lambda : assign_value("1"),
            'two' : lambda : assign_value("2"),
            'three' : lambda : assign_value("3"),
            'four' : lambda : assign_value("4"),
            'five' : lambda : assign_value("5"),
            'six' : lambda : assign_value("6"),
            'seven' : lambda : assign_value("7"),
            'eight' : lambda : assign_value("8"),
            'nine' : lambda : assign_value("9"),
            'comma' : lambda : assign_value("."),
            'plus' : lambda : assign_value("+"),
            'minus' : lambda : assign_value("-"),
            'multiply' : lambda : assign_value("*"),
            'divide' : lambda : assign_value(":"),
            'root' : lambda : assign_value("\u221a"),
            'power2' : lambda : assign_value("0²"),
            'powerN' : lambda : assign_value("0^"),
            'open' : lambda : assign_value("("),
            'close' : lambda : assign_value(")"),
        }
    else:
        switch={
            'zero' : lambda : assign_value(calc_value+"0"),
            'one' : lambda : assign_value(calc_value+"1"),
            'two' : lambda : assign_value(calc_value+"2"),
            'three' : lambda : assign_value(calc_value+"3"),
            'four' : lambda : assign_value(calc_value+"4"),
            'five' : lambda : assign_value(calc_value+"5"),
            'six' : lambda : assign_value(calc_value+"6"),
            'seven' : lambda : assign_value(calc_value+"7"),
            'eight' : lambda : assign_value(calc_value+"8"),
            'nine' : lambda : assign_value(calc_value+"9"),
            'comma' : lambda : assign_value(calc_value+"."),
            'plus' : lambda : assign_value(calc_value+"+"),
            'minus' : lambda : assign_value(calc_value+"-"),
            'multiply' : lambda : assign_value(calc_value+"*"),
            'divide' : lambda : assign_value(calc_value+":"),
            'root' : lambda : assign_value(calc_value+"\u221a"),
            'power2' : lambda : assign_value(calc_value+"²"),
            'powerN' : lambda : assign_value(calc_value+"^"),
            'open' : lambda : assign_value(calc_value+"("),
            'close' : lambda : assign_value(calc_value+")"),
        }
    switch_function = switch.get(value)
    if switch_function:
        switch_function()

#help method to fill calculation field
def assign_value(new_value):
    global calc_value
    calc_value = new_value
    update_calc()

#remove last entered object in calculation field
def delete():
    global calc_value
    if len(calc_value)==1:
        calc_value="0"
    else:
        calc_value = calc_value[:-1]
    update_calc()

#clears calculation and result
def clear_all():
    global calc_value
    global result_value
    calc_value="0"
    result_value="0"
    update_calc()
    update_result()

# call ans variable to get answer from earlier calculation
def add_ans():
    global calc_value
    global result_value
    global ans_value
    result_value="0"
    update_result()
    if len(calc_value)==1 and calc_value[0]=="0":
        calc_value=str(ans_value)
    else:
        calc_value=str(calc_value)+str(ans_value)
    update_calc()

#CREATE ELEMENTS

#input and output 
inputDisplay = tk.Label(root, textvariable=calc_var, font=('arial',30, 'bold'),justify=tk.LEFT, wraplength=192)
outputDisplay = tk.Label(root, textvariable=result_var, font=('arial',30, 'bold'),justify=tk.LEFT, wraplength=128)

#square button
root_image = tk.PhotoImage(file="images/square-root.png")
root_button = tk.Button(root, image=root_image, command=lambda: add_value('root'))

#power 2 button
power_2_image = tk.PhotoImage(file = "images/power-2.png")
power_2_button = tk.Button(root, image=power_2_image, command=lambda: add_value('power2'))

#power button
power_n_image = tk.PhotoImage(file = "images/power-n.png")
power_n_button = tk.Button(root, image=power_n_image, command=lambda: add_value('powerN'))

# open button
open_image = tk.PhotoImage(file="images/open-parenthesis.png")
open_button = tk.Button(root, image=open_image,command=lambda: add_value('open'))

# close button
close_image = tk.PhotoImage(file="images/close-parenthesis.png")
close_button = tk.Button(root, image=close_image,command=lambda: add_value('close'))

#number 7 button
seven_image = tk.PhotoImage(file="images/seven.png")
seven_button = tk.Button(root, image=seven_image, command=lambda: add_value('seven'))

#number 8 button
eight_image = tk.PhotoImage(file = "images/eight.png")
eight_button = tk.Button(root, image=eight_image, command=lambda: add_value('eight'))

#number 9 button
nine_image = tk.PhotoImage(file="images/nine.png")
nine_button = tk.Button(root, image=nine_image, command=lambda: add_value('nine'))

#DEL button
del_image = tk.PhotoImage(file="images/del.png")
del_button = tk.Button(root, image=del_image, command=delete)

#AC button
ac_image = tk.PhotoImage(file="images/ac.png")
ac_button = tk.Button(root, image=ac_image, command=clear_all)

#number 4 button
four_image = tk.PhotoImage(file="images/four.png")
four_button = tk.Button(root, image=four_image, command=lambda: add_value('four'))

#number 5 button
five_image = tk.PhotoImage(file="images/five.png")
five_button = tk.Button(root, image=five_image, command=lambda: add_value('five'))

#number 6 button
six_image = tk.PhotoImage(file="images/six.png")
six_button = tk.Button(root, image=six_image, command=lambda: add_value('six'))

#multiply button
multiply_image = tk.PhotoImage(file="images/multiply.png")
multiply_button = tk.Button(root, image=multiply_image, command=lambda: add_value('multiply'))

#divide button
divide_image = tk.PhotoImage(file="images/divide.png")
divide_button = tk.Button(root, image=divide_image, command=lambda: add_value('divide'))

#number 1 button
one_image = tk.PhotoImage(file="images/one.png")
one_button = tk.Button(root, image=one_image, command=lambda: add_value('one'))

#number 2 button 
two_image = tk.PhotoImage(file="images/two.png")
two_button = tk.Button(root, image=two_image, command=lambda: add_value('two'))

#number 3 button
three_image = tk.PhotoImage(file="images/three.png")
three_button = tk.Button(root, image=three_image, command=lambda: add_value('three'))

#plus button 
plus_image = tk.PhotoImage(file="images/plus.png")
plus_button = tk.Button(root, image=plus_image, command=lambda: add_value('plus'))

#minus button
minus_image = tk.PhotoImage(file="images/minus.png")
minus_button = tk.Button(root, image=minus_image, command=lambda: add_value('minus'))

#zero button
zero_image = tk.PhotoImage(file="images/zero.png")
zero_button = tk.Button(root, image=zero_image, command=lambda: add_value('zero'))

#comma button
comma_image = tk.PhotoImage(file="images/comma.png")
comma_button = tk.Button(root, image=comma_image, command=lambda: add_value('comma'))

#ANS button
ans_image = tk.PhotoImage(file="images/ans.png")
ans_button = tk.Button(root, image=ans_image, command=add_ans)

#eqaul button
equal_image = tk.PhotoImage(file="images/equal.png")
equal_button = tk.Button(root, image=equal_image, command=result)


#SET SIZE OF ELEMENTS
#set the width of columns to 64 pixels
root.columnconfigure(0, minsize=64) 
root.columnconfigure(1, minsize=64)  
root.columnconfigure(2, minsize=64)  
root.columnconfigure(3, minsize=64)  
root.columnconfigure(4, minsize=64)  

#set the height of rows to 64 pixels
root.rowconfigure(0, minsize=64)  
root.rowconfigure(1, minsize=64)
root.rowconfigure(2, minsize=64)
root.rowconfigure(3, minsize=64)
root.rowconfigure(4, minsize=64)
root.rowconfigure(5, minsize=64)

#INSERT ELEMENTS
inputDisplay.grid(row=0, column=0, columnspan=3, sticky=tk.W)
outputDisplay.grid(row=0, column=3, columnspan=2, sticky=tk.W)

root_button.grid(row=1, column=0)
power_2_button.grid(row=1, column=1)
power_n_button.grid(row=1, column=2)
open_button.grid(row=1, column=3)
close_button.grid(row=1, column=4)

seven_button.grid(row=2,column=0)
eight_button.grid(row=2, column=1)
nine_button.grid(row=2, column=2)
del_button.grid(row=2, column=3)
ac_button.grid(row=2, column=4)

four_button.grid(row=3, column=0)
five_button.grid(row=3, column=1)
six_button.grid(row=3, column=2)
multiply_button.grid(row=3, column=3)
divide_button.grid(row=3, column=4)

one_button.grid(row=4, column=0)
two_button.grid(row=4, column=1)
three_button.grid(row=4, column=2)
plus_button.grid(row=4, column=3)
minus_button.grid(row=4, column=4)

zero_button.grid(row=5, column=0)
comma_button.grid(row=5, column=1)
ans_button.grid(row=5, column=3)
equal_button.grid(row=5, column=4)
root.mainloop()

