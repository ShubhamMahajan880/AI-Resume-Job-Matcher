def eligibility_status(match_percentage):
    if match_percentage >= 70:
        return "Eligible"
    elif match_percentage >= 40:
        return "Partially Eligible"
    else:
        return "Not Eligible"
