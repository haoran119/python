import re

filename = 'test.log'
pattern = re.compile('FinishedMessage from (?P<truck>.*):.*d=(?P<dump>.*)')
dumps = {}

with open( filename, 'r' ) as f:
    for line in f:
        print(line)

        match = re.search(pattern, line)
        print(match)

        if match:
            print(match.group(0))
            print(match.group(1))
            print(match.group(2))
            print(match.groupdict())
            print(match.groupdict()['truck'])
            print(match.groupdict()['dump'])

            dump = match.groupdict()['dump']

            if dump not in dumps:
                dumps[ dump ] = [ match.groupdict()['truck'] ]
            else:
                dumps[ dump ].append(match.groupdict()['truck'])
        print()

import pprint
pprint.pprint(dumps, width=1)

# =============================================================================
# [1] FinishedMessage from t1: group=[1] d=D1
#
# <re.Match object; span=(4, 43), match='FinishedMessage from t1: group=[1] d=D1'>
# FinishedMessage from t1: group=[1] d=D1
# t1
# D1
# {'truck': 't1', 'dump': 'D1'}
# t1
# D1
#
# [2] FinishedMessage from t2: group=[2] d=D2
#
# <re.Match object; span=(4, 43), match='FinishedMessage from t2: group=[2] d=D2'>
# FinishedMessage from t2: group=[2] d=D2
# t2
# D2
# {'truck': 't2', 'dump': 'D2'}
# t2
# D2
#
# [3] FinishedMessage from t3: group=[3] d=D2
# <re.Match object; span=(4, 43), match='FinishedMessage from t3: group=[3] d=D2'>
# FinishedMessage from t3: group=[3] d=D2
# t3
# D2
# {'truck': 't3', 'dump': 'D2'}
# t3
# D2
#
# {'D1': ['t1'],
#  'D2': ['t2',
#         't3']}
# =============================================================================
