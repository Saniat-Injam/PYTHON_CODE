text = "ice cream"
print(text)

print(text[0])
print(text[1])
print(text[2])

"""
text[0]  = k
It is not possible because strings are immutable. Once you create you can not change them. You can 
place another string into this variable but you can not cannot partially change it. Just remember that 
strings are immutable in python programming language. Other programming languages such as C++ Java 
they will allow you to do it but not python.

"""
txt = "soft drinks"
new_txt = txt[0:4]

print(new_txt)

print(txt[0:11])

print(txt[0: ])

print(txt[ :4])

print(txt[ : ])

# String concatenation
s1  = "Hello"
s2  = "World"
s3 = s1 + " " + s2
print(s3) 

some_text = "Total districs in Bangladesh: "
districs = 64
result = some_text + str(districs)
print(result)
