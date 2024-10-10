p1 = "Make a lot of money" 
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comments:")
#have put bracket because its easy to read can also be writteb without brackets
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")