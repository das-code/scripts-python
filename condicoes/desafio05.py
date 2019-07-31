year = int(input('Enter the current year: '))

for_4 = year % 4 == 0
for_400 = year % 400 == 0
for_100 = year % 100 > 0

if for_4 or for_400 and for_100:
    print(f'The year {year} is leap year')
else:
    print(f"The year {year} isn't leap year")
