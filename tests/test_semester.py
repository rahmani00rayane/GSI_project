import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from module import Module
from unit import Unit
from semester import Semester

def test_semester_creation():
    """Test basic semester creation"""
    semester = Semester("S1", "Semester 1")
    assert semester.name == "S1"
    assert semester.title == "Semester 1"
    print("✓ Semester creation test passed")

def test_semester_add_unit():
    """Test adding units to semester"""
    semester = Semester("S1", "Semester 1")
    unit = Unit("UTEST", "Test Unit")
    semester.add_unit(unit)
    assert len(semester._units) == 1
    print("✓ Semester add unit test passed")

def test_semester_average():
    """Test semester average calculation"""
    semester = Semester("S1", "Semester 1")
    unit = Unit("UTEST", "Test Unit")
    module = Module("TEST", "Test Module", coef=2, hours_tp=1.5)
    
    module.set_grade(tp=15, exam=15)
    unit.add_module(module)
    semester.add_unit(unit)
    
    average = semester.calculate_average()
    assert average > 0
    print("✓ Semester average calculation test passed")

def test_semester_credits():
    """Test semester credits calculation"""
    semester = Semester("S1", "Semester 1")
    unit = Unit("UTEST", "Test Unit")
    module = Module("TEST", "Test Module", coef=2, credit=3, hours_tp=1.5)
    
    module.set_grade(tp=15, exam=15)  # Good grade
    unit.add_module(module)
    semester.add_unit(unit)
    
    credits = semester.calculate_credits()
    assert credits == 3  # Should get credits
    print("✓ Semester credits calculation test passed")

if __name__ == "__main__":
    test_semester_creation()
    test_semester_add_unit()
    test_semester_average()
    test_semester_credits()
    print("All semester tests passed! ")