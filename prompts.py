def career_prompt(name, age, course, city):

    return f"""
ROLE:
You are an experienced career counselor with over 15 years of experience.

CONTEXT:
Student Details:
Name: {name}
Age: {age}
Course: {course}
City: {city}

TASK:
1. Suggest suitable career paths.
2. Suggest skills to learn.
3. Recommend higher studies.
4. Predict career opportunities in 2030 and 2035.
5. Give a year-wise roadmap.

CONSTRAINTS:
- Maximum 200 words.
- Use headings.
- Give list of 10-14 points.
- Keep the advice practical.
"""