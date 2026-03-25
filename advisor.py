def recommend_stream(math, science, english, interest):
    if math > 75 and interest == "Technology":
        return "Maths Stream (Engineering / IT)"
    elif science > 75:
        return "Biological Science (Medical)"
    elif english > 65 and interest == "Business":
        return "Commerce Stream"
    elif interest == "Arts":
        return "Arts Stream"
    else:
        return "Technology Stream"


def generate_ai_explanation(level, stream, subjects):
    return f"""
🧠 AI Analysis Report:

You are currently performing at a {level} level.

Based on your academic strengths, we recommend:
👉 {stream}

Suggested key subjects:
👉 {", ".join(subjects)}

Focus on improving weaker areas while maintaining your strengths.
This AI system helps guide your academic and career path effectively.
"""


def generate_full_advice(level, interest, math, science, english):
    study_plan = {
        "High Performer": "Advanced courses + projects + competitions",
        "Good": "Regular study + practice past papers",
        "Average": "Daily 2–3 hour study + focus weak subjects",
        "Below Average": "Extra classes + revision plan",
        "Needs Improvement": "Daily guided study + basics focus",
        "At Risk": "Counseling + strict monitoring",
        "Critical": "Start from fundamentals with teacher support"
    }

    subject_advice = {
        "Technology": ["Mathematics", "Computer Science", "Physics"],
        "Arts": ["History", "Literature", "Fine Arts"],
        "Business": ["Economics", "Accounting", "Business Studies"]
    }

    career_advice = {
        "High Performer": "Software Engineer, Doctor, AI Specialist",
        "Good": "Engineer, Analyst, Designer",
        "Average": "Teacher, Technician, Business roles",
        "Below Average": "Vocational training, Skill-based careers",
        "Needs Improvement": "Certifications, Technical skills",
        "At Risk": "Guided career planning required",
        "Critical": "Focus on basic education first"
    }

    # 🔥 NEW FEATURES
    stream = recommend_stream(math, science, english, interest)
    subjects = subject_advice.get(interest, ["General Studies"])
    explanation = generate_ai_explanation(level, stream, subjects)

    return {
        "study_plan": study_plan.get(level, ""),
        "subjects": subjects,
        "career": career_advice.get(level, ""),
        "stream": stream,
        "explanation": explanation
    }