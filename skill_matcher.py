# Step 1: Install fuzzywuzzy
# pip install fuzzywuzzy[speedup]

from fuzzywuzzy import fuzz

def extract_skills(text, skills_list):
    found_skills = []
    for skill in skills_list:
        if fuzz.partial_ratio(skill.lower(), text.lower()) > 80:  # match threshold
            found_skills.append(skill)
    return found_skills