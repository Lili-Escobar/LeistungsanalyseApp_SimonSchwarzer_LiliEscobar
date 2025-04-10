class Person:
   def __init__(self, first_name, last_name):
      self.first_name
      self.last_name
   
class Subject(Person):
  def __init__(self, first_name, last_name, sex, birth_date):
      super().__init__(first_name, last_name)
      self.sex = sex
      self.__birth_date = birth_date  # private attribute

  def estimate_max_hr(age_years : int , sex : str) -> int:
    """
    See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
    """
    if sex == "male":
      max_hr_bpm =  223 - 0.9 * age_years
    elif sex == "female":
      max_hr_bpm = 226 - 1.0 *  age_years
    else:
      # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
      max_hr_bpm  = input("Enter maximum heart rate:")
    return int(max_hr_bpm)

class Supervisor(Person):
    def __init__(self, first_name, last_name):
      super().__init__(first_name, last_name) 


class Experiment(Person):
    def __init__(self, first_name, last_name, date):
      super().__init__(first_name, last_name)

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      pass