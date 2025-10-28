import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from module import Module

def test_module_creation():
    """Test basic module creation"""
    module = Module("TEST", "Test Module", coef=2, credit=3)
    assert module.name == "TEST"
    assert module.title == "Test Module"
    assert module.coef == 2
    assert module.credit == 3
    print("✓ Module creation test passed")

def test_module_average():
    """Test module average calculation"""
    module = Module("TEST", "Test Module", coef=2, credit=3, hours_tp=1.5)
    module.set_grade(tp=16, exam=14)
    average = module.calculate_average()
    assert average > 0
    print("✓ Module average calculation test passed")

def test_module_credits():
    """Test module credits calculation"""
    # FIX: Added hours_tp so continuous evaluation works
    module = Module("TEST", "Test Module", coef=2, credit=3, hours_tp=1.5)
    module.set_grade(tp=16, exam=14)  # Good grades
    credits = module.calculate_credits()
    assert credits == 3  # Should get full credits
    print("✓ Module credits calculation test passed")

def test_module_failing_credits():
    """Test module credits when failing"""
    module = Module("TEST", "Test Module", coef=2, credit=3, hours_tp=1.5)
    module.set_grade(tp=5, exam=5)  # Bad grades - should fail
    credits = module.calculate_credits()
    assert credits == 0  # Should get no credits
    print("✓ Module failing credits test passed")

if __name__ == "__main__":
    test_module_creation()
    test_module_average()
    test_module_credits()
    test_module_failing_credits()
    print("All module tests passed! ")