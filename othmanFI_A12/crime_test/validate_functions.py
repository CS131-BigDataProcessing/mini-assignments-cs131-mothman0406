# validate_functions.py

def validate_sex(sex):
    """Validates that 'Vict sex' is either 'M' or 'F'."""
    if sex not in ['M', 'F']:
        raise ValueError("Vict sex must be 'M' or 'F'.")
    return True

def validate_age(age):
    """Validates that 'Vict age' is between 1 and 100."""
    if age is None:
        raise ValueError("Vict age cannot be NULL.")
    if not (1 <= age <= 100):
        raise ValueError("Vict age must be between 1 and 100.")
    return True

