speed = int(input('What is your speed? '))
traffic_ticket = (speed - 80) * 7

if speed > 80:
    print('You were fined! Speed greater than 80km/h.')
    print(f'The value of the traffic ticket is ${traffic_ticket :.2f}')
