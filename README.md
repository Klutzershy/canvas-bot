# Canvas Bot
Automated to-do list for your Canvas assignments.  

### To run from command line:  

  `cd canvas-bot`  
  `python3 ManualDemo.py`  
> Required: Canvas dashboard in card view.  
> Recommended: rearrange classes so that they are in the same order as your class periods.


Navigate to and log in to Canvas on the initial tab.
The process will automatically begin.
Alternatively, the set_link followed by the get_link command can be used to direct the bot to your login link, where you will be prompted to login yourself.

### Class Options
| Parameter | Default | Description |
| --- | --- | --- |
| `head` | False | Pass in True to show the browser, False to run in headless. |
| `browser` | None | Pass a Selenium Webdriver instance or it will create its own. |
| `manual_login` | True | Pass in False if using a set_link command. |


### Methods
| Method | Parameters | Purpose |
| --- | --- | --- |
| `set_link` | link | Pass the link to the Canvas login page. |
| `get_link` | none | Call after setting a link to go to the link. |
| `login` | uName, pWord | Login using a username and password from input. |
| `set_pd_order` | pdArray | Optionally enter a list of integers representing the period numbers for each class. |
| `fetch_upcoming` | none | Collects all upcoming assignments and prepares a to-do list. |
| `print_assignments` | none | Print the to-do list. |
| `print_time` | none | Logs the time it took to complete the script. |
| `end` | none | Closes the window. |
| `restart` | none | Opens a new window. |

Note: Not affiliated with Instructure Canvas in any way. This was entirely a personal project. Please don't sue me.
