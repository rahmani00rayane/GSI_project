from academicelement import AcademicElement

class Unit(AcademicElement):
    """Represents a teaching unit containing multiple modules."""

    def __init__(self, name, title, modules=None):
        super().__init__(name, title)
        self._modules = modules if modules is not None else []
        self.coef = 1

    def add_module(self, module):
        """Add a module to the unit."""
        self._modules.append(module)

    def calculate_average(self):
        """Calculate unit average from module averages."""
        if not self._modules:
            return 0
        total = sum(m.calculate_average() * m.coef for m in self._modules)
        coef_sum = sum(m.coef for m in self._modules)
        return total / coef_sum if coef_sum != 0 else 0

    def calculate_credits(self):
        """Calculate total credits for the unit."""
        if not self._modules:
            return 0
        return sum(m.calculate_credits() for m in self._modules)

    def display_modules(self):
        """Display all modules in this unit."""
        return [m.display_info() for m in self._modules]

    @classmethod
    def from_csv(cls, csv_data):
        """Create Unit instance from CSV data."""
        return cls(csv_data['code'], csv_data['title'])