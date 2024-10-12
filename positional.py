def greet(name,msg="good morning"):
    print("hello",name+','+msg)
greet(name="bruce",msg="how do you do?")  
greet(msg="how do you do?",name="bruce")
greet("bruce",msg="how do you do?")
greet("bruce","how do you do?")
#greet(name="bruce","how do you do?") SyntaxError: positional argument follows keyword argument
greet("how do you do?","kate")
