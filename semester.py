from academicelement import AcademicElement

class Semester(AcademicElement):
    """Represents an academic semester containing multiple units."""

    def __init__(self, name, title, units=None):
        super().__init__(name, title)
        self._units = units if units is not None else []
        self.coef = 1

    def add_unit(self, unit):
        """Add a unit to the semester."""
        self._units.append(unit)

    def calculate_average(self):
        """Calculate semester average from unit averages."""
        if not self._units:
            return 0
        total = sum(unit.calculate_average() * unit.coef for unit in self._units)
        coef_sum = sum(unit.coef for unit in self._units)
        return total / coef_sum if coef_sum != 0 else 0

    def calculate_credits(self):
        """Calculate total credits earned in the semester."""
        if not self._units:
            return 0
        return sum(unit.calculate_credits() for unit in self._units)

    def display_units(self):
        """Display all units in this semester."""
        return [unit.display_info() for unit in self._units]

    @classmethod
    def from_csv(cls, csv_data):
        """Create Semester instance from CSV data."""
        return cls(csv_data['code'], csv_data['title'])