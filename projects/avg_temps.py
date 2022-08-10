def main():
	numDays = int(input('How many days? '))
	print(f'Calculate temperatures for {numDays} days')
	temps = []

	for i in range(numDays):
		days_temp = int(input(f"Day {i+1}'s high temperature: "))
		temps.append(days_temp)

	total = sum(temps)
	avg =  round(total/numDays,2)
	print(f'Avg temp is {avg}')

	above_avg = list(filter(lambda t: t > avg, temps))
	print(f'Days above avg temp {len(above_avg)}')

main()