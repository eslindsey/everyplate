import os
import re

filename  = 'units.md'
markdown  = re.compile(r'\W')

spicedir  = 'spices'
spicename = re.compile(r"^title: '?(.+)'?$", re.MULTILINE)
spices    = {}
for fn in [f'_{spicedir}/{fn}' for fn in os.listdir(f'_{spicedir}')]:
    with open(fn, 'r') as f:
        m = spicename.search(f.read())
        if m == None:
            continue
        spices[m.group(1)] = fn[1:-3]

with open(filename + '.new', 'w') as outfile:
  with open(filename, 'r') as infile:
  
      # Beginning of file
      for line in infile:
          print(line.rstrip('\n\r'), file=outfile)
          if line[:3] == '|:-':
              break
  
      # Sort and link
      table = []
      for line in infile:
          if line[:2] != '| ':
              table.sort(key=lambda row: markdown.sub('', row[0]))
              for row in table:
                  print('| ', end='', file=outfile)
                  print(*row, sep=' | ', end=' |\n', file=outfile)
              print(line.rstrip('\n\r'), file=outfile)
              break
          row = [col.strip() for col in line.strip('\n\r\t| ').split(' | ') if col.strip() != '']
          if row[0] in spices:
              row[0] = '[' + row[0] + '](' + spices[row[0]] + ')'
          table.append(row)
  
      # End of file
      for line in infile:
          print(line.rstrip('\n\r'), file=outfile)

os.remove(filename)
os.rename(filename + '.new', filename)
