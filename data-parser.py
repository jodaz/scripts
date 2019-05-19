import re

fhand = open('data-deleted')
fout = open('data-deleted.txt', 'w')

pattern = re.compile(r'(^removed\s\'\w+\/\w+\/\w+)(\/.*)(\.doc|\.pdf|\.mp4|\.html)(\')$')

previous = None
for line in open('data-deleted', encoding='utf-8'):
    mo = pattern.search(line)

    if mo:
        fout.write('.' + mo.group(2) + mo.group(3) + '\n')

