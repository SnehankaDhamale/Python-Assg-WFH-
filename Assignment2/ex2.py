from pip._vendor.distlib.compat import raw_input

age = raw_input("How old are you? ") #user input
height =raw_input("How many tall are you? ")
weight =raw_input("How much do you weight? ")

print ("So, you're %r old, %r tall and %r heavy." % (
age, height, weight))
