import re

pattern = re.compile(r"([a-zA-Z0-9@#$%]){8,}\d")
password = "hell@#8t7"

a = re.fullmatch(pattern, password)
print(a)
