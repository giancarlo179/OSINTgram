import instaloader
from getpass import getpass

# Instantiate the API client
L = instaloader.Instaloader()

# Set your username and password
L.context.log("Setting username and password")
L.context.username = getpass("Insert your Instagram account: ")
L.context.password = getpass("Insert your password: ")

# Target user's profile
target_username = input("Insert target user profile: ")

# Get the user's profile
profile = instaloader.Profile.from_username(L.context, target_username)

# Print the user's information
print("Username:", profile.username)
print("Full name:", profile.full_name)
print("Biography:", profile.biography)
print("Followers:", profile.followers)
print("Following:", profile.followees)
print("Number of posts:", profile.mediacount)
print("URL Pic Profile: \n", profile.get_profile_pic_url())
