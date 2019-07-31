distance = int(input('How far is your trip? '))

if distance <= 200:
    print(f'The cost for this trip is ${0.5 * distance}')
else:
    print(f'The cost for this trip is ${0.45 * distance}')
