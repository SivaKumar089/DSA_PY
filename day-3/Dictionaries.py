
student = {
    "name": "Siva",
    "age": 40,
    "skills": ["Python", "React"]
}

print(student["name"])   
print(student.get("age"))

student["city"] = "Chennai"


student["age"] = 41


del student["skills"]

print(student)
