# Break
# Based on condition fall out of the loop
# Break only used with loop
for i in range(0, 11):
    if i == 5:
        break
    print(i)

print("Outside the loop")

for i in range(10):
    if i == 5:
        pass
    else:
        print(i)

# Pass
# Do nothing
# Skip the condition without doing anything
for i in range(1, 11):
    if i == 5:
        pass
    print(i)

print("This is pass")
