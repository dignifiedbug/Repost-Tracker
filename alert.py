import praw

def alert(reddit, new_submission, original_submission_data):
	# Set up attributes.
	original_id = original_submission_data[0]
	original_shortlink = 'https://redd.it/' + str(original_id)	
	
	# Grab custom config.
	site_name = 'Repost Tracker Bot'
	config = praw.config.Config(site_name)
	receiver = config.custom['alert_receiver']

	# Send the alert (PM).
	reddit.redditor(receiver).message(
		'Repost Alert for r/{}'.format(new_submission.subreddit),
		'Title: *{}*'
		'\n\n'
		'[New Post]({})'
		'\n\n'
		'[Original Post]({})'.format(
			new_submission.title,
			new_submission.shortlink,
			original_shortlink,
		)
	)