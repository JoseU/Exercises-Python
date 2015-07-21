import re

# Sample strings.
pregunta =  input ("dime la dirección")

# Loop.
for element in pregunta:
    # Match if two words starting with letter d.
    m = re.match("izquierda", element)

    # See if success.
    if m:
        print(m.group(0))