from calendar import *

year = int(input('Select year: '))
print(calendar(year, 2, 1, 8, 2))

# 2 = 2 characters for days (Mo, Tu, etc)
# 1 = 1 row for each week
# 8 = 8 rows for each month
# 2 = 2 columns for each month