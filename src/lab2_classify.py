"""
Lab 2 Task 1: Grade Classification
GGY3061 - Geoscience Data Analysis

Implement the classify_grade function using if/elif/else statements.
"""

# Your Name: thandolwenkosi sakala
# Student ID: 2023073987


high_threshold = 3.0
medium_threshold = 2.0
low_threshold = 1.0

def classify_grade(grade):
    """
    Classify an ore grade value into categories.

    Args:
        grade: Numeric grade value (can be float or int)

    Returns:
        str: Classification category
            - "High Grade" if grade >= high threshold
            - "Medium Grade" if grade >= medium threshold
            - "Low Grade" if grade >= low threshold
            - "Sub-economic" if grade >= 0 but below low threshold
            - "Invalid" if grade < 0

    Note: Check README.md for YOUR specific threshold values.
    """
    # TODO: Implement the classification logic
    # 1. First check if grade is negative (Invalid)
    # 2. Then check from highest to lowest threshold
    # 3. Use the thresholds from YOUR README.md
    if(grade < 0):
        return "invalid"
    elif(grade >= high_threshold):
        return "High Grade"
    elif(grade >= medium_threshold):
        return "Medium Grade"
    elif(grade >= low_threshold):
        return "Low Grade"
    else:
        return "Sub-economic"
    
"""
grade_thresholds = {'high': 3.0, 'medium': 2.0, 'low': 1.0}
  test_samples = [1.3, 3.9, 0.3, 0.7, 4.0, 2.5, 3.8, 2.8]"""

if __name__ == "__main__":
    # Test your function with sample values
    # Replace these with YOUR test_samples from README.md
    test_grades = [1.3, 3.9, 0.3, 0.7,4.0,2.5,3.8,2.8]

    print("Grade Classification Results:")
    print("-" * 40)
    for grade in test_grades:
        result = classify_grade(grade)
        print(f"Grade {grade:6.2f} -> {result}")
