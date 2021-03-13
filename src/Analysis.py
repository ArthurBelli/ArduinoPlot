import serial
import time

class Analysis:
    def __init__(self, port, baud):
         self.__ser = serial.Serial(port, baud)
         print(f'Connected to arduino port {port}')

    def collect_data(self, samples):
        line = 0
        raw_data = []
        while (line < samples):
        #collects
            get_data = str(self.__ser.readline())

            #cleans
            data = get_data.split(',')
            time = str(int(data[0].split("b'")[1])/1000)
            value = data[1].split("\\")[0] + '\n'
            raw_data.append(time + ',' + value)

            line += 1
            print(f"Sample {line}/{samples} collected")
        print("Data collection complete!")
        return raw_data

    def clean_data(self, raw_data):
        starting_point = 0 #keeps the number of the line + 1 that starts the valid data
        for i in range(0, len(raw_data)):
            if (raw_data[i].startswith('0.0')):
                starting_point = i 
            #will exit de loop having the last index that starts with '0.0' which is our initial value for time

        size = len(raw_data)
        valid_data = []
        for k in range(starting_point, size): #will get only the data that comes after the starting point
            valid_data.append(raw_data[k])
        return valid_data

    def write_file(self, file_name, valid_data, first_label, second_label):

        file = open(file_name, 'w')
        label = first_label + ',' + second_label + '\n'
        file.write(label)
        for entry in valid_data:
            file.write(entry)
        file.close()

    @property
    def ser(self):
        return self.__ser