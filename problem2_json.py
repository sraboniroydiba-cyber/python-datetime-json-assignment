import json

student = {
    "name": "Diba",
    "age": 21,
    "department": "CSE"
}

json_string = json.dumps(student)

print(json_string)