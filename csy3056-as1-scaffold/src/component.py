
def assess_mental_health_risk(age, stress, mood, sleep_amount, panic_attacks, missed_commitments, suicidal_thoughts):

    """ Mental health risk assessor function.

    Funtion contains main logic needed in order to assess the mental health risk of a patient. 

    Main parameters required:
        age (int): Age of patient
        stress (int): Stress level of patient scale of (1-10)
        mood (int): Mood level of patient scale of (1-10)
        sleep_amount (int): Average hours of sleep (per night)
        panic_attacks (int): Number of panic attacks (per week)
        missed_commitments (int): Number of missed commitments (per week)
        suicidal_thoughts (bool): Whether the patient has suicidal thoughts (True/False)

    Returns:
        risk (str): Risk level of patient (Low, Moderate, High or Critial Risk)
    """

    # Input validation
    if age < 0 or age > 100:
        raise ValueError("Age must be between 0 and 100.")
    
    if not 1 <= stress <= 10:
        raise ValueError("Stress level must be between 1 and 10.")
    
    if not 1 <= mood <= 10:
        raise ValueError("Mood level must be between 1 and 10.")
    
    if sleep_amount < 0 or sleep_amount > 24:
        raise ValueError("Sleep amount must be between 0 and 24 hours.")
    
    if panic_attacks < 0:
        raise ValueError("Number of panic attacks cannot be negative.")
    
    if missed_commitments < 0:
        raise ValueError("Number of missed commitments cannot be negative.")
    
    if not isinstance(suicidal_thoughts, bool):
        raise ValueError("Suicidal thoughts must be Yes/No.")
    
    # Risk Assessment Logic:
    # Immediate critical risk if suicidal thoughts are present
    if suicidal_thoughts == True:
        return "Risk level is Critical"

    # Weighted scoring system based on various factors (higher score indicates higher risk)
    risk_score = 0

    # Stress (0-3 scoring points (higher stress = higher risk))
    if stress >= 8:
        risk_score += 3
    elif stress >= 5:
        risk_score += 2
    elif stress >= 3:
        risk_score += 1

    # Mood (0-3 scoring points (lower mood = higher risk))
    if mood <= 3:
        risk_score += 3
    elif mood <= 5:
        risk_score += 2
    elif mood <= 7:
        risk_score += 1

    # Sleep amount (0-2 scoring points (less sleep = higher risk))
    if sleep_amount < 4:
        risk_score += 2
    elif sleep_amount < 6:
        risk_score += 1
    elif sleep_amount > 9:
        risk_score += 1 # Oversleeping can also be an issue

    # Panic attacks (0-3 scoring points (more panic attacks = higher risk))
    risk_score += min(panic_attacks, 3) # capped at 3

    # Missed commitment (0-2 scoring points (more missed commitments = higher risk))
    risk_score += min(missed_commitments, 2) # capped at 2

    # Age (0-1 scoring points (younger and older age potentially higher risk))
    if age <= 24 or age >= 65:
        risk_score += 1

    # Risk leel based on total scored points
    if risk_score >= 8:
        return "Risk level is High"
    elif risk_score >= 5:
        return "Risk level is Moderate"
    else:
        return "Risk level is Low "


# Allows users to input patient data and recieve a risk assessment result whne the sript is ran directly
if __name__ == "__main__":

    # This gets inputs from the user, calls the 'assess_mental_health_risk' function, and then print the result
    print("Mental health Risk Assessment Tool")
    age = int(input("Enter patient's age: "))
    stress = int(input("Enter patient's stress level (1-10): "))
    mood = int(input("Enter patient's mood level (1-10): "))
    sleep_amount = int(input("Enter patuents average hours of sleep per night: "))
    panic_attacks = int(input("Enter number of panic attacks suffered per week: "))
    missed_commitments = int(input("Enter number of missed commitments per week: "))
    
    suicial_thoughts_input = input("Does the patient have suicidal thoughts? (yes/no): ").strip().lower()
    
    if suicial_thoughts_input not in ("yes", "no"):
        raise ValueError("Invalid input for suicidal thoughts. Please enter 'yes' or 'no'.")
    
    suicial_thoughts = suicial_thoughts_input.lower() == "yes"

    risk = assess_mental_health_risk(age, stress, mood, sleep_amount, panic_attacks, missed_commitments, suicial_thoughts)
    print("Patient's mental health risk assessment result: " + risk)
