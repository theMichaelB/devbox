import random
import string

lines = []
for _ in range(20):
    line = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))
    line += ' ' * random.randint(1, 10)
    lines.append(line)

text = '\n'.join(lines)

with open('./test.txt', 'w') as file:
    file.write(text)
