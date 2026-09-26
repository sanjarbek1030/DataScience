"""
******
STRING
******
"""

single_quoted_string='data science'
double_quoted_string="data science"

tab_string = "\t" # represents the tab character
#print(len(tab_string)) # is 1

not_tab_sting = r"\t" # represents the characters '\' and 't'
#print(len(not_tab_sting)) # is 2

multi_line_sting = """This is the first line.
and this is the second line
and this is the third line"""

first_name = "Joel"
last_name = "Grus"

full_name1 = first_name + " " + last_name # string addition
full_name2 = "{0} {1}".format(first_name, last_name) # string.format
full_name3 = f"{first_name} {last_name}"

print(full_name1)
print(full_name2)
print(full_name3)
