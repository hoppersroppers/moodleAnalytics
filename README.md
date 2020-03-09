# moodleAnalytics
A simple script to run retention and engagement analytics for my security training site <https://academy.hoppersroppers.org>.

## tl;dr Retention in free online courses is as bad as people say it is. 

Calculates and graphs DAU/MAU, retention numbers, and engagement curve. 

Also allows site creator to identify accounts based on time since enrollment or time since last access for manual sending of onboarding/re-engagement emails. In progress of adding mailchimp API hooks to automate the emails. Shouldn't be too much work, will require mailchimp premium, which seems like a pain in the ass.

### Daily Active Users (Blue) and Daily Returning Users (Orange) Since Launch

![alt text](https://raw.githubusercontent.com/hoppersroppers/moodleAnalytics/master/img/DAUnSignups.png "DAU")


### Retention (as Measured by Number of Logins)  

![alt text](https://raw.githubusercontent.com/hoppersroppers/moodleAnalytics/master/img/activityHistogram.png
 "retention")

### Days Between User's Last Activity and Sign-Up 

![alt text](https://raw.githubusercontent.com/hoppersroppers/moodleAnalytics/master/img/retention.png "DAU")



Hopefully automated onboarding emails will result in significantly better initial retention in the first week. 

After the first week of automated emails, when students go inactive I plan to pass students over to an automated re-engagement email series. 

