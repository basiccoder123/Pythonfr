student_data = {
    "id1": {
        "name": "Kirk",
        "class": "7A",
        "subject_integration": ["Math", "OWOP"],
    },
    "id2": {
        "name": "Kwasi",
        "class": "8L",
        "subject_integration": ["Science", "Music"],
    },
    "id3": {
        "name": "Kirk",
        "class": "7A",
        "subject_integration": ["Math", "OWOP"],
    },
    "id4": {
        "name": "Adwoa",
        "class": "9L",
        "subject_integration": ["History", "English"]
    },
}

result = {}
seen = set()

for student_id, details in student_data.items():
    # Normalize subject_integration to a tuple for use in a set
    subjects = details.get("subject_integration")
    if isinstance(subjects, list):
        subjects_key = tuple(subjects)
    else:
        subjects_key = (subjects,)

    unique_key = (
        details["name"],
        details["class"],
        subjects_key,
    )
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_id] = details

for student_id, details in result.items():
    print(f"{student_id} : {details}")
