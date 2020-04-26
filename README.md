# Moodle Analytics
In order to measure and improve my numbers, I wrote a series of scripts to run retention and engagement analytics for my security training site <https://academy.hoppersroppers.org>. It converts the logs from the Moodle LMS into a pandas dataframe and goes from there.

We can calculate DAU/WAU/MAU, do cohort retention heatmaps, check the number of students who do a particular action, or really anything else we want to. This all integrates very nicely with my emailing script, so in theory I can personalize the emails even better going forward, but it isn't a priority.

## tl;dr Retention in free online courses is as bad as people say it is.

###  Cohort Retention Heatmaps

![Cohort Heatmap Monthly](https://github.com/hoppersroppers/moodleAnalytics/raw/master/img/cohortPerc.png "retention")

We can easily do retention cohorts by Day/Week/Month and have it display a percentage or a count. With numbers this low, a count demonstrates things better.

![Cohort Heatmap Weekly](https://github.com/hoppersroppers/moodleAnalytics/raw/master/img/cohortCount.png "retention count")

### DAU, WAU, MAU

At least these are going up!

![WAU](https://raw.githubusercontent.com/hoppersroppers/moodleAnalytics/master/img/WAU.png "WAU")
![MAU](https://raw.githubusercontent.com/hoppersroppers/moodleAnalytics/master/img/MAU.png "MAU")


## Content Analytics

Here, we are using the script to see how many people complete each assignment. This provides teacher's great insights on which assignments they are losing students on. In this case, we can see that more than half of all students never install a VM. That means that even after our initial drop off of students who never return to the course, we lose half that number at a single section.

Time to go figure out how to make that easier for students.

![completed Activities](https://raw.githubusercontent.com/hoppersroppers/moodleAnalytics/master/img/completed.png "signups")

### Action Completions

In this case, we are using the script to track the number of new registrations.

![New Singups](https://raw.githubusercontent.com/hoppersroppers/moodleAnalytics/master/img/signUps.png "signups")

Here we are tracking the number of assignments that are submitted each week. Looking at this, it is obvious that the vast majority of students never submit an assignment. What does a teacher have to do to get better engagement? Probably not offer a free online course.

![Assignments Completed](https://raw.githubusercontent.com/hoppersroppers/moodleAnalytics/master/img/assign.png "assign")


### Way Forward

I am currently sending fully automated onboarding emails at 1,2,3,5 and 7 days, and retention emails at 15,30,45,60,90, and 120 days of inactivity. These emails are not customized or based off of anything, they are just Hail Mary's to get students back on the site and improve the numbers.

At some point I will really sit down and do some reading on how to improve these. 
