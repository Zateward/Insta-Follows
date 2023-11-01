import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException

def find_unfollowed_followings(username):
    followers_list = []
    following_list = []

    loader = instaloader.Instaloader()

    try:
        loader.login('luis.nogueraa', '_?&ziXpeBwaPV4N')
    except TwoFactorAuthRequiredException:
        code = input('Enter your code: ')
        loader.two_factor_login(code)

    profile = instaloader.Profile.from_username(loader.context, username)

    followers = profile.get_followers()
    following = profile.get_followees()

    for follower in followers:
        followers_list.append(follower.username)

    for follow in following:
        following_list.append(follow.username)

    # Code to find accounts the specified user follows but doesn't follow back.
    followers_set = set(followers_list)
    following_set = set(following_list)

    unfollowed_followings = following_set - followers_set

    # Print the usernames
    for username in unfollowed_followings:
        print(username)

# Input the Instagram username for which you want to find unfollowed followings.
input_username = input('Enter the Instagram username: ')
find_unfollowed_followings(input_username)
