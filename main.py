student = {
    'name' : 'maggie',
    'age' : 15 , 
    'hobby' : 'reading',
}

print(student)
print(student['age'])
print(student['hobby'])
print(student.keys())
print(student.values())

student["marks"]=[90,80,100]
print(student)

for i in student.keys():
    print(i,':', student[i])

if 'marks' in student :
    print('key is there')
else:
    print('nope')

del (student['hobby'])
print(student)

print(student['marks'][2])

classroom = {
    "remi" : {
        "age" : 12,
        "hobby": "dancing"
    },
    "olivia" : {
        "age" : 11,
        "hobby" : "singing"
    }
}

print(classroom)
print(classroom.keys())
print(classroom.values())
print(classroom['olivia']["hobby"])

for p in classroom.keys() :
    print(p, ":" , classroom[p])

print(len(student))

if "Derrick" in classroom:
    print("Derrick is in classroom")
else:
    print("Who's Derrick??")

classroom["Derrick"]={"age" : 35, "hobby" : "coding"}

print(classroom)

if "Derrick" in classroom:
    print("Derrick is in classroom")
else:
    print("Who's Derrick??")

del (classroom["olivia"])

print(classroom)