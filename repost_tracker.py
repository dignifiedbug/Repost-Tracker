import time
import sqlite3
import praw
import alert


def main():
	# Connect to Reddit.
	site_name = 'Repost Tracker Bot'
	config = praw.config.Config(site_name)
	reddit = praw.Reddit(
		site_name,
		user_agent = 'win:{}:v1 by /u/dignifiedbug'.format(config.client_id))
	subreddit = reddit.subreddit(config.custom['subreddit'])
	# Handle KeyboardInterrupt.
	try:
		while True:
			# Handle normal exceptions.
			try:
				print('{} running...\nExit with Ctrl+C\n'.format(site_name))
				# Iterate through subreddit.submissions stream.
				for submission in subreddit.stream.submissions():
					process_submission(reddit, submission)
			except Exception as e:
				print(e.args)
				print('Restarting in 30 minutes...')
				time.sleep(1800)
	
	except KeyboardInterrupt:
		print('\n[Interrupted]')
	finally:
		print('Process stopped.')
		time.sleep(5)

def process_submission(reddit, submission):
	if submission is not None:
		# Connect to database.
		connection = sqlite3.connect('history.db')
		cursor = connection.cursor()
		cursor.execute(
			"SELECT * FROM data WHERE title = ? ORDER BY time_created ASC",
			(submission.title,))
		details = cursor.fetchone()
		
		if details is None:
			# Submission is not in database.
			values = (submission.id, submission.created, submission.title)
			cursor.execute(
				"INSERT INTO data VALUES (?,?,?)",
				values)
			connection.commit()
			# print('Original: ' + submission.id)
		elif submission.id != details[0]:
			# Submission is a repost.
			alert.alert(reddit, submission, details)
			print('REPOST: ' + submission.id)
		connection.close()


if __name__ == '__main__':
	main()