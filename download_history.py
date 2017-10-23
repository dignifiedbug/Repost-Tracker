import time
import sqlite3
import praw


# Recording time
beginning = time.time()

# Database timeframe in UNIX.
time_start = 1119484800  # June 23, 2005    |    1230447163 -> Sunday, December 28, 2008 6:52:43 AM
time_end = time.time()   # now

# Connect to Reddit.
site_name = 'Repost Tracker Bot'
config = praw.config.Config(site_name)
reddit = praw.Reddit(
	site_name,
	user_agent = 'win:{}:v1 by /u/dignifiedbug'.format(config.client_id))
subreddit = reddit.subreddit(config.custom['subreddit'])

# Connect to database.
connection = sqlite3.connect('history.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS data (id text, time_created int, title text)")
index = 0

# Search subreddit for all submissions.
try:
	for submission in subreddit.submissions(time_start, time_end):
		values = (submission.id, submission.created_utc, submission.title)
		cursor.execute("INSERT INTO data VALUES (?,?,?)", values)
		index += 1
		
		# Show progress through time, NOT posts.
		progress = (submission.created_utc-time_start) / (time_end-time_start) * 100
		print(str('%.2f' % (100 - progress)) + '% done  |  ' + str(index) + ' posts')

except Exception as e:
	# Loosely handle exceptions.
	print(e.args)
	
finally:	
	# Close database.
	connection.commit()
	connection.close()
	
	print('Finished!\n')
	print('Started UNIX: ' + str(beginning))
	print('Ended UNIX:   ' + str(time.time()))