from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import time


class CanvasBot:
	#  parameters:
	#  browser: web driver element with user-chosen options - overrides the "head" parameter
	#  head: uses headless browser if false
	#  manual_login: waits for user to navigate to their canvas dashboard (within the same tab) before beginning script.
	def __init__(self, browser=None, head=False, manual_login=True):
		self.start_time = time.perf_counter()
		if browser is None:
			chrome_options = Options()
			if not head:
				chrome_options.add_argument("headless")
			chrome_options.add_argument('--no-proxy-server')
			chrome_options.add_argument("--disable-gpu")
			chrome_options.add_argument("keep-alive")
			self.start_load = time.perf_counter()
			self.browser = webdriver.Chrome(executable_path="../driver/chromedriver", options=chrome_options)
			self.load_time = time.perf_counter() - self.start_load
		else:
			self.browser = browser
		self.order = [1, 2, 3, 4, 5, 6, 7]
		self.assignments = []
		self.start_load = time.perf_counter()
		self.link = "<CANVAS LOGIN LINK>"
		if manual_login:
			WebDriverWait(self.browser, 1000).until(ec.presence_of_element_located((By.ID, "DashboardCard_Container")))
			self.start_time = time.perf_counter()
		self.end_time = time.perf_counter()

	def __pressKeys(self, key, otherKey):
		action = ActionChains(self.browser)
		action.key_down(key).key_down(otherKey).key_up(key).key_down(otherKey).perform()

	def set_link(self, link):
		self.link = link

	def get_link(self):
		self.browser.get(self.link)
		self.load_time += time.perf_counter() - self.start_load

	def login(self, uName, pWord):
		print("Logging in...")
		username = self.browser.find_element_by_id("username")
		password = self.browser.find_element_by_id("password")
		username.send_keys(uName)
		password.send_keys(pWord)
		password.send_keys(Keys.ENTER)
		self.__waitUntilLoad(By.ID, "DashboardCard_Container")
		print("Logged in successfully.")
		self.end_time = time.perf_counter()

	def __waitUntilLoad(self, by, string):
		self.start_load = time.perf_counter()
		try:
			element = WebDriverWait(self.browser, 5).until(ec.presence_of_element_located((by, string)))
		except TimeoutException:
			print("Loading took too long. You'll have to check this class manually.")
			element = False
		self.load_time += time.perf_counter() - self.start_load
		return element

	def __switchTab(self, tab_num):
		self.browser.switch_to.window(self.browser.window_handles[tab_num])

	def set_pd_order(self, pdArray):  # class cards can be moved into order manually in the app,
		self.order = pdArray          # which is preferred over using this method.

	def __setOrder(self):
		newAssignments = []
		for i in range(1, 8):
			newAssignments.append(self.assignments[self.order.index(i)])
		self.assignments = newAssignments

	def fetch_upcoming(self):
		print("Fetching assignments...")
		assignmentList = []
		courses = self.browser.find_elements_by_class_name("assignments")
		self.__waitUntilLoad(By.ID, "DashboardCard_Container")
		for c in range(7):
			courses[c].send_keys(Keys.COMMAND + Keys.RETURN)
		for i in range(7):
			self.__switchTab(7 - i)
			courseName = self.__waitUntilLoad(By.XPATH, "//*[@id='breadcrumbs']/ul/li[2]/a/span")
			self.__waitUntilLoad(By.ID, "assignment_group_past")
			try:
				upcomingAssignments = self.browser.find_element_by_id("assignment_group_upcoming_assignments")
			except NoSuchElementException:
				upcomingAssignments = False
			if upcomingAssignments is not False:
				upcomingList = upcomingAssignments.find_element_by_tag_name("ul").find_elements_by_tag_name("li")
				assignList = []
				for n in range(len(upcomingList)):
					assignment = upcomingList[n].find_element_by_tag_name("a")
					dueDate = upcomingList[n].find_element_by_class_name("assignment-date-due").find_element_by_tag_name("span")
					assignList.append({"name": assignment.text, "link": assignment.get_attribute("href"), "due": dueDate.text})
				assignmentList.append({"class": courseName.text, "work": assignList})
			else:
				assignmentList.append({"class": courseName.text, "work": []})
		self.__switchTab(0)
		self.assignments = assignmentList
		self.__setOrder()
		self.end_time = time.perf_counter()
		print("Assignments fetched.")
		return assignmentList

	def print_assignments(self):
		print("-------------------------------")
		for i in range(7):
			a = self.assignments[i]
			print(str(i + 1) + ". " + a["class"])
			if len(a["work"]) > 0:
				dueDate = a["work"][0]["due"]
				print("Due: " + dueDate)
				for assignment in a["work"]:
					nextDue = assignment["due"]
					if nextDue != dueDate:
						dueDate = nextDue
						print("Due: " + dueDate)
					print("---- " + assignment["name"] + ": " + assignment["link"])
			else:
				print("No upcoming assignments.")
			print("-------------------------------")

	def print_time(self):
		print("Process took " + str(round(self.end_time - self.start_time, 2)) + " seconds.")
		print(str(round(self.load_time, 2)) + " seconds were spent loading.")

	def end(self):
		self.browser.quit()

	def restart(self, browser):
		self.__init__(browser)

