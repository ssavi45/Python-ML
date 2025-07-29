temp = float(input('Enter temperature: '))
temp_unit = input('Enter unit(C/F): ').lower()

if temp_unit == 'c':
    temp = (temp * 9/5) + 32
    print(f'{temp} farenhite')

elif temp_unit == 'f':
    temp = (temp - 32) * 5/9
    print(f'{temp} celcius')

else:
    print('Please enter a valid Temp/ Unit')