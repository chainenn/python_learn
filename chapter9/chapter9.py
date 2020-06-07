#!/usr/bin/python3

class Restaurant():
	def __init__(self,name, type):
		self.name = name
		self.type = type
		self.num_served = 0;
	def describe_restaurant(self):
		print("restaurant name :" + self.name + ",type:" + str(self.type) + ",served num:"+ str(self.num_served))
	def open_restaurant(self):
		print("restaurant is openging")
	def set_num_served(self, num):
		self.num_served = num;
	def increment_num_served(self, num):
		self.num_served += num




class User():
	def __init__(self,first_name, last_name, user_desc):
		self.first_name = first_name
		self.last_name = last_name
		self.user_desc = user_desc
		self.login_attempts = 0
	def describe_user(self):
		print("=================")
		print("fname:" + self.first_name)
		print("lname:" + self.last_name)
		print("user_desc:" + self.user_desc)
		print("login: " + str(self.login_attempts))
	def greet_user(self):
		print(self.first_name+ "." + self.last_name + " say hello ")
		print("{0}.{1} say hello to other".format(self.first_name, self.last_name))
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts =0



class IceCreamStand(Restaurant):
	def __init__(self, name ,type,flavors):
		super().__init__(name,type)
		self.flavors = flavors
	def get_flavors(self):
		print("all flavors:" + str(self.flavors))



class Admin(User):
	def __init__(self, fname,lname,desc):
		super().__init__(fname,lname,desc)
		self.__priv= ["can add post", "can delete post", "can ban user"]
	def show_priv(self):
		print ("priv: " + str(self.__priv))


"""
r1 = Restaurant("r1", 1)
r1.describe_restaurant()
r1.open_restaurant()
r1.set_num_served(10)
r1.describe_restaurant()
r1.increment_num_served(2)
r1.describe_restaurant()

u12=User("cc","mm","is a man")
u12.describe_user()
u12.greet_user()
u12.increment_login_attempts()
u12.increment_login_attempts()
u12.describe_user()
u12.reset_login_attempts()
u12.describe_user()


ice = IceCreamStand("ice", "2", ["cold","hot","apple"])
ice.get_flavors()

ad = Admin("cc","mm","other man " )
ad.show_priv()
ad.describe_user()
print("fname11 :" + ad.first_name)
#print("priv : " + str(ad.__priv))

"""