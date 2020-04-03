#python3

from datetime import datetime
import matplotlib.pyplot as plt
import csv



from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from email.header import Header
from email.utils import formataddr

startDate = datetime.strptime('01/11/19', '%d/%m/%y').date()
endDate = datetime.today().date()


def retentionEmails():

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
        if x == "-" or x == 'Guest user  ':
            continue

        if difference.days <= 7:
            days7.append((userdict[x],difference.days))

        if difference.days >= 7 and difference.days < 14:
            days14.append((userdict[x],difference.days))


        if difference.days >= 14 and difference.days < 30:
            days30.append((userdict[x],difference.days))


        if difference.days >= 30 and difference.days < 60:
            days60.append((userdict[x],difference.days))

        if difference.days >= 60 and difference.days < 120:
            days120.append((userdict[x],difference.days))

        if difference.days >= 120:
            daysover.append((userdict[x],difference.days))




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


def retentionEmail():

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs (2).csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            thisdict[row[1]] = row[0]

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (1).csv') as csvfile2:
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
        if x == "-" or x == 'Guest user  ':
            continue

        if difference.days == 7:
            days7.append((userdict[x],difference.days))

        if difference.days == 14:
            days14.append((userdict[x],difference.days))


        if difference.days == 30:
            days30.append((userdict[x],difference.days))


        if difference.days == 60:
            days60.append((userdict[x],difference.days))

        if difference.days == 90:
            days120.append((userdict[x],difference.days))

        if difference.days == 120:
            daysover.append((userdict[x],difference.days))




    print("\n7 Days:\n")
    for i in days7:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]
        text = """\
        Subject: 7 Day Follow Up

        What makes good follow up text?
        I should probably copy someone who knows what they are doing.

        A critical bit of all this is that I provide an easy link for them to get back after it.

        Log back in to https://academy.hoppersroppers.org today!

        -roppers """

        message = MIMEMultipart("alternative")

        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        print(sender_email, receiver_email, message)


    print("\n14 Days:\n")
    for i in days14:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]
        text = """\
        Subject: 14 Day Follow Up

        What makes good follow up text?
        I should probably copy someone who knows what they are doing.

        A critical bit of all this is that I provide an easy link for them to get back after it.

        Log back in to https://academy.hoppersroppers.org today!

        -roppers """

        message = MIMEMultipart("alternative")

        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        print(sender_email, receiver_email, message)

    print("\n30 Days:\n")
    for i in days30:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]
        text = """\
        Subject: 30 Day Follow Up

        What makes good follow up text?
        I should probably copy someone who knows what they are doing.

        A critical bit of all this is that I provide an easy link for them to get back after it.

        Log back in to https://academy.hoppersroppers.org today!

        -roppers """

        message = MIMEMultipart("alternative")

        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        print(sender_email, receiver_email, message)

    print("\n60 Days:\n")
    for i in days60:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]
        text = """\
        Subject: 60 Day Follow Up

        What makes good follow up text?
        I should probably copy someone who knows what they are doing.

        A critical bit of all this is that I provide an easy link for them to get back after it.

        Log back in to https://academy.hoppersroppers.org today!

        -roppers """

        message = MIMEMultipart("alternative")

        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        print(sender_email, receiver_email, message)

    print("\n90 Days:\n")
    for i in days120:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]
        text = """\
        Subject: 90 Day Follow Up

        What makes good follow up text?
        I should probably copy someone who knows what they are doing.

        A critical bit of all this is that I provide an easy link for them to get back after it.

        Log back in to https://academy.hoppersroppers.org today!

        -roppers """

        message = MIMEMultipart("alternative")

        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        print(sender_email, receiver_email, message)

    print("\n120 Days:\n")
    for i in daysover:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]
        text = """\
        Subject: 120 Day Follow Up

        What makes good follow up text?
        I should probably copy someone who knows what they are doing.

        A critical bit of all this is that I provide an easy link for them to get back after it.

        Log back in to https://academy.hoppersroppers.org today!

        -roppers """

        message = MIMEMultipart("alternative")

        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        print(sender_email, receiver_email, message)


def recentUsers():

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs (2).csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            thisdict[row[1]] = row[0]

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (1).csv') as csvfile2:
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
        if x == "-" or x == 'Guest user  ':
            continue

        try:
            if difference.days < 30:
                print(userdict[x])
        except:
            print("Broke: "+x)


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
        a = sorted(list(userdict[x]))
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


def signUpDrip():
    days1 = []
    days2 = []
    days3 = []
    days5 = []
    days7 = []
    today = datetime.today().date()



    userdict = userActivityEmail()
    numSignUps = len(userdict)
    retentionList = []
    for x in userdict:

        if userdict[x] == set():
            continue
        dates = []
        email = ""
        for z in userdict[x]:
            if isinstance(z, str):
                email = z
            else:
                dates.append(z)
        a = sorted(dates)
        try:
            first = a[0]
        except:
            #print(x,a)
            continue
        print(x, email, first)



        difference = today-first
        print(difference.days)

        if x == "-" or x == 'Guest user  ':
            continue

        if difference.days == 1:
            days1.append([x, email,difference.days])

        if difference.days == 2:
            days2.append([x, email,difference.days])


        if difference.days == 3:
            days3.append([x, email,difference.days])


        if difference.days == 5:
            days5.append([x, email,difference.days])

        if difference.days == 7:
            days7.append([x, email,difference.days])

    print(days1, days2, days3, days5, days7)


    print("\n1 Day:\n")
    for i in days1:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]

        message = MIMEMultipart("alternative")


        html = """\
    <html>
      <body>
    	<h2> We are totally stoked you signed up for the site! </h2>

    	<p> We think we have the best courses available and we are in the process of building the best community possible. </p>
    <p> <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	Join our Slack and introduce yourself!	</a> </p>

    <<form action="https://academy.hoppersroppers.org/?redirect=01">
        <input type="submit" value="Or Jump Right Into the Material!" />
    </form>
    	<p> Let people know that you started learning with us on your Twitter, Linkedin, or Facebook! We are trying to grow so sharing our site helps us out a ton. </p>

    	<p> If you have any questions for us, ask us in Slack or reply to this email! </p>

    	<p> See you around! </p>
    	<p> - roppers </p>
      </body>
    </html>
    """


        message["Subject"] = "Welcome to the Show!"
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        #part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        #message.attach(part1)
        message.attach(part2)

        print(sender_email, receiver_email, message)

    print("\n2 Days:\n")
    for i in days2:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]

        message = MIMEMultipart("alternative")



        html = """\
        <html>
          <body>
        	<p> This site is meant to be the best place on the internet to learn the basics of computing and security. We are only five months old, so there is plenty of room for improvement! Any time that you come across something that does not fit that philosophy, let us know. </p>

        	<p> This is a living site and our courses are updated daily. We have feedback modules after each section and constantly are asking for your help to help us improve.</p>

        <p> If you have any feedback for us, let us know with a reply or <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	in our Slack!</a> </p>

        <form action="https://academy.hoppersroppers.org/?redirect=02">
            <input type="submit" value="Check out the material now!" />
        </form>

        	<p> Stay stoked </p>
        	<p> - roppers </p>
          </body>
        </html>


        """


        message["Subject"] = "Our Site"
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        #part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        #message.attach(part1)
        message.attach(part2)

        print(sender_email, receiver_email, message)

    print("\n3 Days:\n")
    for i in days3:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]

        message = MIMEMultipart("alternative")


        html = """\
        <html>
          <body>
        	<p> Don't stay stuck in the place you were before signing up for our site. </p>

            <p> You've already found the best place on the internet to learn, now all you have to do is work through it and  you will come out the other side ready for anything! </p>



        <form action="https://academy.hoppersroppers.org/?redirect=02">
            <input type="submit" value="Check out the material now!" />
        </form>


        <p> If you have any feedback for us, let us know with a reply or <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	in our Slack!</a> </p>

        	<p> Stay stoked </p>
        	<p> - roppers </p>
          </body>
        </html>

        """


        message["Subject"] = "Get Yourself to the Next Level"
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        #part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        #message.attach(part1)
        message.attach(part2)

        print(sender_email, receiver_email, message)

    print("\n5 Days:\n")
    for i in days5:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]

        message = MIMEMultipart("alternative")


        html = """\
        <html>
          <body>
        	<p> You've been busy since you signed up and we hope that everything is going well!
         </p>


         <p> If you have any feedback for us, let us know with a reply or <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	in our Slack!</a> </p>

        <form action="https://academy.hoppersroppers.org/?redirect=02">
            <input type="submit" value="Keep Learning" />
        </form>



        	<p> Stay stoked </p>
        	<p> - roppers </p>
          </body>
        </html>

        """


        message["Subject"] = "How Has it Been Going?"
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        #part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        #message.attach(part1)
        message.attach(part2)

        print(sender_email, receiver_email, message)

    print("\n7 Days:\n")
    for i in days7:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]

        message = MIMEMultipart("alternative")


        html = """\
        <html>
          <body>
        	<p> We hope you are enjoying the material so far, keep up the great work!
         </p>

        <p> To help us out, we would love it if you could share our course with some of your friends and followers so that we can help more students! </p>

        <form action="https://academy.hoppersroppers.org/?redirect=02">
            <input type="submit" value="Get Back to Learning!" />
        </form>

         <p> If you have any feedback for us, let us know with a reply or <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	in our Slack!</a> </p>





        	<p> Stay stoked </p>
        	<p> - roppers </p>
          </body>
        </html>


        """


        message["Subject"] = "How was the first week?"
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        #part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        #message.attach(part1)
        message.attach(part2)

        print(sender_email, receiver_email, message)




def userActivityEmail():

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (1).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = [row[2]]

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs (2).csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            if row[1] != '-' and row[1] != "Guest user  ":
                unfilteredDate =datetime.strptime(row[0], '%d/%m/%y, %H:%M').date()
                if unfilteredDate >= startDate and unfilteredDate <= endDate:
                    filteredDate = unfilteredDate

                    try:
                        userdict[row[1]].append(filteredDate)
                    except KeyError:
                        print(row[1])
    for x in userdict:
        if x == "System Administrator":
            userdict[x] = []
        #print(userdict[x])
        s = {d for d in userdict[x]}
        #print(x+": "+str(len(s)))
        userdict[x] = s
    return(userdict)






def userActivity():

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (1).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []
            print(row[2])

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs (2).csv') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in reversed(list(spamreader)):
            if row[1] != '-' and row[1] != "Guest user  ":
                unfilteredDate =datetime.strptime(row[0], '%d/%m/%y, %H:%M').date()
                if unfilteredDate >= startDate and unfilteredDate <= endDate:
                    filteredDate = unfilteredDate

                    try:
                        userdict[row[1]].append(filteredDate)
                    except KeyError:
                        print(row[1])
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
    with open('..\\..\\..\\Downloads\\Users (2).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = []

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs (2).csv') as csvfile:
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




recentUsers()
#userActivityHistogram()
