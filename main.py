import praw
from collections import deque
from time import sleep


r = praw.Reddit("circleModBot by /r/thirdegree")

def _login():
	USERNAME = raw_input("Username?\n> ")
	PASSWORD = raw_input("Password?\n> ")
	r.login(USERNAME, PASSWORD)
	return USERNAME

done = deque(maxlen=200)

Trying = True
while Trying:
	try:
		USERNAME = _login()
		Trying = False
	except praw.errors.InvalidUserPass:
		print "Invalid Username/password, please try again."

def main():
	subs = r.get_subreddit("thirdegree").get_new()
	for i in subs:
		if "[serious]" in i.title.lower() and i.id not in done:
			print i.title
			i.add_comment("**Attention!** Please keep in mind that the OP of this thread has chosen to mark this post with the **[Serious] fedoras only** tag, therefore any replies that are not jokes, puns, off-topic, or are otherwise non-contributory will be removed.\n\nIf you see others posting comments that violate this tag, please report them to the mods!\n\nThanks for your cooperation and enjoy the discussion!\n\n*[I AMA bot](/r/circlejerk), and this action was performed automatically. Please [contact the moderators of this subreddit](http://i3.kym-cdn.com/entries/icons/facebook/000/015/009/SZOm9zp.jpg) if you have any questions or concerns.*")
			sleep(2)
		done.append(i.id)

while True:
	try: 
		main()
		sleep(10)
	except:
		sleep(100)
