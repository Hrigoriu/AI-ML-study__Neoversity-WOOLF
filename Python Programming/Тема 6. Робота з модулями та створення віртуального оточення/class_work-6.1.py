import sys
import os

print(sys.modules.keys())
#============================================

import sys
import os

print(sys.builtin_module_names)
#============================================
from calculations import salary_calculations

salary = 1000
bonus = 15
salary_with_bonus = salary_calculations.add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015

#============================================
