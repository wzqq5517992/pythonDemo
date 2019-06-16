import csv

csv_file = csv.reader(open('jolin.csv',"r", encoding="UTF-8"))
count = 0
for line in csv_file:
    print(line[0])
    if count >= 17:
        print(line[0])
        # 所有的详细信息

    count += 1
