from module import Module
from unit import Unit
from semester import Semester
import csv
import os

class GSIAcademicManager:
    """Main class to manage the GSI academic structure."""
    
    def __init__(self):
        self.modules = {}
        self.units = {}
        self.semesters = {}
    
    def load_from_csv(self, csv_file):
        """Load academic data from CSV file and organize it properly."""
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                
                # First pass: Create all elements
                for row in csv_reader:
                    element_type = row.get('type', '').lower()
                    
                    if element_type == 'module':
                        module = Module.from_csv(row)
                        self.modules[module.name] = module
                    
                    elif element_type == 'unit':
                        unit = Unit.from_csv(row)
                        self.units[unit.name] = unit
                    
                    elif element_type == 'semester':
                        semester = Semester.from_csv(row)
                        self.semesters[semester.name] = semester
            
            # Second pass: Organize the hierarchy based on GSI curriculum
            self.organize_gsi_curriculum()
            
            # Set default grades for all modules
            self.set_default_grades()
            
            print(f"✓ Successfully loaded data from {csv_file}")
            return True
                        
        except FileNotFoundError:
            print(f"✗ CSV file {csv_file} not found.")
            return False
    
    def organize_gsi_curriculum(self):
        """Organize modules into units and units into semesters based on GSI curriculum."""
        # Organize Semester 1 modules into their respective units
        if 'UEF11' in self.units:
            self.units['UEF11'].add_module(self.modules['F111'])
            self.units['UEF11'].add_module(self.modules['F112'])
        
        if 'UEF12' in self.units:
            self.units['UEF12'].add_module(self.modules['F121'])
            self.units['UEF12'].add_module(self.modules['F122'])
        
        if 'UEM11' in self.units:
            self.units['UEM11'].add_module(self.modules['M111'])
            self.units['UEM11'].add_module(self.modules['M112'])
        
        if 'UED11' in self.units:
            self.units['UED11'].add_module(self.modules['D111'])
        
        if 'UET11' in self.units:
            self.units['UET11'].add_module(self.modules['T111'])
        
        # Organize units into Semester 1
        if 'S1' in self.semesters:
            semester1 = self.semesters['S1']
            for unit_code in ['UEF11', 'UEF12', 'UEM11', 'UED11', 'UET11']:
                if unit_code in self.units:
                    semester1.add_unit(self.units[unit_code])
    
    def set_default_grades(self):
        """Set realistic default grades for all modules."""
        grade_ranges = {
            'F111': (12, 14),  # Réseaux des couches basses
            'F112': (14, 16),  # Algorithmique Avancée
            'F121': (13, 15),  # Système d'exploitation
            'F122': (11, 13),  # Architectures Modernes
            'M111': (15, 17),  # Architecture BD
            'M112': (16, 18),  # Méthodes et Technologies
            'D111': (12, 14),  # Communication Vocaux
            'T111': (14, 16)   # Cloud Computing
        }
        
        for module_code, (min_grade, max_grade) in grade_ranges.items():
            if module_code in self.modules:
                module = self.modules[module_code]
                # Set grades based on module type
                if module.hours_tp > 0:
                    module.set_grade(tp=(min_grade + max_grade) / 2)
                if module.hours_td > 0:
                    module.set_grade(td=(min_grade + max_grade) / 2)
                module.set_grade(exam=(min_grade + max_grade) / 2)
    
    def display_academic_structure(self):
        """Display the complete academic structure."""
        print("\n" + "=" * 60)
        print("GSI ACADEMIC STRUCTURE - SEMESTER 1")
        print("=" * 60)
        
        total_semester_credits = 0
        
        for sem_name, semester in self.semesters.items():
            print(f"\n{semester.title} ({sem_name}):")
            print(f"  Semester Average: {semester.calculate_average():.2f}/20")
            sem_credits = semester.calculate_credits()
            print(f"  Semester Credits: {sem_credits}/27")
            total_semester_credits = sem_credits
            
            for unit in semester._units:
                print(f"\n    {unit.title} ({unit.name}):")
                print(f"      Unit Average: {unit.calculate_average():.2f}/20")
                print(f"      Unit Credits: {unit.calculate_credits()}")
                
                for module in unit._modules:
                    module_avg = module.calculate_average()
                    module_credits = module.calculate_credits()
                    status = "✓ PASS" if module_avg >= 10 else "✗ FAIL"
                    print(f"        - {module.title}: {module_avg:.2f}/20 "
                          f"(Credits: {module_credits}) {status}")
        
        return total_semester_credits
    
    def calculate_student_results(self):
        """Calculate and display comprehensive student results."""
        print("\n" + "=" * 60)
        print("STUDENT ACADEMIC RESULTS SUMMARY")
        print("=" * 60)
        
        for semester in self.semesters.values():
            sem_avg = semester.calculate_average()
            sem_credits = semester.calculate_credits()
            
            print(f"\n{semester.title}:")
            print(f"  Average: {sem_avg:.2f}/20")
            print(f"  Credits Obtained: {sem_credits}/27")
            print(f"  Status: {'✓ PASS' if sem_avg >= 10 else '✗ FAIL'}")
            
            if sem_avg >= 10:
                print(f"  Result: Student has passed the semester")
            else:
                print(f"  Result: Student must repeat the semester")
        
        print(f"\nNOTE: Total credits for Semester 1 should be 27")
from module import Module
from unit import Unit
from semester import Semester
import csv
import os

class GSIAcademicManager:
    """Main class to manage the GSI academic structure."""
    
    def __init__(self):
        self.modules = {}
        self.units = {}
        self.semesters = {}
    
    def load_from_csv(self, csv_file):
        """Load academic data from CSV file and organize it properly."""
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                
                # First pass: Create all elements
                for row in csv_reader:
                    element_type = row.get('type', '').lower()
                    
                    if element_type == 'module':
                        module = Module.from_csv(row)
                        self.modules[module.name] = module
                    
                    elif element_type == 'unit':
                        unit = Unit.from_csv(row)
                        self.units[unit.name] = unit
                    
                    elif element_type == 'semester':
                        semester = Semester.from_csv(row)
                        self.semesters[semester.name] = semester
            
            # Second pass: Organize the hierarchy based on GSI curriculum
            self.organize_gsi_curriculum()
            
            # Set default grades for all modules
            self.set_default_grades()
            
            print(f"✓ Successfully loaded data from {csv_file}")
            return True
                        
        except FileNotFoundError:
            print(f"✗ CSV file {csv_file} not found.")
            return False
    
    def organize_gsi_curriculum(self):
        """Organize modules into units and units into semesters based on GSI curriculum."""
        # Organize Semester 1 modules into their respective units
        if 'UEF11' in self.units:
            self.units['UEF11'].add_module(self.modules['F111'])
            self.units['UEF11'].add_module(self.modules['F112'])
        
        if 'UEF12' in self.units:
            self.units['UEF12'].add_module(self.modules['F121'])
            self.units['UEF12'].add_module(self.modules['F122'])
        
        if 'UEM11' in self.units:
            self.units['UEM11'].add_module(self.modules['M111'])
            self.units['UEM11'].add_module(self.modules['M112'])
        
        if 'UED11' in self.units:
            self.units['UED11'].add_module(self.modules['D111'])
        
        if 'UET11' in self.units:
            self.units['UET11'].add_module(self.modules['T111'])
        
        # Organize units into Semester 1
        if 'S1' in self.semesters:
            semester1 = self.semesters['S1']
            for unit_code in ['UEF11', 'UEF12', 'UEM11', 'UED11', 'UET11']:
                if unit_code in self.units:
                    semester1.add_unit(self.units[unit_code])
    
    def set_default_grades(self):
        """Set realistic default grades for all modules."""
        grade_ranges = {
            'F111': (12, 14),  # Réseaux des couches basses
            'F112': (14, 16),  # Algorithmique Avancée
            'F121': (13, 15),  # Système d'exploitation
            'F122': (11, 13),  # Architectures Modernes
            'M111': (15, 17),  # Architecture BD
            'M112': (16, 18),  # Méthodes et Technologies
            'D111': (12, 14),  # Communication Vocaux
            'T111': (14, 16)   # Cloud Computing
        }
        
        for module_code, (min_grade, max_grade) in grade_ranges.items():
            if module_code in self.modules:
                module = self.modules[module_code]
                # Set grades based on module type
                if module.hours_tp > 0:
                    module.set_grade(tp=(min_grade + max_grade) / 2)
                if module.hours_td > 0:
                    module.set_grade(td=(min_grade + max_grade) / 2)
                module.set_grade(exam=(min_grade + max_grade) / 2)
    
    def display_academic_structure(self):
        """Display the complete academic structure."""
        print("\n" + "=" * 60)
        print("GSI ACADEMIC STRUCTURE - SEMESTER 1")
        print("=" * 60)
        
        total_semester_credits = 0
        
        for sem_name, semester in self.semesters.items():
            print(f"\n{semester.title} ({sem_name}):")
            print(f"  Semester Average: {semester.calculate_average():.2f}/20")
            sem_credits = semester.calculate_credits()
            print(f"  Semester Credits: {sem_credits}/27")
            total_semester_credits = sem_credits
            
            for unit in semester._units:
                print(f"\n    {unit.title} ({unit.name}):")
                print(f"      Unit Average: {unit.calculate_average():.2f}/20")
                print(f"      Unit Credits: {unit.calculate_credits()}")
                
                for module in unit._modules:
                    module_avg = module.calculate_average()
                    module_credits = module.calculate_credits()
                    status = "✓ PASS" if module_avg >= 10 else "✗ FAIL"
                    print(f"        - {module.title}: {module_avg:.2f}/20 "
                          f"(Credits: {module_credits}) {status}")
        
        return total_semester_credits
    
    def calculate_student_results(self):
        """Calculate and display comprehensive student results."""
        print("\n" + "=" * 60)
        print("STUDENT ACADEMIC RESULTS SUMMARY")
        print("=" * 60)
        
        for semester in self.semesters.values():
            sem_avg = semester.calculate_average()
            sem_credits = semester.calculate_credits()
            
            print(f"\n{semester.title}:")
            print(f"  Average: {sem_avg:.2f}/20")
            print(f"  Credits Obtained: {sem_credits}/27")
            print(f"  Status: {'✓ PASS' if sem_avg >= 10 else '✗ FAIL'}")
            
            if sem_avg >= 10:
                print(f"  Result: Student has passed the semester")
            else:
                print(f"  Result: Student must repeat the semester")
        
        print(f"\nNOTE: Total credits for Semester 1 should be 27")
       

def create_sample_csv():
    """Create a sample CSV file if it doesn't exist."""
    csv_content = """type,code,title,coef,credit,hours_lecture,hours_td,hours_tp,teaching_mode,continous_percent,exam_percent
module,F111,Réseaux des couches basses,3,6,1.5,1.5,1.5,In-person,40,60
module,F112,Algorithmique Avancée et Complexité,2,4,1.5,1.5,0,In-person,40,60
module,F121,Système d'exploitation,2,4,1.5,1.5,0,In-person,40,60
module,F122,Architectures Modernes des Systèmes Informatiques,2,4,1.5,1.5,0,In-person,40,60
module,M111,Architecture et administration des bases de données,2,4,1.5,1.5,0,In-person,40,60
module,M112,Méthodes et Technologies d'Implémentation,3,5,1.5,0,1.5,In-person,40,60
module,D111,Systèmes de Communication Vocaux et Vidéos,2,2,1.5,1.5,0,In-person,40,60
module,T111,Cloud Computing,1,1,1.5,0,0,In-person,100,0
unit,UEF11,UE Fondamentales 1,0,0,0,0,0,In-person,0,0
unit,UEF12,UE Fondamentales 2,0,0,0,0,0,In-person,0,0
unit,UEM11,UE Méthodologie,0,0,0,0,0,In-person,0,0
unit,UED11,UE Découverte,0,0,0,0,0,In-person,0,0
unit,UET11,UE Transversale,0,0,0,0,0,In-person,0,0
semester,S1,Semester 1,0,0,0,0,0,In-person,0,0"""
    
    with open("gsi_curriculum.csv", "w", encoding="utf-8") as f:
        f.write(csv_content)
    print("✓ Sample CSV file created: gsi_curriculum.csv")

def main():
    """Main function to run the GSI Academic Manager."""
    manager = GSIAcademicManager()
    
    # Create sample CSV file if it doesn't exist
    if not os.path.exists("gsi_curriculum.csv"):
        create_sample_csv()
    
    # Load from CSV
    csv_file = "gsi_curriculum.csv"
    if manager.load_from_csv(csv_file):
        # Display results
        manager.display_academic_structure()
        manager.calculate_student_results()
    else:
        print("Failed to load data. Please check the CSV file.")

if __name__ == "__main__":
    main()
def main():
    """Main function to run the GSI Academic Manager."""
    manager = GSIAcademicManager()
    
    # Create sample CSV file if it doesn't exist
    if not os.path.exists("gsi_curriculum.csv"):
        create_sample_csv()
    
    # Load from CSV
    csv_file = "gsi_curriculum.csv"
    if manager.load_from_csv(csv_file):
        # Display results
        manager.display_academic_structure()
        manager.calculate_student_results()
    else:
        print("Failed to load data. Please check the CSV file.")

if __name__ == "__main__":
    main()