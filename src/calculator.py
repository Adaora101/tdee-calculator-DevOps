import json
import os


def convert_lbs_to_kg(lbs):
    """Converts pounds to kilograms."""
    
    pass

def convert_inches_to_cm(inches):
    """Converts inches to centimeters."""
    
    pass

def calculate_bmr(weight_kg, height_cm, age_years, gender):
    """Calculates Basal Metabolic Rate using the Mifflin-St Jeor equation."""
    if weight_kg < 0 or height_cm < 0 or age_years < 0:
        raise ValueError("Inputs cannot be negative")
    
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years)
    if gender.lower() == 'male':
        return bmr + 5
    elif gender.lower() == 'female':
        return bmr - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")
    

def calculate_tdee(bmr, activity_level):
    """Calculates Total Daily Energy Expenditure based on activity multiplier."""
    multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'very_active': 1.725,
        'extreme': 1.9
    }

    level = activity_level.lower()
    if level not in multipliers:
        raise ValueError(f"Invalid activity level. Choose from {list(multipliers.keys())}")

    return bmr * multipliers[level]
    
    

def get_calorie_goals(tdee):
    """Returns calorie targets for cutting, maintaining, and bulking."""
    
    pass

def calculate_macros(calories):
    """Calculates recommended macro splits (30% protein, 40% carbs, 30% fat)."""
    
    pass

def save_results_to_file(filepath, results_dict):
    """Saves calculation results to a JSON file."""
    
    pass

def main():
    print("=== TDEE Calculator (Under Development) ===")

    pass

if __name__ == "__main__":
    main()
