# =======================================================
# Program Name:		variables_by_rfw.py
# By:				Robert F Woods
# Date:				March 26 2015
# Course:			CSC 119 310
# Course Project:	This program is to demonstrate the 
# proper construction and discuss potential applications
# of the 8 variable types.
# =======================================================


def main():
	str_fun()
	int_fun()
	float_fun()
	boolean_fun()
	list_fun()
	tuple_fun()
	dictionary_fun()
	set_fun()

def str_fun():
	narrow_line()
	print("Code used to establish str_var is str_var = 'string'")
	str_var = 'string'
	print('str_var currently references ',str_var)
	print('The variable type is ',type(str_var))
	print('The length of str_var is',len(str_var))

def int_fun():
	narrow_line()
	print("Code used to establish int_var is int_var = 111")
	int_var = 111
	print('int_var currently references ',int_var)
	print('The variable type is ',type(int_var))
	int_var = str(int_var)
	print('The length of int_var is',len(int_var))

def float_fun():
	narrow_line()
	print("Code used to establish float_var is float_var = 111.22 / 2")
	float_var = 111.22 / 2
	print('float_var currently references ',float_var)
	print('The variable type is ',type(float_var))
	float_var = str(float_var)
	print('The length of float_var is',len(float_var))

def boolean_fun():
	narrow_line()
	print("Code used to establish boolean_var is boolean_var = True")
	boolean_var = True
	print('boolean_var currently references ',boolean_var)
# print('The length of boolean_var is',len(boolean_var))
	print('The variable type is ',type(boolean_var))
	print('Booleans do not have a length')

def list_fun():
	narrow_line()
	print("Code used to establish list_var is list_var = ['string']")
	list_var = ['string']
	print('list_var currently references ',list_var)
	print('The variable type is ',type(list_var))
	print('The length of list_var is',len(list_var))

def tuple_fun():
	narrow_line()
	print("Code used to establish tuple_var is tuple_var = ('string',)")
	tuple_var = ('string',)
	print('tuple_var currently references ',tuple_var)
	print('The variable type is ',type(tuple_var))
	print('The length of tuple_var is',len(tuple_var))


def dictionary_fun():
	narrow_line()
	print("Code used to establish dictionary_var is dictionary_var = {'RJ11':'phone','RJ45':'ethernet'}")
	dictionary_var = {'RJ11':'phone','RJ45':'ethernet'}
	print('dictionary_var currently references ',dictionary_var)
	print('The variable type is ',type(dictionary_var))
	print('The length of dictionary_var is',len(dictionary_var))

def set_fun():
	narrow_line()
	print("Code used to establish set_var is set_var = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}")
	set_var = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
	print('set_var currently references ',set_var)
	print('The variable type is ',type(set_var))
	print('The length of set_var is',len(set_var))

def narrow_line():
	print('-'*40)

main()
