import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)

    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatColor = input('What color do you wish to know the date of?')

        if whatColor in colors:

            coldex = colors.index(whatColor)
            theDate = dates[coldex]
            print('The date of ', whatColor, 'is: ', theDate)
        else:
            print('Color not found,or is not a ')

    #except Exception, e
    except Exception as e:
        print(e)

    print('continuing')
