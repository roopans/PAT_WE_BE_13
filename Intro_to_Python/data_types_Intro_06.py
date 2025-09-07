# type conversion

integer_number = 1232
print(type(integer_number))
float_number = 12.3
new_number = integer_number + float_number

print("value:",  new_number)
print("data type:", type(new_number))
print("******************************")
num_string = '12'
num_integer = 12
print(type(num_string))
print(type(num_integer))

# explicit type conversion
num_string = int(num_string)
print(type(num_string))
num_sum = num_string + num_integer
print(type(num_sum))
print("Sum:",num_sum)

# Float to int
a=5.9
b=2
c = int(a)+int(b)
print("flaot to Int:",c)

# string to int
a="59"
b=2
c = int(a)+int(b)
print("string to Int:",c)

# boolean to int
print(int(True))
print(int(False))




