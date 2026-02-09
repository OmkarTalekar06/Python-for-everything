
job_description = """
python machine learning data analysis sql communication teamwork
problem-solving critical-thinking
"""

resume = """
python data analysis excel teamwork problem-solving
"""


job_skills = set(job_description.lower().replace("-", " ").split())
resume_skills = set(resume.lower().replace("-", " ").split())


matched_skills = job_skills.intersection(resume_skills)
missing_skills = job_skills.difference(resume_skills)

match_percentage = (len(matched_skills) / len(job_skills)) * 100

print("Matched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nResume Match Percentage:", round(match_percentage, 2), "%")


if match_percentage >= 70:
    print("Status: Strong Match ✅")
elif match_percentage >= 40:
    print("Status: Average Match ⚠️")
else:
    print("Status: Weak Match ❌")
