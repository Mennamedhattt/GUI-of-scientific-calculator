
from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("MM Scientific Calculator")
root.configure(background = 'white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")
calc = Frame(root)
calc.grid()

class Calc():
	def __init__(self):
		self.total=0
		self.current=''
		self.input_value=True
		self.check_sum=False
		self.op=''
		self.result=False

	def numberEnter(self, num):
		self.result=False
		firstnum=txtDisplay.get()
		secondnum=str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value=False
		else:
			if secondnum == '.':
				if secondnum in firstnum:
					return
			self.current = firstnum+secondnum
		self.display(self.current)

	def sum_of_total(self):
		self.result=True
		self.current=float(self.current)
		if self.check_sum==True:
			self.valid_function()
		else:
			self.total=float(txtDisplay.get())

	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)

	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
		self.input_value=True
		self.check_sum=False
		self.display(self.total)

	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total=self.current
			self.input_value=True
		self.check_sum=True
		self.op=op
		self.result=False

	def Clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value=True

	def All_Clear_Entry(self):
		self.Clear_Entry()
		self.total=0

	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)

	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)
	def squared(self):
		self.result = False
		self.current = math.sqrt(float(txtDisplay.get()))
		self.display(self.current)
	def cube_root(self):
		self.result =False
		self.current =float(txtDisplay.get()) ** (1/3)
		self.display(self.current)

	def sqr_nth(self):
		self.result = False
		from tkinter.simpledialog import askfloat
		n = askfloat("Input", "Enter the value of n (root degree):")
		if n is not None and n != 0:  # Ensure valid input and avoid division by zero
			self.current = float(txtDisplay.get()) ** (1 / n)
			self.display(self.current)
		else:
			self.display("Error")
			

	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def log(self):
		self.result = False
		self.current = math.log(float(txtDisplay.get()))
		self.display(self.current)
	def log_base10(self):
		self.result =False
		self.current = math.log10(float(txtDisplay.get()))
		self.display(self.current)
	def log_base2(self):
		self.result =False
		self.current = math.log2(float(txtDisplay.get()))
		self.display(self.current)
		
	def power(self):
		self.result = False
		base = float(txtDisplay.get()) 
		from tkinter.simpledialog import askfloat
		exponent = askfloat("Input", "Enter the exponent (power):")  # Get the exponent from the user
		if exponent is not None:  # Check if a valid exponent was entered
			self.current = math.pow(base, exponent)  # Raise the base to the exponent
			self.display(self.current)
		else:
			self.display("Error")  # Display an error if no valid input
            
	def exp(self):
		self.result = False
		self.current = math.exp(float(txtDisplay.get()))
		self.display(self.current)
	def mean(self):
		self.result = False
		numbers = txtDisplay.get()  # Get the input numbers from the display (e.g., "1,2,3")
		numbers_list = list(map(float, numbers.split(',')))  # Split by commas and convert to float
		self.current = sum(numbers_list) / len(numbers_list)  # Calculate the mean
		self.display(self.current)  # Display the result
	def standard_deviation(self):
		self.result = False
		numbers = txtDisplay.get()  # Get the input numbers from the display (e.g., "1,2,3")
		numbers_list = list(map(float, numbers.split(',')))  # Convert input to a list of floats
		mean = sum(numbers_list) / len(numbers_list)  # Calculate mean
		variance = sum((x - mean) ** 2 for x in numbers_list) / len(numbers_list)  # Variance
		std_dev = math.sqrt(variance)  # Standard Deviation
		self.display(std_dev)  # Display result
	def variance(self):
		self.result = False
		numbers = txtDisplay.get()  # Get the input numbers from the display (e.g., "1,2,3")
		numbers_list = list(map(float, numbers.split(',')))  # Convert input to a list of floats
		mean = sum(numbers_list) / len(numbers_list)  # Calculate mean
		variance = sum((x - mean) ** 2 for x in numbers_list) / len(numbers_list)  # Variance
		self.display(variance)  # Display result
	def linear_regression(self):
		self.result = False
		data = txtDisplay.get()  # Get the input pairs of points (e.g., "1,2; 3,4; 5,6")
		pairs = [list(map(float, pair.split(','))) for pair in data.split(';')]  # Split pairs by ';' and then numbers by ','
		x_values = [pair[0] for pair in pairs]  # X values
		y_values = [pair[1] for pair in pairs]  # Y values
		n = len(x_values)
		x_mean = sum(x_values) / n
		y_mean = sum(y_values) / n
		# Calculate slope (m) and intercept (b)
		numerator = sum((x_values[i] - x_mean) * (y_values[i] - y_mean) for i in range(n))
		denominator = sum((x_values[i] - x_mean) ** 2 for i in range(n))
		slope = numerator / denominator
		intercept = y_mean - slope * x_mean
		self.display(f"Slope: {slope}, Intercept: {intercept}")  # Display slope and intercept
	def factorial(self):
		self.result = False
		number = int(txtDisplay.get())  # Get the number from display
		result = math.factorial(number)  # Calculate factorial
		self.display(result)  # Display result
    

	def permutation(self):
		self.result = False
		try:
			# Get the input numbers in the format "n,r" (e.g., "5,2")
			numbers = txtDisplay.get()
			n, r = map(int, numbers.split('.'))  # Split the input by comma and convert to integers
			if n >= r >= 0:  # Ensure n >= r and both are non-negative
				result = math.perm(n, r)  # Calculate permutation nPr
				self.display(result)
			else:
				self.display("Error")  # Display error if values are invalid
		except (ValueError, IndexError):
			self.display("Error")  # Handle any input errors (e.g., wrong format)
	def combination(self):
		self.result = False
		try:
			# Get the input numbers in the format "n,r" (e.g., "5,2")
			numbers = txtDisplay.get()
			n, r = map(int, numbers.split('.'))  # Split the input by comma and convert to integers
			if n >= r >= 0:  # Ensure n >= r and both are non-negative
				result = math.perm(n, r)  # Calculate permutation nPr
				self.display(result)
			else:
				self.display("Error")  # Display error if values are invalid
		except (ValueError, IndexError):
			self.display("Error")  # Handle any input errors (e.g., wrong format)
        

added_value = Calc()

txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),
				bg='green',fg='white',
				bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
	for k in range(3):
		btn.append(Button(calc, width=6, height=2,
						bg='dark blue',fg='white',
						font=('Helvetica',20,'bold'),
						bd=4,text=numberpad[i]))
		btn[i].grid(row=j, column= k, pady = 1)
		btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
		i+=1
	
btnClear = Button(calc, text=chr(67),width=6,
				height=2,bg='green',fg='white',
				font=('Helvetica',20,'bold')
				,bd=4, command=added_value.Clear_Entry
				).grid(row=1 , column= 0, pady = 1)

btnAllClear = Button(calc, text=chr(67)+chr(69),
					width=6, height=2,
					bg='green',fg='white',
					font=('Helvetica',20,'bold'),
					bd=4,
					command=added_value.All_Clear_Entry
					).grid(row=1, column= 1, pady = 1)

btnsq = Button(calc, text="√",width=6, height=2,
			bg='purple', font=('Helvetica',
									20,'bold'),fg='white',
			bd=4,command=added_value.squared
			).grid(row=1, column= 2, pady = 1)
btncube = Button(calc, text="√3",width=6, height=2,
			bg='purple', font=('Helvetica',
									20,'bold'),fg='white',
			bd=4,command=added_value.cube_root
			).grid(row=2, column= 4, pady = 1)
btnsq_nth = Button(calc, text="√n",width=6, height=2,
			bg='purple', font=('Helvetica',
									20,'bold'),fg='white',
			bd=4,command=added_value.sqr_nth
			).grid(row=1, column= 4, pady = 1)

btnAdd = Button(calc, text="+",width=6, height=2,
				bg='purple',
				font=('Helvetica',20,'bold'),fg='white',
				bd=4,command=lambda:added_value.operation("add")
				).grid(row=4, column=3, pady = 1)

btnSub = Button(calc, text="-",width=6,
				height=2,bg='purple',
				font=('Helvetica',20,'bold'),fg='white',
				bd=4,command=lambda:added_value.operation("sub")
				).grid(row=3, column= 3, pady = 1)

btnMul = Button(calc, text="x",width=6, 
				height=2,bg='purple', 
				font=('Helvetica',20,'bold'),fg='white',
				bd=4,command=lambda:added_value.operation("multi")
				).grid(row=1, column= 3, pady = 1)

btnDiv = Button(calc, text="/",width=6, 
				height=2,bg='purple',
				font=('Helvetica',20,'bold'),fg='white',
				bd=4,command=lambda:added_value.operation("divide")
				).grid(row=2, column= 3, pady = 1)

btnZero = Button(calc, text="0",width=6,
				height=2,bg='dark blue',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.numberEnter(0)
				).grid(row=5, column= 0, pady = 1)

btnDot = Button(calc, text=".",width=6,
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.numberEnter(".")
				).grid(row=5, column= 1, pady = 1)

btnEquals = Button(calc, text="=",width=6,
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.sum_of_total
				).grid(row=5, column= 3, pady = 1)
btnMean = Button(calc, text="Mean",width=6, height=2,
                 bg='purple',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.mean
                 ).grid(row=4, column=6, pady=1)

# ROW 1 :
btnPi = Button(calc, text="π",width=6,
			height=2,bg='purple',fg='white', 
			font=('Helvetica',20,'bold'),
			bd=4,command=added_value.pi
			).grid(row=5, column= 2, pady = 1)

btnCos = Button(calc, text="Cos",width=6, 
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.cos
			).grid(row=1, column= 5, pady = 1)

btntan = Button(calc, text="tan",width=6, 
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.tan
			).grid(row=1, column= 6, pady = 1)

btnsin = Button(calc, text="sin",width=6,
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.sin
			).grid(row=1, column= 7, pady = 1)

# ROW 2 :

btnCosh = Button(calc, text="Cosh",width=6,
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.cosh
				).grid(row=2, column= 5, pady = 1)

btntanh = Button(calc, text="tanh",width=6, 
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.tanh
				).grid(row=2, column= 6, pady = 1)

btnsinh = Button(calc, text="sinh",width=6, 
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.sinh
				).grid(row=2, column= 7, pady = 1)

# ROW 3 :
btnlog = Button(calc, text="log",width=6,
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.log
			).grid(row=3, column= 4, pady = 1)

btnExp = Button(calc, text="e^x",width=6, height=2,
				bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.exp
			).grid(row=3, column= 5, pady = 1)

btFactorial = Button(calc, text="n!",width=6,
				height=2,bg='purple',fg='white', 
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.factorial
				).grid(row=3, column= 6, pady = 1)

btnE = Button(calc, text="e",width=6, 
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.e
			).grid(row=3, column= 7, pady = 1)

btnlog10 = Button(calc, text="log10",width=6, 
				height=2,bg='purple',fg='white', 
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.log_base10
				).grid(row=4, column= 4, pady = 1)


btnlog2 = Button(calc, text="log2",width=6, 
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.log_base2
				).grid(row=5, column= 4, pady = 1)
btnpower = Button(calc, text="xn",width=6, 
				height=2,bg='purple',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.power
				).grid(row=4, column= 5, pady = 1)
btnStdDev = Button(calc, text="StdDev",width=6, height=2,
                   bg='purple',fg='white',
                   font=('Helvetica',20,'bold'),
                   bd=4,command=added_value.standard_deviation
                   ).grid(row=4, column=7, pady=1)

btnVariance = Button(calc, text="Vari",width=6, height=2,
                     bg='purple',fg='white',
                     font=('Helvetica',20,'bold'),
                     bd=4,command=added_value.variance
                     ).grid(row=5, column=5, pady=1)

btnRegression = Button(calc, text="Lin Reg",width=6, height=2,
                       bg='purple',fg='white',
                       font=('Helvetica',20,'bold'),
                       bd=4,command=added_value.linear_regression
                       ).grid(row=6, column=8, pady=1)

btnPermutation = Button(calc, text="nPr",width=6, height=2,
                        bg='purple',fg='white',
                        font=('Helvetica',20,'bold'),
                        bd=4,command=added_value.permutation
                        ).grid(row=5, column=7, pady=1)

btnCombination = Button(calc, text="nCr",width=6, height=2,
                        bg='purple',fg='white',
                        font=('Helvetica',20,'bold'),
                        bd=4,command=added_value.combination
                        ).grid(row=5, column=6, pady=1)




lblDisplay = Label(calc, text = "Scientific Calculator",
				font=('Helvetica',25,'bold'),
				bg='white',fg='green',justify=CENTER)

lblDisplay.grid(row=0, column= 4,columnspan=4)

def iExit():
	iExit = tkinter.messagebox.askyesno("Scientific Calculator",
										"Do you want to exit ?")
	if iExit>0:
		root.destroy()
		return

def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("944x568+0+0")


def Standard():
	root.resizable(width=False, height=False)
	root.geometry("480x568+0+0")

menubar = Menu(calc)

# ManuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

# ManuBar 2 :
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

root.config(menu=menubar)

root.mainloop()

