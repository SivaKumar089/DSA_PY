# Dictionary example
student = {
    "name": "Siva",
    "age": 40,
    "skills": ["Python", "React"]
}

print(student["name"])   # Siva
print(student.get("age")) # 40

# Add new key
student["city"] = "Chennai"

# Update value
student["age"] = 41

# Delete
del student["skills"]

print(student)
