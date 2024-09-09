"""
Just use lists comprehensions honestly
"""

from data.play_data import get_list_of_floats

float_list_50 = get_list_of_floats(50)

trunc_digits = map(lambda x: float(f"{x:.2f}"), float_list_50)

list_comp_version = [float(f"{i:.2f}") for i in float_list_50]
compare_list = zip(float_list_50, trunc_digits, list_comp_version)

for raw, truncated, list_comp in compare_list:
    print(truncated, list_comp, raw)
