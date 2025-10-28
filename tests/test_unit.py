import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from module import Module
from unit import Unit

def test_unit_creation():
    """Test basic unit creation"""
    unit = Unit("UTEST", "Test Unit")
    assert unit.name == "UTEST"
    assert unit.title == "Test Unit"
    print("✓ Unit creation test passed")

def test_unit_add_module():
    """Test adding modules to unit"""
    unit = Unit("UTEST", "Test Unit")
    module = Module("TEST", "Test Module")
    unit.add_module(module)
    assert len(unit._modules) == 1
    print("✓ Unit add module test passed")

def test_unit_average():
    """Test unit average calculation"""
    unit = Unit("UTEST", "Test Unit")
    module1 = Module("TEST1", "Test Module 1", coef=2)
    module2 = Module("TEST2", "Test Module 2", coef=3)
    
    module1.set_grade(exam=12)
    module2.set_grade(exam=14)
    
    unit.add_module(module1)
    unit.add_module(module2)
    
    average = unit.calculate_average()
    assert average > 0
    print("✓ Unit average calculation test passed")

if __name__ == "__main__":
    test_unit_creation()
    test_unit_add_module()
    test_unit_average()
    print("All unit tests passed! ")