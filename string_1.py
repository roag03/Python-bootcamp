# First string class



# name = "rohit"
# friend = "Yash"


# apple= ''' he said,
# hi rohit
# hey i am good 
# "i want eat apple"   '''

#    2nd string class



# print ("hello, " + name)
# print(apple)


# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# for raj in name:
#     print(raj)


# rohit = "a dumb boy"
# she = len(rohit)
# print(she)
# print(rohit[0:9])
# print(rohit[len(rohit)-2])

# #    print(rohit[-5:len(rohit) -1])
# print(rohit[-3:-1])

# rt ="rohit"
# print(rt[-4:-2])


# 3rd string class



# STRINGS ARE IMMUTABLE


a= "!!!Rohit!!  !!Rohit!!  yash anant "

print(len(a))

print(a.upper())

print(a.lower())

print(a.rstrip("!"))

print(a.replace("Rohit","Yash"))

print(a.split(" "))

blogHeading= "rohit is learning python"
#  it convert the first letter of string to cpital letter and other in small letter

print(blogHeading.capitalize())

rd1= "Welcome to Ayodhya!!"
print(len(rd1))

print(len(rd1.center(50)))

print(a.count("Rohit"))

rd1= "Welcome to Ayodhya !!"

print(rd1.endswith("!!"))

rd1= "Welcome to Ayodhya !!"

print(rd1.endswith("to",4,10))

rd2 = "his name is Yash.he is very honest guy"
print(rd2.find("is"))
 
#  isalnum is use to detect the string is alpha numeric value or not

rd3= "swagatam"
print(rd3.isalnum())

rd4 = "swagatam"
print(rd4.isalpha())

rd1 = "namaste duniya"
print(rd1.islower())

rd1 = "namaste duniya]\n"
# coz \n is not printable

print(rd1.isprintable())

rd2="     "
print(rd2.isspace())

rd1 = "namaste duniya"
print(rd1.istitle())

rd1 = "namaste duniya"
print(rd1.swapcase())

rd2 = "his name is Yash.he is very honest guy"
print(rd2.title())