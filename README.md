# Canvas Bot
Automated to-do list for your Canvas assignments.  

### Why is this necessary?
The built-in to-do list on Canvas always gets flooded with announcements and calendar updates that have little to do with your actual work, and it takes a lot of valuable time to manually search through each class individually.

### How does this solve the problem?
By automatically searching your assignments and returning a list of all relevant work for each class, Canvas Bot reduces all the time it takes to find your assignments down to just 10-15 seconds, most of which is governed by your internet speed.

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


Example Output  
-------------------------------
1. Govt & Politics - AP - Washington  
Due: Jun 5 at 10am  
---- Supreme Court Review: [https://canvas.instructure.com/courses/185372/assignments/9846224](https://youtu.be/dQw4w9WgXcQ)
-------------------------------
2. Biology - AP - Adams  
Due: Jun 5 at 10am  
---- Mitochondria Worksheet: [https://canvas.instructure.com/courses/846375/assignments/1374582](https://youtu.be/dQw4w9WgXcQ)
-------------------------------
3. Spanish III - Jefferson  
Due: Jun 12 at 11:59pm  
---- Puerto Rico Research Paper: [https://canvas.instructure.com/courses/657354/assignments/3856364](https://youtu.be/dQw4w9WgXcQ)
-------------------------------
4. Art I - Madison  
Due: Jun 12 at 10am  
---- Digital Art Project: [https://canvas.instructure.com/courses/245185/assignments/4857366](https://youtu.be/dQw4w9WgXcQ)
-------------------------------
5. Calculus BC - AP - Lincoln    
Due: Jun 5 at 10am   
---- Pg 385 #10-20, 18-30, 39, 50: [https://canvas.instructure.com/courses/245767/assignments/5579435](https://youtu.be/dQw4w9WgXcQ)  
Due: Jun 12 at 10am      
---- Gradient Review: [https://canvas.instructure.com/courses/906453/assignments/4478563](https://youtu.be/dQw4w9WgXcQ)
-------------------------------
6. English 10 - GT - Kennedy    
Due: Jun 5 at 10am    
---- Chapter 7 Review: [https://canvas.instructure.com/courses/793620/assignments/8462945](https://youtu.be/dQw4w9WgXcQ)  
---- Chapter 8 Theme Analysis: [https://canvas.instructure.com/courses/857463/assignments/3346526](https://youtu.be/dQw4w9WgXcQ)
-------------------------------
7. Computer Science A - AP - Reagan  
Due: Jun 5 at 10am  
---- Object-Oriented Design Review: [https://canvas.instructure.com/courses/123456/assignments/7891011](https://youtu.be/dQw4w9WgXcQ)
-------------------------------


Note: Not affiliated with Instructure Canvas in any way. This was entirely a personal project. Please don't sue me.
