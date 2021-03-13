from Analysis import Analysis

'''
Initial setup
'''
arduino_port = '/dev/ttyACM0'
baud = 9600
file_name = 'samples.csv'
analysis = Analysis(arduino_port, baud)
second_label = input('What are we measuring this time? ')
first_label = input('And we are measuring it in function of what? ')
samples = int(input('How many samples do you want? '))

#data collection and first cleaning
raw_data = analysis.collect_data(samples)

'''
Since I yet can't synchronize the time == 0 of the arduino with the beggining of this program,
we'll have to exclude all data that comes before it

Maybe there is some way to discard the serial buffer, got to check it
'''
valid_data = analysis.clean_data(raw_data)

#now write the file with de correct data
analysis.write_file(file_name, valid_data, first_label, second_label)
print(f'Valid measures: {100*len(valid_data)/len(raw_data)}%')

