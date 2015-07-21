import first_operation

num1 = 12
num2 = 4

added_nums = first_operation.add(num1, num2)
subtracted_nums = first_operation.subtract(num1, num2)
multiplied_nums = first_operation.multiply(num1, num2)
divided_nums = first_operation.divide(num1, num2)

print "{} + {} = {}".format(num1, num2, added_nums)
print "{} - {} = {}".format(num1, num2, subtracted_nums)
print "{} * {} = {}".format(num1, num2, multiplied_nums)
print "{} / {} = {}".format(num1, num2, divided_nums)