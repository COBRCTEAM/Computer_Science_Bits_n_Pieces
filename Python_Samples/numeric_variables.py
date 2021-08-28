# =======================================================
# Program Name:		numeric_variables.py
# By:				Robert F Woods
# Date:				December 25, 2020
# Objective:	This program is to demonstrate the 
# proper construction of various numeric variables. 
# =======================================================


def main():
	int_fun()
	int_display()
	octal_int_fun()
	experiment()
#   float_fun()




def int_fun():
	narrow_line()
	print("Code used to establish int_var is int_var = 14")
	int_var = 14
	print('int_var currently references ',int_var)
	print('The variable type is ',type(int_var))
	int_var = str(int_var)
	print('The length of int_var is',len(int_var))
		
def int_display():
# Display the integer in other numeral systems
# Base 2, 8, and 16. AKA Binary, Octal, and Hexadecimal.
	narrow_line()
	int_var = 14
	print('int_var displayed as Binary      ',bin(int_var))
	print('int_var displayed as Octal       ',oct(int_var))
	print('int_var displayed as Hexadecimal ',hex(int_var))
	print('int_var displayed using repr			',repr(int_var))
	
	
def octal_int_fun():
	narrow_line()
	print("Code used to establish octal_int_var is octal_int_var = 0o1111")
	octal_int_var = 0o1111
	print('octal_int_var currently references ',octal_int_var)
	print('The variable type is ',type(octal_int_var))
	octal_int_var = str(octal_int_var)
	print('octal_int_var displayed using repr			',repr(octal_int_var))
	print('The length of octal_int_var is',len(octal_int_var))
	
def experiment():
	narrow_line()
	instring = '0b11111111'
	int_var = 0b11111111
	samovar = 0b11111111
# print('length of samovar',len(samovar))
	print('Source value = ',instring,' Integer value = ', int_var,' Type = ',type(int_var),' Length = ')
	print('int_var displayed using repr							',repr(int_var))
	print('int_var displayed using str							',str(int_var))
	print('int_var displayed using binary						',bin(int_var))
	print('int_var displayed using octal						',oct(int_var))
	print('int_var displayed using hexadecimal			',hex(int_var))
# print(len(int_var))

def float_fun():
	narrow_line()
	print("Code used to establish float_var is float_var = 111.22 / 2")
	float_var = 111.22 / 2
	print('float_var currently references ',float_var)
	print('The variable type is ',type(float_var))
	float_var = str(float_var)
	print('The length of float_var is',len(float_var))

def narrow_line():
	print('-'*40)

main()
