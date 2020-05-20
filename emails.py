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

from emailContent import *


smtp_server = "mail.hoppersroppers.org"
port = 587  # For starttls



sender_email = "contact@hoppersroppers.org"
password = "****C"

token = "********************7"

username = 'd.m.devey@gmail.com'
apikey = '******************************7'

from notincluded import *

import json



def getUsers():
    request = 'https://academy.hoppersroppers.org/webservice/rest/server.php?wstoken='+token+'&wsfunction=core_user_get_users_by_field&field=id&values\[0\]='

    number = 10
    users = []
    users.append(("email", "firstaccess", "lastaccess"))

    print(users)


    while number < 550:
        fullArg = request+str(number)
        print(fullArg)
        with open("out.txt", "w") as file:

            result = subprocess.run(['curl', fullArg], stdout=file, stderr=subprocess.DEVNULL)
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
    day1 = []
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
        differenceFirst = today-datetime.strptime(x[1], '%Y-%m-%d %H:%M:%S').date()
        differenceLast = today-datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S').date()

        if x == "-" or x == 'Guest user  ':
            continue
        if  differenceFirst.days == 1:
            signUp(email)
            tagNumber = "250313"
            addTag(email,tagNumber)
            day1.append([email])
        if differenceLast.days == 15:
            days15.append([email])

        if differenceLast.days == 30:
            days30.append([email])

        if differenceLast.days == 45:
            days45.append([email])

        if differenceLast.days == 60:
            days60.append([email])

        if differenceLast.days == 90:
            days90.append([email])

        if differenceLast.days == 120:
            days120.append([email])

    print(days15, days30, days45, days60, days90, days120)

    print("\n15 Days:\n")
    for i in days15:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]

        message = MIMEMultipart("alternative")



        message["Subject"] = subjRet15
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textRet15, "plain")
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
        receiver_email = i[0]


        message = MIMEMultipart("alternative")

        message["Subject"] = subjRet30
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textRet30, "plain")
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
        receiver_email = i[0]
        message = MIMEMultipart("alternative")

        message["Subject"] = subjRet45
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textRet45, "plain")
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
        receiver_email = i[0]

        message = MIMEMultipart("alternative")

        message["Subject"] = subjRet60
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textRet60, "plain")
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
        receiver_email = i[0]
        message = MIMEMultipart("alternative")



        message["Subject"] = subjRet90
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textRet90, "plain")
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
        receiver_email = i[0]
        message = MIMEMultipart("alternative")


        message["Subject"] = subjRet120
        message["From"] = formataddr((str(Header("Roppers Academy", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textRet120, "plain")
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

    text += str((day1, days15, days30, days45, days60, days90, days120))




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
            days1.append([email])

        if differenceFirst.days == 2:
            days2.append([email])


        if differenceFirst.days == 3:
            days3.append([email])


        if differenceFirst.days == 5:
            days5.append([email])

        if differenceFirst.days == 7:
            days7.append([email])

    print(days1, days2, days3, days5, days7)

    print("\n1 Day:\n")
    for i in days1:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]
        signUp(receiver_email)

        message = MIMEMultipart("alternative")


        message["Subject"] = subjDay1
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textDay1, "plain")
        part2 = MIMEText(htmlDay1, "html")

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
        receiver_email = i[0]


        message = MIMEMultipart("alternative")

        message["Subject"] = subjDay2
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textDay2, "plain")
        part2 = MIMEText(htmlDay2, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email probably sent to " + receiver_email)


    print("\n3 Days:\n")
    for i in days3:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]
        message = MIMEMultipart("alternative")


        message["Subject"] = subjDay3
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textDay3, "plain")
        part2 = MIMEText(htmlDay3, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email probably sent to " + receiver_email)

    print("\n5 Days:\n")
    for i in days5:
        sender_email = "contact@hoppersroppers.org"
        receiver_email = i[0]

        message = MIMEMultipart("alternative")


        message["Subject"] = subjDay5
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textDay5, "plain")
        part2 = MIMEText(htmlDay5, "html")

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
        receiver_email = i[0]
        message = MIMEMultipart("alternative")


        message["Subject"] = subjDay7
        message["From"] = formataddr((str(Header("Hopper's Roppers", "utf-8")), sender_email ))
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(textDay7, "plain")
        part2 = MIMEText(htmlDay7, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        #print(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email proabably sent to " + receiver_email)


    print("Sending confirmation email.")
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


def createTag(tagName):



    url = "https://us5.api.mailchimp.com/3.0/lists/8d9620c4b7/segments"

    post_params = {'name': tagName, "static_segment":[]}

    r = requests.post(url, auth=(username, apikey), json=post_params)
    try:
        r.raise_for_status()

        results = r.json()
        print(results)
    except:
        print(r)

def addTag(email,tagNumber):

    url = "https://us5.api.mailchimp.com/3.0/lists/8d9620c4b7/segments/"+tagNumber+"/members"

    post_params = {'email_address': email}

    r = requests.post(url, auth=(username, apikey), json=post_params)
    try:
        r.raise_for_status()

        results = r.json()
        print(results)
    except:
        print(r)

def removeTag(email, tagName):

    url = "https://us5.api.mailchimp.com/3.0/lists/8d9620c4b7/members/"+emailHash+"/tags"

    post_params = {"name": tagName, "status": "inactive"}

    r = requests.post(url, auth=(username, apikey), json=post_params)
    try:
        r.raise_for_status()

        results = r.json()
        print(results)
    except:
        print(r)


def printTag(emailAddr):

    import hashlib
    emailHash = (hashlib.md5(emailAddr.lower().encode('utf-8')).hexdigest())


    url = "https://us5.api.mailchimp.com/3.0/lists/8d9620c4b7/members/"+emailHash+"/tags"


    r = requests.get(url, auth=(username, apikey))
    try:
        r.raise_for_status()

        results = r.json()
        print(results)
        y = json.loads(results)
        print(y)

    except:
        print(r)


context = ssl._create_unverified_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    signupDrip(userdict)


"""
context = ssl._create_unverified_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    retentionDrip(userdict)
"""
