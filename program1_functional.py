
#IMPERATIVE

names = ["harry", "ravi", "k", "ramesh", "p"]

# Step 1: Filter out one-character names
step_one = []
for name in names:
    if len(name) > 1:
        step_one.append(name)

# Step 2: Transform - Capitalize the first letter of each name
step_two = []
for name in step_one:
    step_two.append(name.capitalize())

# Step 3: Convert - Join the names with commas to form a single string
ans = ""
for i in range(len(step_two)):
    if i == len(step_two) - 1:  # If it's the last element, no comma after it
        ans += step_two[i]
    else:
        ans += step_two[i] + ","

# Output the result
print(ans)






#FUNCTIONAL

names=["harry","ravi","k","ramesh","p"]

# Three steps: Filter -> transform -> convert

'''
Filter: To remove one character names.
Transform: To capitalize first character.
Convert: To convert list to string with commas.
'''

# Filter
step_one=list(filter(lambda name: len(name)>1,names))

#Transform
step_two = list(map(lambda name: name.capitalize(), step_one))


#convert
ans=""
ans=",".join(step_two)

#output
print(ans)
