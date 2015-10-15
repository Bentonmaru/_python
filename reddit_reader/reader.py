import praw

subreddit = input("Please enter a subreddit to continue: ")

def main(submission):
	r = praw.Reddit(user_agent='reddit_reader')
	subname = [x.strip() for x in submission.split('/')]
	submissions = r.get_subreddit(subname[-1]).get_hot(limit=30)
	submission_form =  "{}) {} : {} <{}>"
	print("Top 30 Posts from /r/" + subname[-1])
	count = 1
	for sub in submissions:
		print(submission_form.format(count, sub.ups, sub.title, sub.url))
		count += 1
	

main(subreddit)