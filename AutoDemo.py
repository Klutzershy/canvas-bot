from src.CanvasBot import CanvasBot
from getpass import getpass

print("Please choose which browser to use:")
print("1. Chrome")
print("2. Firefox")
browser_type = input("Browser Type:")
user = input("Username:")
passW = getpass()

new_bot = CanvasBot(head=False, manual_login=False,browser_type=browser_type)
new_bot.set_link("https://login.rowan.edu/cas/login?service=https%3A%2F%2Frowan.instructure.com%2Flogin%2Fcas") # replace with link to the login page for your Canvas
new_bot.get_link()
new_bot.login(user, passW)
assignments = new_bot.fetch_upcoming()
new_bot.print_assignments()
new_bot.print_time()
new_bot.end()
