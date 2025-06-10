from pathlib import Path

path = Path('chapter-10.txt')
contents = path.read_text().rstrip()

pi_string = ''
for line in contents.splitlines():
	pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

from pathlib import Path

path = Path('chapter-10-2.txt')
contents = path.read_text().rstrip().replace('Chapter 10:Files', '')
print(contents)

from pathlib import Path

path = Path('chapter-10-guest.txt')
contents = path.read_text().rstrip()
contents += input(f'ENTER NAME AND DATE, AND EMAIL HERE \n')
path.write_text(f' {contents}')
