LEARNING_MAP = {
    "python": "Practice scripting, problem-solving, and backend development.",
    "data structures": "Learn arrays, stacks, queues, trees, and graphs.",
    "algorithms": "Focus on sorting, searching, recursion, and dynamic programming.",
    "sql": "Practice joins, subqueries, indexes, and normalization.",
    "docker": "Learn containerization and basic DevOps workflows.",
    "react": "Understand hooks, component lifecycle, and state management.",
    "node": "Learn REST APIs, middleware, and authentication.",
    "machine learning": "Study supervised, unsupervised learning, and model evaluation."
}

def learning_recommendations(missing_skills):
    recommendations = []
    for skill in missing_skills:
        if skill in LEARNING_MAP:
            recommendations.append(f"{skill.title()}: {LEARNING_MAP[skill]}")
        else:
            recommendations.append(f"{skill.title()}: Learn fundamentals and apply them in a project.")
    return recommendations
