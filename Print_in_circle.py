#print hello world 18 times in a circle
from math import pi, sqrt, ceil
string="Hello World "
text = string * 18
radius = ceil(sqrt(len(text)/(2*pi))) # calculate with 2 characters per "cell"
text_iter = iter(text)
for i in range(-radius, radius+1):
    num = ceil(sqrt(radius**2 - i**2) * 2)
    print("{:^{}}".format("".join(next(text_iter, ".") for _ in range(2*num)), 4*radius))
 
