from datetime import datetime
import json
import random
import sys

import stats


data_filename = sys.argv[1]
with open(data_filename, 'r') as f:
    data = json.load(f)

print 'The pot is currently at $%d.' % stats.current_pot(data)
name_input = raw_input('Who is playing? Comma separated list of names: ')
names = [name.strip() for name in name_input.split(',') if name.strip() != '']

print
print 'There are %d players: %s' % (len(names), ', '.join(sorted(names)))
print 'The pot is now $%d.' % (stats.current_pot(data) + len(names))
raw_input('Press enter to start. ')
print
print "'y' for a hit, 'n' for a miss, 's' to skip someone no longer playing, 'w' to wait"

random.shuffle(names)

results = {}

while names:
    name = names.pop()

    result = raw_input('[%d] %s: ' % (len(results) + 1, name))
    result = result.lower()

    if result in ('y', 'yes'):
        results[name] = True

    elif result in ('n', 'no'):
        results[name] = False

    elif result in ('w', 'wait'):
        names.insert(0, name)

    elif result in ('s', 'skip'):
        continue

    else:
        print 'Unrecognized'
        names.append(name)

data.append({'date': str(datetime.now().date()), 'results': results})

with open(data_filename, 'w') as f:
    json.dump(data, f, indent=2)
print "Updated {0} with these results.".format(data_filename)
