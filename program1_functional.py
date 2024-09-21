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