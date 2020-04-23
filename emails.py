import os
import subprocess
import xml.etree.ElementTree as ET
import time
from datetime import datetime

import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.header import Header
from email.utils import formataddr

import requests



smtp_server = "mail.hoppersroppers.org"
port = 587  # For starttls

sender_email = "contact@hoppersroppers.org"
password = "***************"

token = "****************"

username = 'd.m.devey@gmail.com'
apikey = '***********'



def getUsers():
    request = 'https://academy.hoppersroppers.org/webservice/rest/server.php?wstoken='+token+'&wsfunction=core_user_get_users_by_field&field=id&values\[0\]='

    number = 10 
    users = []
    users.append(("email", "firstaccess", "lastaccess"))

    print(users)


    while number < 450:
        fullArg = request+str(number)
        print(fullArg)
        with open("out.txt", "w") as file:

            result = subprocess.run(['curl', fullArg], stdout=file)
            tree = ET.parse("out.txt")
            root = tree.getroot()
            info = []
            for child in root.iter():
                info.append(child.text)
            try:
                users.append((info[14], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(info[40]))), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(info[42])))))
           
                print(number, info[14])
            except:
                print(number, info)


        #print(result.stdout)
        number += 1

    #print(users)
    return(users)



def retentionDrip(userdict):
    days15 = []
    days30 = []
    days45 = []
    days60 = []
    days90 = []
    days120 = []
    today = datetime.today().date()




    numSignUps = len(userdict)
    print(numSignUps)
    retentionList = []
    for x in userdict[1:]:

        print(x)

        email = x[0]
        #differenceFirst = today-datetime.strptime(x[1], '%Y-%m-%d %H:%M:%S').date()

        differenceLast = today-datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S').date()

        if x == "-" or x == 'Guest user  ':
            continue

        if differenceLast.days == 15:
            days15.append([x, email,differenceLast.days])

        if differenceLast.days == 30:
            days30.append([x, email,differenceLast.days])


        if differenceLast.days == 45:
            days45.append([x, email,differenceLast.days])


        if differenceLast.days == 60:
            days60.append([x, email,differenceLast.days])

        if differenceLast.days == 90:
            days90.append([x, email,differenceLast.days])

        if differenceLast.days == 120:
            days120.append([x, email,differenceLast.days])

    print(days15, days30, days45, days60, days90, days120)

    print("\n15 Days:\n")
    for i in days15:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]

        message = MIMEMultipart("alternative")

        text = """\
        It's been a couple weeks since we last saw you, and we'd love to get you back.

        We totally understand that life gets in the way and you might be saving the course for some other time, but we promise that just a few hours a week taking this course will be enough to have a major impact on your ability to learn.

        Jump right back to the material: https://academy.hoppersroppers.org/?redirect=15

        If you don't want to be registered anymore, are planning on doing it at some later point, or just signed up so that you could get updates, let us know at this link so that we can understand what we can do to help our students better. https://forms.gle/jorK42dz5tpUVtRv8

        If you want to help us out, the best thing you can do is to share our site with new students, because we want to reach as many people as possible. https://hoppersroppers.org/training.html

        If you have any questions or feedback for us, ask us in Slack at https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA or reply to this email!

        See you around!
        - roppers

        """
        '''
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
        '''

        message["Subject"] = "How Has it Been Going?"
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        #part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        #message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email probably sent to " + receiver_email)

    print("\n30 Days:\n")
    for i in days30:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]


        message = MIMEMultipart("alternative")
        text = """\
        It's been a month since we last saw you, and we'd love to get you back.

        We totally understand that life gets in the way and you might be saving the course for some other time, but we promise that just a few hours a week taking this course will be enough to have a major impact on your ability to learn.

        Jump right back to the material: https://academy.hoppersroppers.org/?redirect=30

        If you don't want to be registered anymore, are planning on doing it at some later point, or just signed up so that you could get updates, let us know at this link so that we can understand what we can do to help our students better. https://forms.gle/jorK42dz5tpUVtRv8

        If you want to help us out, the best thing you can do is to share our site with new students, because we want to reach as many people as possible. https://hoppersroppers.org/training.html

        If you have any questions or feedback for us, ask us in Slack at https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA or reply to this email!

        See you around!
        - roppers

        """
        '''
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
        '''

        message["Subject"] = "How Has it Been Going?"
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        #part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        #message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email probably sent to " + receiver_email)


    print("\n45 Days:\n")
    for i in days45:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]
        message = MIMEMultipart("alternative")
        text = """\
        It's been over a month since we last saw you, and we'd love to get you back.

        We totally understand that life gets in the way and you might be saving the course for some other time, but we promise that just a few hours a week taking this course will be enough to have a major impact on your ability to learn.

        Jump right back to the material: https://academy.hoppersroppers.org/?redirect=45

        If you don't want to be registered anymore, are planning on doing it at some later point, or just signed up so that you could get updates, let us know at this link so that we can understand what we can do to help our students better. https://forms.gle/jorK42dz5tpUVtRv8

        If you want to help us out, the best thing you can do is to share our site with new students, because we want to reach as many people as possible. https://hoppersroppers.org/training.html

        If you have any questions or feedback for us, ask us in Slack at https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA or reply to this email!

        See you around!
        - roppers

        """
        '''
        html = """\
            <html>
              <body>
            	<p> Don't stay stuck in the place you were before signing up for our site. </p>

                <p> You've already found the best place on the internet to learn, now all you have to do is work through it and  you will come out the other side ready for anything! </p>



            <form action="https://academy.hoppersroppers.org/?redirect=45">
                <input type="submit" value="Check out the material now!" />
            </form>


            <p> If you have any feedback for us, let us know with a reply or <a href="https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA">	in our Slack!</a> </p>

            	<p> Stay stoked </p>
            	<p> - roppers </p>
              </body>
            </html>
            """
        '''
        message["Subject"] = "How Has it Been Going?"
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        #part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        #message.attach(part2)
        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email probably sent to " + receiver_email)

    print("\n60 Days:\n")
    for i in days60:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]

        message = MIMEMultipart("alternative")
        text = """\
        It's been a couple months since we last saw you, and we'd love to get you back.

        We totally understand that life gets in the way and you might be saving the course for some other time, but we promise that just a few hours a week taking this course will be enough to have a major impact on your ability to learn.

        Jump right back to the material: https://academy.hoppersroppers.org/?redirect=60

        If you don't want to be registered anymore, are planning on doing it at some later point, or just signed up so that you could get updates, let us know at this link so that we can understand what we can do to help our students better. https://forms.gle/jorK42dz5tpUVtRv8

        If you want to help us out, the best thing you can do is to share our site with new students, because we want to reach as many people as possible. https://hoppersroppers.org/training.html

        If you have any questions or feedback for us, ask us in Slack at https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA or reply to this email!

        See you around!
        - roppers

        """
        '''
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
            '''

        message["Subject"] = "How Has it Been Going?"
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        #part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        #message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email proabably sent to " + receiver_email)

    print("\n90 Days:\n")
    for i in days90:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]
        message = MIMEMultipart("alternative")
        text = """\
        It's been a few months since we last saw you around, and we'd love to get you back.

        We totally understand that life gets in the way and you might be saving the course for some other time, but we promise that just a few hours a week taking this course will be enough to have a major impact on your ability to learn.

        Jump right back to the material: https://academy.hoppersroppers.org/?redirect=90

        If you don't want to be registered anymore, are planning on doing it at some later point, or just signed up so that you could get updates, let us know at this link so that we can understand what we can do to help our students better. https://forms.gle/jorK42dz5tpUVtRv8

        If you want to help us out, the best thing you can do is to share our site with new students, because we want to reach as many people as possible. https://hoppersroppers.org/training.html

        If you have any questions or feedback for us, ask us in Slack at https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA or reply to this email!

        See you around!
        - roppers

        """

        '''
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
        '''

        message["Subject"] = "How Has it Been Going?"
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        #part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        #message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email proabably sent to " + receiver_email)

    print("\n120 Days:\n")
    for i in days120:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]
        message = MIMEMultipart("alternative")
        text = """\
        It's been a few months since we last saw you around, and we'd love to get you back.

        We totally understand that life gets in the way and you might be saving the course for some other time, but we promise that just a few hours a week taking this course will be enough to have a major impact on your ability to learn.

        Jump right back to the material: https://academy.hoppersroppers.org/?redirect=90

        If you don't want to be registered anymore, are planning on doing it at some later point, or just signed up so that you could get updates, let us know at this link so that we can understand what we can do to help our students better. https://forms.gle/jorK42dz5tpUVtRv8

        If you want to help us out, the best thing you can do is to share our site with new students, because we want to reach as many people as possible. https://hoppersroppers.org/training.html

        If you have any questions for us, ask us in Slack at https://join.slack.com/t/hoppersroppers/shared_invite/zt-d66799ci-tZStzuZ5Nb0Coz5O6huKTA or reply to this email!

        See you around!
        - roppers

        """

        '''
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
'''

        message["Subject"] = "How Has it Been Going?"
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        #part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        #message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email probably sent to " + receiver_email)

    sender_email = "contact@hoppersroppers.org"
    receiver_email = "d.m.devey@gmail.com"
    message = MIMEMultipart("alternative")

    text = """\
    It probably worked today:

    Emails sent to:
    """

    text += str((days15, days30, days45, days60, days90, days120))




    message["Subject"] = "Retention Emails Sent"
    message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    #print(sender_email, receiver_email, message)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Confirmation Email probably sent to " + receiver_email)

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first


def signupDrip(userdict):
    days1 = []
    days2 = []
    days3 = []
    days5 = []
    days7 = []
    today = datetime.today().date()



    #userdict = getUsers()

    numSignUps = len(userdict)
    print(numSignUps)
    retentionList = []
    for x in userdict[1:]:

        print(x)

        email = x[0]
        differenceFirst = today-datetime.strptime(x[1], '%Y-%m-%d %H:%M:%S').date()

        differenceLast = today-datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S').date()
        print(differenceFirst)
        if x == "-" or x == 'Guest user  ':
            continue

        if differenceFirst.days == 1:
            days1.append([x, email,differenceFirst.days])
            
        if differenceFirst.days == 2:
            days2.append([x, email,differenceFirst.days])


        if differenceFirst.days == 3:
            days3.append([x, email,differenceFirst.days])


        if differenceFirst.days == 5:
            days5.append([x, email,differenceFirst.days])

        if differenceFirst.days == 7:
            days7.append([x, email,differenceFirst.days])
            
    print(days1, days2, days3, days5, days7)

    print("\n1 Day:\n")
    for i in days1:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[1]
        signUp(receiver_email)

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


        message["Subject"] = "One Week With Us?"
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

    sender_email = "contact@hoppersroppers.org"
    receiver_email = "d.m.devey@gmail.com"
    message = MIMEMultipart("alternative")

    text = """\
    It probably worked today:

    Emails sent to:
    """

    text += str((days1, days2, days3, days5, days7))




    message["Subject"] = "Sign-Up Emails Sent"
    message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    #print(sender_email, receiver_email, message)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Confirmation Email probably sent to " + receiver_email)

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first

def signUp(emailAddr):


    url = "https://us5.api.mailchimp.com/3.0/lists/8d9620c4b7/members"

    post_params = {'email_address': emailAddr, 'status': 'subscribed'}

    r = requests.post(url, auth=(username, apikey), json=post_params)
    try:
        r.raise_for_status()

        results = r.json()
        print(results)
    except:
        print(r)


def autoEmail():
    userdict = getUsers()
    signupDrip(userdict)
    retentionDrip(userdict)
    print("Auto Emailing Complete")

userdict = getUsers()
context = ssl._create_unverified_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    signupDrip(userdict)
    
'''
context = ssl._create_unverified_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    retentionDrip(userdict)

'''
