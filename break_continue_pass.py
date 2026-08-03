# Break: break immediately stops the current loop (for or while) and moves to the next line after the loop.

for i in range (100):
    if i == 51:
        break
    print(i)

# As soon as i becomes 51, the loop will break and the program will move to the next line after the loop.

# Continue: continue skips the current iteration of the loop and moves to the next iteration.

for i in range(100):
    if i == 49:
        continue
    print(i)

# As soon as i becomes 49, the loop will skip that iteration and move to the next iteration.

# pass: pass is a null statement in python. It is used as a placeholder for future code. When the pass statement is executed, it instructs to do nothingand move to the next line of code.

for i in range(100):
    pass

i = 0
while i < 5:
    print(i)
    i += 1