d = {} # empty dictionary
marks = {
    "Harry": 100,
    "shumbham": 56,
    "rohan": 23,
    0:"harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry":99}) #Also can add new character and there marks 
# print(marks)

print(marks.get("Harry"))
print(marks["Harry"])

# print(marks.get("Harry 2")) # Prints None
# print(marks["Harry 2"]) # Returns an error