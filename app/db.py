from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models.base import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()






# Iterative Solution
def get_missing_numbers_in_range(numbers, low, high):
    missing_numbers = []
    
    for num in range(low, high):
        if not num in numbers:
            missing_numbers.append(num)
    return missing_numbers

# hash table solution
def get_missing_numbers_in_range(array, low, high):
    map = {}

    for num in array:
        map[num] = True

    missing_nums = []
    for i in range(low, high):
        if i not in map:
            missing_nums.append(i)

    return missing_nums
    