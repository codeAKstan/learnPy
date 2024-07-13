import math
from utilities import number_utils
# using standard module
print(f"standard: {math.factorial(3)}")

# using my defined module and package
print(f"defined: {number_utils.fact(3)}")