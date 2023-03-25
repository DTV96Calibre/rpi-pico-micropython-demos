filename = "hello.txt"

with open("hello.txt") as f:
    text = f.read()
    
print(text)