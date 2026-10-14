import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from task_1 import gen_report, scoring, pts2lvl
from random import randint

n : int = 1000
counter = {}

for i in range(n):
    score, skips = randint(0, 100), randint(0, 5)
    wtype = ('PASS', 'exam', 'project', 'practice')[randint(0, 3)]
    print(gen_report(score, wtype, skips))
    lvl = scoring(pts2lvl(score, skips))
    counter[lvl] = counter.get(lvl, 0) + 1

print('\nSTAT')
for key, val in sorted(counter.items(), key=lambda x: x[0]):
    print(f"{key}: {val} students")