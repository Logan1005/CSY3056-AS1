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
    with pytest.raises(ValueError):
        assess_mental_health_risk(-18, 2, 8, 8, 0, 0, False)

def test_invalid_age_too_high():
    with pytest.raises(ValueError):
        assess_mental_health_risk(115, 2, 9, 9, 0, 0, False)

def test_invalid_stress():
    with pytest.raises(ValueError):
        assess_mental_health_risk(25, 12, 8, 9, 0, 0, False)

def test_invalid_mood():
    with pytest.raises(ValueError):
        assess_mental_health_risk(25, 5, 14, 9, 0, 0, False)


