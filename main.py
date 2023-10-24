list1 = ['main', 'main',]

from testTwo import Test



def greet( greeting: str, *names) -> int:
	meow = 'hello meow'
	print(meow, greeting, names[1])
	return 123

result = greet('123f', 'mmm', 'hhh')
print(result)

def meow(num1Arg: int | float, num2Arg: int | float) -> int:
	result = num1Arg + num2Arg



	return result



if False or True:
	print('123')

if False | True:
	print('123')


class Calculator():
	num1 = 3
	__num2 = 2

	def plus(self) -> int:
		return self.num1 + self.__num2







INSTANCE_CALC = Calculator()
# print(INSTANCE_CALC.__num2) private atr in class 




print(INSTANCE_CALC.plus())


INSTANCE_CALC = 0

print(INSTANCE_CALC)


calc = []


num1: int = 10
num2: float = 2.5


result: float = num1 + num2


print(meow(1,2.5))

print(type(result))
 

if type(calc) == list: 
	print('meow')


obj = {
	"name": str(123)
}



# for(i = 0, i < 10, i++):
i = 0
while i < 6:
	print('13')
	i += 1


for j in list1: 
	print('close', j) 
	#like a for each in js 


obj2 = {
	'name': 'nick',
	'age': 'eith'
}
 


print(obj['name'])



for value in obj2:
	print(obj2[str(value)])



for x in range(3,5):
	print(x)




listmeow = [
	[1,1,1],
	[1,3,1],
	[1,2,1],
	[1,2,1],
]
 
for listi in listmeow:
	print(listi)
	for x in listi:
		print(x)



# meow kjfsaljf;akjfakfjslkjf a;kjf askljf a;kljdfTTODODOOTOOTOT TODO:CRETESFDF"SD:LFKklsajflkjsafklajf;alsjkfalksjfalksjfalskd

# test = `mew`

'''
	big
'''




try: 
	x: int = int(input('meow '))
	print(x)
except ValueError: 
	print('хуй')
	# print('value is wrong', ValueError.args.__annotations__)
finally:
	print('finish')


result = open("./test.txt", "r")
# print(result.readfable())

for line in result.readlines():
	print(line)


result = open("./test.txt", "w")
result.write('this a text')


result = open("./test.txt", "a")
result.write('this a text new')


print(result)

result.close()




class Person:
	def __init__(self, name: str, age: int) -> None:
		self.__name = name
		self.__age = age
		pass





p1 = Person('Nick', 25)
print(p1)


p2 = Test()

print(p2.value)