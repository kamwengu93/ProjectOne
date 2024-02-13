courses = ["MIT", "Cybersecurity", "Data Science"]
print(courses)
# accessing an element in an array
print(courses[0])
print(courses[1])
print(courses[2])
# looping through an array
for course in courses:
    print(course)

# adding a new element into an array
courses.append("Android Programming")
print(courses)


# Deleting an element from an array
courses.remove("Data Science")
print(courses)

