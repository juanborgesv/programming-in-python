#import sys

# Shows the location where modules can be found.
#locations = sys.path
#print(locations)

import calendar
calendar
leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

isitleap = calendar.isleap(2036)
print(isitleap)
