import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.header import Header
from email.utils import formataddr

from datetime import datetime

import csv





smtp_server = "mail.hoppersroppers.org"
port = 587  # For starttls

sender_email = "contact@hoppersroppers.org"
password = "*************"

startDate = datetime.strptime('01/11/19', '%d/%m/%y').date()
endDate = datetime.today().date()


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

        text = """\
        We are totally stoked you signed up for the site!

        We think we have the best courses available and we are in the process of building the best community possible.

        Join our Slack and introduce yourself! https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA

        Jump straight to the material: https://academy.hoppersroppers.org/?redirect=01

        et people know that you started learning with us on your Twitter, Linkedin, or Facebook! We are trying to grow so sharing our site helps us out a ton.

        If you have any questions for us, ask us in Slack or reply to this email!

        See you around!
        - roppers

        """

        html = """\
        <html>
        <body>
        <h2> We are totally stoked you signed up for the site! </h2>

        <p> We think we have the best courses available and we are in the process of building the best community possible. </p>
        <p> <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	Join our Slack and introduce yourself!	</a> </p>

        <form action="https://academy.hoppersroppers.org/?redirect=01">
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
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email probably sent to " + receiver_email)

    print("\n2 Days:\n")
    for i in days2:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]


        message = MIMEMultipart("alternative")
        text = """\
This site is meant to be the best place on the internet to learn the basics of computing and security. We are only five months old, so there is plenty of room for improvement! Any time that you come across something that does not fit that philosophy, let us know.

Check out the material now! https://academy.hoppersroppers.org/?redirect=02

This is a living site and our courses are updated daily. We have feedback modules after each section and constantly are asking for your help to help us improve.

If you have any feedback for us, let us know with a reply or in our Slack! https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA


Stay stoked
- roppers
"""

        html = """\
            <html>
              <body>
            	<p> This site is meant to be the best place on the internet to learn the basics of computing and security. We are only five months old, so there is plenty of room for improvement! Any time that you come across something that does not fit that philosophy, let us know. </p>


                        <form action="https://academy.hoppersroppers.org/?redirect=02">
                            <input type="submit" value="Check out the material now!" />
                        </form>

            	<p> This is a living site and our courses are updated daily. We have feedback modules after each section and constantly are asking for your help to help us improve.</p>

            <p> If you have any feedback for us, let us know with a reply or <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	in our Slack!</a> </p>


            	<p> Stay stoked </p>
            	<p> - roppers </p>
              </body>
            </html>
            """

        message["Subject"] = "Our Site"
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email proabably sent to " + receiver_email)


    print("\n3 Days:\n")
    for i in days3:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]
        message = MIMEMultipart("alternative")
        text = """\
Don't stay stuck in the place you were before signing up for our site.

You've already found the best place on the internet to learn, now all you have to do is work through it and  you will come out the other side ready for anything!

Check out the material now! https://academy.hoppersroppers.org/?redirect=03

If you have any feedback for us, let us know with a reply or in our Slack! https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA

Stay stoked
- roppers

        """

        html = """\
            <html>
              <body>
            	<p> Don't stay stuck in the place you were before signing up for our site. </p>

                <p> You've already found the best place on the internet to learn, now all you have to do is work through it and  you will come out the other side ready for anything! </p>



            <form action="https://academy.hoppersroppers.org/?redirect=03">
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
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email proabably sent to " + receiver_email)

    print("\n5 Days:\n")
    for i in days5:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]

        message = MIMEMultipart("alternative")
        text = """\
You've been busy since you signed up and we hope that everything is going well!

If you have any feedback for us, let us know with a reply or in our Slack! https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA


Check out the material now! https://academy.hoppersroppers.org/?redirect=05


Stay stoked
- roppers

"""

        html = """\
            <html>
              <body>
            	<p> You've been busy since you signed up and we hope that everything is going well!
             </p>


             <p> If you have any feedback for us, let us know with a reply or <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	in our Slack!</a> </p>

            <form action="https://academy.hoppersroppers.org/?redirect=05">
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
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email proabably sent to " + receiver_email)

    print("\n7 Days:\n")
    for i in days7:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]
        message = MIMEMultipart("alternative")
        text = """\
We hope you are enjoying the material so far, keep up the great work!

To help us out, we would love it if you could share our course with some of your friends and followers so that we can help more students! https://hoppersroppers.org/training.html


Get Back to Learning! https://academy.hoppersroppers.org/?redirect=07



Stay stoked
- roppers


"""

        html = """\
    <html>
      <body>
        <p> We hope you are enjoying the material so far, keep up the great work!
     </p>

    <p> To help us out, we would love it if you could share our course with some of your friends and followers so that we can help more students! </p>
    <p> https://hoppersroppers.org/training.html </p>

    <form action="https://academy.hoppersroppers.org/?redirect=07">
        <input type="submit" value="Get Back to Learning!" />
    </form>

     <p> If you have any feedback for us, let us know with a reply or <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	in our Slack!</a> </p>





        <p> Stay stoked </p>
        <p> - roppers </p>
      </body>
    </html>
            """


        message["Subject"] = "How Has it Been Going?"
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email proabably sent to " + receiver_email)




def userActivityEmail():

    userdict = {}
    with open('..\\..\\..\\Downloads\\Users (2).csv') as csvfile2:
        userreader = csv.reader(csvfile2, delimiter=',')
        for row in userreader:
            userdict[row[3]+" "+row[4]] = [row[2]]

    thisdict = {}
    today = datetime.today()
    users = []
    with open('..\..\..\Downloads\logs (3).csv') as csvfile:
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






# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first

context = ssl._create_unverified_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    signUpDrip()
