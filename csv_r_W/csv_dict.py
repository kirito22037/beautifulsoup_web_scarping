import csv

#it is a way of showing csv data in a dictionary format and nothing more
with open('new_names.csv','r') as f:
    csv_f=csv.DictReader(f,delimiter='#')  #DictReader read every row an listelement of dict

    #for line in csv_f:
       #print(line['first_name'],line['last_name'],line['email'])   #here we can use keywords
       #print(line)

    #now to write a csv but coding it as dictionary
    with open('new_dict_names.csv','w') as fw:
        fieldnames=['first_name','last_name','email']    #same as the 1st line of csv file
        wcsv_f=csv.DictWriter(fw,fieldnames=fieldnames,delimiter='\t')
        wcsv_f.writeheader()
        for line in csv_f:
            wcsv_f.writerow(line)
