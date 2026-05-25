from src.component import assess_mental_health_risk
import pytest


def test_low_risk():
    result = assess_mental_health_risk(20, 3, 8, 9, 0, 0, False)
    assert result == "Risk level is Low "

def test_moderate_rsik():
    result = assess_mental_health_risk(20, 4, 5, 5, 1, 1, False)
    assert result == "Risk level is Moderate"

def test_high_risk():
    result = assess_mental_health_risk(18, 9, 2, 3, 3, 2, False)
    assert result == "Risk level is High"

def test_critital_risk():
    result = assess_mental_health_risk(30, 5, 3, 6, 2, 1, True)
    assert result == "Risk level is Critical"

def test_crital_risk_low_risk_factors():
    result = assess_mental_health_risk(40, 2, 9, 8, 0, 0, True)
    assert result == "Risk level is Critical"

def test_invalid_age_negative():
    with pytest.raises(ValueError, match="Age must be between 0 and 100."):
        assess_mental_health_risk(-18, 2, 8, 8, 0, 0, False)

def test_invalid_age_too_high():
    with pytest.raises(ValueError, match="Age must be between 0 and 100."):
        assess_mental_health_risk(115, 2, 9, 9, 0, 0, False)

def test_invalid_stress():
    with pytest.raises(ValueError, match="Stress level must be between 1 and 10."):
        assess_mental_health_risk(25, 12, 8, 9, 0, 0, False)

def test_invalid_mood():
    with pytest.raises(ValueError, match="Mood level must be between 1 and 10."):
        assess_mental_health_risk(25, 5, 14, 9, 0, 0, False)

def test_invalid_sleep_high():
    with pytest.raises(ValueError, match="Sleep amount must be between 0 and 24."):
        assess_mental_health_risk(25, 3, 9, 27, 0, 0, False)

def test_invalid_sleep_negative():
    with pytest.raises(ValueError, match="Sleep amount must be between 0 and 24."):
        assess_mental_health_risk(14, 7, 2, -5, 0, 0, False)

def test_negative_panic_attacks():
    with pytest.raises(ValueError, match="Number of panic attacks cannot be negative."):
        assess_mental_health_risk(25, 5, 8, 7, -1, 0, False)

def test_negative_missed_commitments():
    with pytest.raises(ValueError, match="Number of missed commitments cannot be negative."):
        assess_mental_health_risk(25, 5, 8, 7, 0, -2, False)

def test_invalid_suicidal_thoughts():
    with pytest.raises(ValueError, match="Suicidal thoughts must be True/False."):
        assess_mental_health_risk(25, 5, 8, 7, 0, 0, "Yes")

def test_panic_attacks_capped():
    a = assess_mental_health_risk(25, 5, 8, 7, 5, 0, False) # More than 3 panic attacks should be capped at 3
    b = assess_mental_health_risk(25, 5, 8, 7, 3, 0, False) # 3 panic attacks
    assert a == b

def test_capped_missed_commitments():
    a = assess_mental_health_risk(25, 5, 8, 7, 0, 9, False) # More than 5 missed commitments should be capped at 5
    b = assess_mental_health_risk(25, 5, 8, 7, 0, 5, False) # 5 missed commitments
    assert a == b

# Very specific test to ensure oversleeping adds a point to risk socre, can only test this when the added point will chanege the risk level outcome (Low to Moderate)
def test_oversleep_adds_point():
    a = assess_mental_health_risk(25, 8, 6, 10, 0, 0, False) # Oversleeping should add 1 point
    b = assess_mental_health_risk(25, 8, 6, 9, 0, 0, False) # Normal sleep should not add points
    assert a != b


# The test below are designed to fail, to ensure failures are decteted and reported
"""
def test_fail_low_risk():
    result = assess_mental_health_risk(14, 8, 4, 5, 2, 1, False)
    assert result == "Risk level is Low"

def test_fail_moderate_risk():
    result = assess_mental_health_risk(24, 3, 7, 9, 0, 0, False)
    assert result == "Risk level is Moderate"

def test_fail_high_risk():
    result = assess_mental_health_risk(24, 3, 7, 9, 0, 0, True)
    assert result == "Risk level is High"

def test_fail_critical_risk():
    result = assess_mental_health_risk(24, 3, 7, 9, 0, 0, False)
    assert result == "Risk level is Critical"
 
"""