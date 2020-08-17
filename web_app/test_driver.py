from cb_controller import register_user
from cb_controller import login_user
from cb_controller import update_preferences


post_data = {"username":"user1","password":"password1","email":"email@email.com","api":"1~88zkyTQfNrE1eV45y1Iqc3oc5cxBe7OIe5NrVyOhBacF1Th6cDmmla3fKkTfCufy"}

print(register_user(post_data))

post_data = {"username":"user1","password":"password1"}

print(login_user(post_data))


post_data = {"username":"anotherone","password":"another","email":"email@email.com","api":"1~88zkyTQfNrE1eV45y1Iqc3oc5cxBe7OIe5NrVyOhBacF1Th6cDmmla3fKkTfCufy"}

print(register_user(post_data))

post_data = {"username":"anotherone","password":"another"}

print(login_user(post_data))


post_data = {"username":"testuser2","password":"testing","email":"email@email.com","api":"1~88zkyTQfNrE1eV45y1Iqc3oc5cxBe7OIe5NrVyOhBacF1Th6cDmmla3fKkTfCufy"}

print(register_user(post_data))

post_data = {"username":"testuser2","password":"testing"}

print(login_user(post_data))