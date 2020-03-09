#python3

import csv
from datetime import datetime
import matplotlib.pyplot as plt


startDate = datetime.strptime('01/11/19', '%d/%m/%y').date()
endDate = datetime.today().date()


def retentionEmail():

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs.csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            thisdict[row[1]] = row[0]

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users.csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = row[2]

    days7 = []
    days14 = []
    days30 = []
    days60 = []
    days120 = []
    daysover = []


    for x in thisdict:
        try:
            lastaccess = datetime.strptime(thisdict[x], '%d/%m/%y, %H:%M')

        except:
            continue

        difference = today-lastaccess
        if difference.days <= 7:
            try:
                days7.append(userdict[x])
            except:
                if x == "-" or x == 'Guest user  ':
                    continue
                else:
                    days7.append(userdict[x])


        if difference.days >= 7 and difference.days < 14:
            days14.append(userdict[x])


        if difference.days >= 14 and difference.days < 30:
            days30.append(userdict[x])


        if difference.days >= 30 and difference.days < 60:
            days60.append(userdict[x])

        if difference.days >= 60 and difference.days < 120:
            days120.append(userdict[x])

        if difference.days >= 120:
            daysover.append(userdict[x])




    print("\n7 Days:\n")
    for i in days7:
        print(i)


    print("\n14 Days:\n")
    for i in days14:
        print(i)

    print("\n30 Days:\n")
    for i in days30:
        print(i)

    print("\n60 Days:\n")
    for i in days60:
        print(i)

    print("\n120 Days:\n")
    for i in days120:
        print(i)

    print("\nOver 120 Days:\n")
    for i in daysover:
        print(i)


def userActivityHistogram():
    userdict = userActivity()
    listOfVisits = []

    for x in userdict:
        print(x)
        if x == "System Administrator":
            continue
        for y in userdict[x]:
            print(y)

        listOfVisits.append(len(userdict[x]))

    plt.hist(listOfVisits, bins = 50)
    plt.show()

def userActivityDau():
    userdict = userActivity()
    alldays = []
    alldayssign = []

    for x in userdict:
        print(x)
        iterusers = list(userdict[x])


        for y in iterusers:
            print(y)
            alldays.append(y)

        for y in iterusers[1:-1]:

            print(y)
            alldayssign.append(y)

    difference = (endDate - startDate).days
    plt.hist(alldays, bins = difference)
    plt.hist(alldayssign, bins = difference)
    plt.show()

def userActivityMau():
    userdict = userActivityMonth()
    alldays = []
    for x in userdict:
        print(x)
        for y in userdict[x]:
            print(y)
            alldays.append(y)

    #difference = int(((endDate - startDate).days)/30)
    plt.hist(alldays, bins = 12)
    plt.show()

def retention():
    userdict = userActivity()
    retentionList = []
    for x in userdict:
        if userdict[x] == set():
            continue
        a = sorted(list(userdict[x]))
        first = a[0]
        for i in a:
            difference = (i - first).days
            retentionList.append(difference)


    plt.hist(retentionList, bins = 50)
    plt.show()












def userActivity():

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users.csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs.csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            if row[1] != '-' and row[1] != "Guest user  ":
                unfilteredDate =datetime.strptime(row[0], '%d/%m/%y, %H:%M').date()
                if unfilteredDate >= startDate and unfilteredDate <= endDate:
                    filteredDate = unfilteredDate

                    userdict[row[1]].append(filteredDate)
    for x in userdict:
        if x == "System Administrator":
            userdict[x] = []
        #print(userdict[x])
        s = {d for d in userdict[x]}
        #print(x+": "+str(len(s)))
        userdict[x] = s
    return(userdict)


def userActivityMonth():

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users.csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs.csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            if row[1] != '-' and row[1] != "Guest user  ":
                unfilteredDate =datetime.strptime(row[0], '%d/%m/%y, %H:%M').date()
                if unfilteredDate >= startDate and unfilteredDate <= endDate:
                    filteredDate = unfilteredDate

                    userdict[row[1]].append(filteredDate)
    for x in userdict:
        if x == "System Administrator":
            userdict[x] = []
        #print(userdict[x])
        s = {d.month for d in userdict[x]}
        #print(x+": "+str(len(s)))
        userdict[x] = s
    return(userdict)




userActivityMau()
