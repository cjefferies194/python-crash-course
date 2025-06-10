from pathlib import Path

path = Path('chapter-10-guest.txt')
contents = path.read_text().rstrip()
contents += input(f'ENTER NAME AND DATE, AND EMAIL HERE \n')
path.write_text(f' {contents}')
