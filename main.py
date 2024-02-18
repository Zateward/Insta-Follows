import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException

followers_list = []
following_list = []

loader = instaloader.Instaloader()

try:
	loader.login('YOUR_USERNAME','YOUR_PASSWORD')
except TwoFactorAuthRequiredException:
	code = input('Enter your code: ')
	loader.two_factor_login(code)

profile = instaloader.Profile.from_username(loader.context,'YOUR_USERNAME')

followers = profile.get_followers()
following = profile.get_followees()

print(followers)

for follower in followers:
	followers_list.append(follower.username)

for follow in following:
	following_list.append(follow.username)


# code to see paper friends.


followers_set = set(followers_list)
following_set = set(following_list)

papers = following_set - followers_set

# Print the usernames
for username in papers:
    print(username)