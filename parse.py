#python3

from datetime import datetime
import matplotlib.pyplot as plt
import csv

import pandas as pd



from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from email.header import Header
from email.utils import formataddr

from cohort import *




startDate = datetime.strptime('01/11/19', '%d/%m/%y')
endDate = datetime.today()


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

    count = 0
    userCount = 0
    for x in userdict:
        print(x)
        iterusers = list(userdict[x])
        countList = []
        tempcount = 0
        for y in iterusers:
            tempcount += 1
            alldays.append(y)
        if count >= 2:
            userCount += 1
            count += tempcount
            tempcount = 0
        else:
            tempcount = 0
        for y in iterusers[1:-1]:


            alldayssign.append(y)

    difference = (endDate - startDate).days
    print(str(count) + " " + str(userCount))
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
    numSignUps = len(userdict)
    retentionList = []
    for x in userdict:
        if userdict[x] == set():
            continue
        if userdict[x] == []:
            continue
        p
        a = sorted(list(userdict[x]))
        print(a)
        first = a[0]
        last = a[-1]
        difference = (last - first).days
        retentionList.append(difference)
    counter = 0
    percentageList = []
    percentageList2 = []
    while counter <= 100:
        tempcount = 0
        for day in retentionList:
            if day >= counter:
                #print("counter: "+ str(counter) + "//day: " + str(day) +"//tc: "+ str(tempcount))
                tempcount += 1

        #percentageList.insert(0,float(tempcount/numSignUps))
        percentageList.append(100*(tempcount/numSignUps))
        percentageList2.append(counter)
        counter += 1
    #print(percentageList)
    print(percentageList[0])
    print(percentageList[6])
    print(percentageList[29])

    plt.plot(percentageList2, percentageList)
    plt.ylim(0, 100)
    plt.show()

def cohort():
    df = pd.DataFrame(columns=["name", "date", "first", "last"])

    userdict = userActivity()

    for i in userdict:
        x = userdict[i]
        try:
            for j in x[0]:
                df = df.append({
             "name": i,
             "date":  j,
             "first": x[1],
             "last": x[2]
              }, ignore_index=True)
                    #print(df)
        except:
            print(i)


    df = df.sort_values(by=['date'])
    print("About to Analyze")
    analysis=cohort_analysisWeekly(input_df=df, ActivityDate='date', CustomerID='name')

    ## Generate retention heatmap
    print("Plotting")
    analysis.plot_retention()
    print("Done")

def cohortActive(flagSet):

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (3).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []



    #df = pd.DataFrame(columns=["date", "name", "activity", "action"])
    df = pd.read_csv('..\..\..\Downloads\logs (4).csv', skipinitialspace = True)
    df.columns = df.columns.str.replace(' ', '_')
    print(list(df))
    df['Time'] = pd.to_datetime(df['Time'])

    df2 = df.loc[:, ["Time", "User_full_name", "Event_context", "Event_name", "Description"]]
    #print(df2)
    df2 = df2.query('User_full_name != "System Administrator"')
    df2 = df2.query('User_full_name != "-"')
    df2 = df2.query('Event_context != "System"')
    df2 = df2.drop_duplicates(subset=None, keep='first', inplace=False)

    # Event_context other is when the old module name has been deleted and is no longer available. Not the best, but whatever.

    df2 = df2.query('Event_context != "Other"')
    df2 = df2[df2["Time"] < endDate]


    if flagSet == "uploads":
        finaldf = df2.query('Event_name == "A file has been uploaded." or Event_name == "An online text has been uploaded."')

    if flagSet == "complete":
        finaldf = df2.query('Event_name == "Course activity completion updated"')
    #print(uploads.to_string())


    finaldf = finaldf.sort_values(by=['Time'])
    print("About to Analyze")
    analysis=cohort_analysisWeekly(input_df=finaldf, ActivityDate='Time', CustomerID='User_full_name')

    ## Generate retention heatmap
    print("Plotting")
    analysis.plot_retention()
    print("Done")

def userActivityPull(flagSet, email):

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (3).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []



    #df = pd.DataFrame(columns=["date", "name", "activity", "action"])
    df = pd.read_csv('..\..\..\Downloads\logs (4).csv', skipinitialspace = True)
    df.columns = df.columns.str.replace(' ', '_')
    print(list(df))
    df['Time'] = pd.to_datetime(df['Time'])

    df2 = df.loc[:, ["Time", "User_full_name", "Event_context", "Event_name"]]
    #print(df2)
    df2 = df2.query('User_full_name =='+email)
    df2 = df2.query('Event_context != "System"')
    df2 = df2.drop_duplicates(subset=None, keep='first', inplace=False)

    # Event_context other is when the old module name has been deleted and is no longer available. Not the best, but whatever.

    df2 = df2.query('Event_context != "Other"')
    df2 = df2[df2["Time"] < endDate]


    if flagSet == "uploads":
        finaldf = df2.query('Event_name == "A file has been uploaded." or Event_name == "An online text has been uploaded."')

    elif flagSet == "complete":
        finaldf = df2.query('Event_name == "Course activity completion updated"')

    else:
        finaldf = df2
    #print(uploads.to_string())


    finaldf = finaldf.sort_values(by=['Time'])
    print(finaldf.to_string())

def userActivity():

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (3).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []
            #print(row[2])

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs (4).csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            if row[1] != '-' and row[1] != "Guest user  ":
                unfilteredDate =datetime.strptime(row[0], '%d/%m/%y, %H:%M')
                if unfilteredDate >= startDate and unfilteredDate <= endDate:
                    filteredDate = unfilteredDate

                    try:
                        userdict[row[1]].append(filteredDate)
                    except KeyError:
                       print("ERROR:" + row[1])
    for x in userdict:
        if x == "System Administrator":
            userdict[x] = []
        #print(userdict[x])
        s = {d for d in userdict[x]}

        #print(x+": "+str(len(s)))
        if s == set():
            continue
        a = sorted(list(s))
        first = a[0]
        last = a[-1]
        difference = (last - first).days

        userdict[x] = (s,first,last,difference)


    return(userdict)


def userActivityMonth():

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (3).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs (4).csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            if row[1] != '-' and row[1] != "Guest user  ":
                unfilteredDate =datetime.strptime(row[0], '%d/%m/%y, %H:%M').date()
                if unfilteredDate >= startDate and unfilteredDate <= endDate:
                    filteredDate = unfilteredDate

                    try:
                        userdict[row[1]].append(filteredDate)
                    except:
                        print(row[1])
    for x in userdict:
        if x == "System Administrator":
            userdict[x] = []
        #print(userdict[x])
        s = {d.month for d in userdict[x]}
        #print(x+": "+str(len(s)))
        userdict[x] = s
    return(userdict)

def byActivity(flagSet, minSize):

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (3).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []



    #df = pd.DataFrame(columns=["date", "name", "activity", "action"])
    df = pd.read_csv('..\..\..\Downloads\logs (4).csv', skipinitialspace = True)
    df.columns = df.columns.str.replace(' ', '_')
    print(list(df))

    df2 = df.loc[:, ["Time", "User_full_name", "Event_context", "Event_name"]]
    #print(df2)
    df2 = df2.drop_duplicates(subset=None, keep='first', inplace=False)
    df2 = df2.query('User_full_name != "System Administrator"')
    df2 = df2.query('User_full_name != "-"')
    df2 = df2.query('Event_context != "System"')
    # Event_context other is when the old module name has been deleted and is no longer available. Not the best, but whatever.

    df2 = df2.query('Event_context != "Other"')

    # to only show Guests uncover this line
    if flagSet == "guestFlag":
        df2 = df2.query('User_full_name == "Guest user  "')
    # This filters out all the feedback stuff. Don't provide any value to our analytics
    # it is a bit sneaky, we are inversing the operation with the tilde
        df2 = df2[~df2["Event_context"].str.contains('Feedback:', regex=False)]#.str.contains("Feedback:", na=False)]


    if flagSet == "uploadsFlag":

        uploads = df2.query('Event_name == "A file has been uploaded." or Event_name == "An online text has been uploaded."')
        uploads = uploads.groupby(['Event_context']).size()
        uploads = uploads.to_frame(name = 'Size').reset_index()
        uploads = uploads.sort_values(["Size"])

    if flagSet == "viewsFlag":
        counter = df2.groupby(['Event_context', 'Event_name']).size()
        counter = counter.to_frame(name = 'Size').reset_index()
        counter = counter.sort_values(["Size"])
        counter = counter.query('Size >='+str(minSize))
        views = counter.query('Event_name == "Course module viewed"')
        finaldf = views

    if flagSet == "completeFlag":
        counter = df2.groupby(['Event_context', 'Event_name']).size()
        counter = counter.to_frame(name = 'Size').reset_index()
        counter = counter.sort_values(["Size"])
        counter = counter.query('Size >='+str(minSize))
        completed = counter.query('Event_name == "Course activity completion updated"')
        finaldf = completed

    #print(completed.to_string())
    finaldf.plot.bar(x='Event_context', y='Size', rot=90)
    plt.gca().invert_xaxis()
    plt.show()


#byActivity("completeFlag", 50)

cohortActive("complete")
#cohort()

#userActivityPull("complete", "'Timo Niere'")
