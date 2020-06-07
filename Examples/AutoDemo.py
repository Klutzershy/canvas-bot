from src.CanvasBot import CanvasBot
from getpass import getpass

user = input("Username:")
passW = getpass()

new_bot = CanvasBot(manual_login=False)
new_bot.set_link("<CANVAS LINK>") # enter the link to the login page for your Canvas
new_bot.get_link()
new_bot.login(user, passW)
assignments = new_bot.fetch_upcoming()
new_bot.print_assignments()
new_bot.print_time()
new_bot.end()
