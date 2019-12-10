import csv

with open('names.csv','r') as f:  #filehandling open file as f
    csv_f=csv.reader(f)            #convert file f in csv file object

    #next(csv_f) #skip the first list ['.....','......','.........']

    #for line in csv_f:
    #    print(line)
    #    print(line[0],line[1],line[2])  #we have to use index

    #writing a csv file
    with open('new_names.csv','w') as new_f:
        csv_write=csv.writer(new_f,delimiter='#')    #csv file object   !!  delimeter is used to seprate data in a row

        for line in csv_f:
            csv_write.writerow(line)                #object of csv file.method
