# Repost-Tracker
A tool to alert you when a repost is submitted.

### Recommendations
[A comprehensive guide to running your bot](redd.it/3d3iss) should help answer most questions.

Expect download_history.py to take a while (depending on the size of your subreddit). It may finish before 100%.

DB Browser (*[Website](http://sqlitebrowser.org/)*, *[Github](https://github.com/sqlitebrowser/sqlitebrowser)*) for SQLite is an excellent tool to view your database.

### Customizing
alert.py is called when a repost is detected; you can edit this file to perform any action you want.

If you wish to use a custom praw.ini site name, edit *site_name* in all three python modules.

To recieve commandline output for every post detected, uncomment line 52 in *repost_tracker.py*
