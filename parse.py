#python3

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

import csv

import pandas as pd



from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from email.header import Header
from email.utils import formataddr

from cohort import *




startDate = datetime.strptime('01/01/20', '%d/%m/%y')
endDate = datetime.today()


def cohort(flagSet, periodFlag, countFlag):

    df = getActivity(flagSet)

    finaldf = df.sort_values(by=['Time'])
    print("About to Analyze")
    analysis=cohort_analysisWeekly(input_df=finaldf, ActivityDate='Time', CustomerID='User_full_name', countFlag=countFlag, periodFlag=periodFlag)
    #print(finaldf.to_string())
    ## Generate retention heatmap
    print("Plotting")
    analysis.plot_retention()
    print("Done")


def cohortActive(flagSet):

    df = getActivity(flagSet)
    finaldf = byActivity(df, "completeFlag")
    print(finaldf)

    finaldf = finaldf.sort_values(by=['Time'])
    print("About to Analyze")
    analysis=cohort_analysisWeekly(input_df=finaldf, ActivityDate='Time', CustomerID='User_full_name')

    ## Generate retention heatmap
    print("Plotting")
    analysis.plot_retention()
    print("Done")

def userActivityPull(flagSet, email):

    df2 = getActivity(flagSet)
    df2 = df2.query('Email =='+email)
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
    return(finaldf)

def activityByWeek(flagSet):
    df2 = getActivity(flagSet)
    df2 = byActivity(df2, flagSet)
    df2['Time'] = df2['Time'].dt.strftime('%Y-%U')

    df2 = df2.loc[:, ["Time", "User_full_name",]]

    counter = df2.drop_duplicates(subset=None, keep='first', inplace=False)

    counter = counter.groupby(['Time']).size()

    counter = counter.to_frame(name = 'Size').reset_index()

    #counter = counter.sort_values(["Size"])
    print(counter)
    total = counter['Size'].sum()
    print(total)
    counter.plot(x='Time', y='Size', rot=90)
    plt.gca().set_ylabel('Number')
    plt.gca().set_xlabel('Week')
    plt.gca().set_title('Assignments Completed Per Week')
    #plt.gca().invert_xaxis()
    plt.show()
    return(counter)

def activityByDay(flagSet):
    df2 = getActivity(flagSet)
    df2 = byActivity(df2, flagSet)
    #df2 = byActivity(df2, flagSetAction)
    df2['Time'] = df2['Time'].dt.strftime('%Y-%m-%d')

    df2 = df2.loc[:, ["Time", "User_full_name",]]

    counter = df2.drop_duplicates(subset=None, keep='first', inplace=False)
    counter = counter.groupby(['Time']).size()

    counter = counter.to_frame(name = 'Size').reset_index()
    #counter = counter.sort_values(["Size"])
    print(counter)
    total = counter['Size'].sum()
    print(total)

    FMT = '%Y-%m-%d' #2019-04-08
    counter['Time'] = counter['Time'].map(lambda x: datetime.strptime(str(x), FMT))
    #counter['Time'] = counter['Time'].map(lambda x: x.replace(day=date, month=month, year=year))

    ax = counter.plot(x='Time', y='Size', rot=90, kind='bar')
    ax.set_xlabel('x label name')
#plt.xticks(np.arange(start, end+1, 15.0))
    #ax = plt.axes()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    #ax.xaxis.set_minor_locator(mdates.DayLocator(interval=30))
    ax.xaxis.set_major_locator(mdates.MonthLocator())

    #ax.tick_params(axis='both', which='major', labelsize=5) #labelsize=5 instead of labelsize=10


    #plt.gcf().autofmt_xdate()

    #plt.autofmt_xdate()

    #ax.grid(True)

    plt.show()
    return(counter)

def activityByMonth(flagSet):
    df2 = getActivity(flagSet)
    df2 = byActivity(df2, flagSet)
    df2['Time'] = df2['Time'].dt.strftime('%Y-%m')

    df2 = df2.loc[:, ["Time", "User_full_name",]]

    counter = df2.drop_duplicates(subset=None, keep='first', inplace=False)
    counter = counter.groupby(['Time']).size()

    counter = counter.to_frame(name = 'Size').reset_index()
    #counter = counter.sort_values(["Size"])
    print(counter)
    total = counter['Size'].sum()
    print(total)
    counter.plot(x='Time', y='Size', rot=90)
    plt.gca().set_ylabel('Number')
    plt.gca().set_xlabel('Week')
    plt.gca().set_title('Monthly Active Users')
    #plt.gca().invert_xaxis()
    plt.show()
    return(counter)

def getActivity(flagSet):
    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (3).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = row[2]
            #print(row)




    #df = pd.DataFrame(columns=["date", "name", "activity", "action"])
    df = pd.read_csv('..\..\..\Downloads\logs (4).csv', skipinitialspace = True)
    df.columns = df.columns.str.replace(' ', '_')
    df['Time'] = pd.to_datetime(df['Time'])
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
    else:
        df2 = df2.query('User_full_name != "Guest user  "')

    # there is a bug in moodle, this gets rid of some data that is in the future...its valid data, but because of importing the dates get fucked.
    df2 = df2[df2["Time"] < endDate]
    df2 = df2[df2["Time"] > startDate]

    df2['Email'] = df['User_full_name'].map(userdict)
    return(df2)

def byActivity(df2, flagSetAction):


    if flagSetAction == "uploadsFlag":

        finaldf = df2.query('Event_name == "A file has been uploaded." or Event_name == "An online text has been uploaded."')

    elif flagSetAction == "viewsFlag":

        finaldf = df2.query('Event_name == "Course module viewed"')

    elif flagSetAction == "completeFlag":

        finaldf = df2.query('Event_name == "Course activity completion updated"')

    elif flagSetAction == "signUp":
        finaldf = df2.drop_duplicates(subset="User_full_name", keep='first', inplace=False)

    else:
        finaldf = df2

    #print(finaldf.to_string())
    return(finaldf)

def activeFilter(df2, flagSetAction, minSize):


    if flagSetAction == "uploadsFlag":

        uploads = df2.groupby(['Event_context']).size()
        uploads = uploads.to_frame(name = 'Size').reset_index()
        uploads = uploads.sort_values(["Size"])
        uploads = uploads.query('Size >='+str(minSize))

        finaldf = uploads

    elif flagSetAction == "viewsFlag":
        counter = df2.groupby(['Event_context', 'Event_name']).size()
        counter = counter.to_frame(name = 'Size').reset_index()
        counter = counter.sort_values(["Size"])
        counter = counter.query('Size >='+str(minSize))
        finaldf = counter

    elif flagSetAction == "completeFlag":
        counter = df2.groupby(['Event_context', 'Event_name']).size()
        counter = counter.to_frame(name = 'Size').reset_index()
        counter = counter.sort_values(["Size"])
        counter = counter.query('Size >='+str(minSize))
        finaldf = counter
    else:
        finaldf = df2

    #print(finaldf.to_string())
    return(finaldf)

def plotByActivity(finaldf):
        finaldf.plot(x='Event_context', y='Size', rot=90, kind="bar")
        plt.gca().invert_xaxis()
        plt.gca().set_ylabel('Number')
        plt.gca().set_xlabel('Activity Name')
        plt.gca().set_title('Completed Activities')
        plt.show()



activityByWeek("completeFlag")

#x = getActivity("no")
#out = byActivity(x,"uploadsFlag")
#out = activeFilter(out, "uploadsFlag", 10)
#plotByActivity(out)


#userActivityPull("no", "'h3lmsman@autistici.org'")
