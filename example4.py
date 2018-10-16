import statistics

example_list = [4,6,2,6,7,8,2,5,6,78,4]

x = statistics.mean(example_list)
y = statistics.stdev(example_list)
z = statistics.variance(example_list)

print(x)
print(y)
print(z)