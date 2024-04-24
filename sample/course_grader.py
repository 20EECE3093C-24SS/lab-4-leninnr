# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    """
    Converts a student’s numerical score into a corresponding letter grade.

    Args:
        score (int or float): The numerical score of the student.

    Returns:
        str: The letter grade corresponding to the score.

    Raises:
        ValueError: If the score is outside the range 0 to 100.
        TypeError: If the score is not an int or float.
    """
    # Check if the score is a numeric value
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")

    # Check if the score is within the valid range
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    # Determine the letter grade based on score ranges
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
