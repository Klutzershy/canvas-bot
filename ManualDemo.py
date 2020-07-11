from src.CanvasBot import CanvasBot

# In the opened window, login to your Canvas account ON THE INITIAL TAB. Process will start automatically.
new_bot = CanvasBot()

assignments = new_bot.fetch_upcoming()
new_bot.print_assignments()
new_bot.print_time()
#new_bot.end()
# include this command if you don't want it to leave the windoww open.
