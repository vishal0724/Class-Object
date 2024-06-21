class work:
	def __init__(self):
		# print('I am in the constructor')
		self.name = 'Vishal'
		self.age = 20

	def creator(self):
		return print('{} is the creator of this class'.format(self.name))
	
	def __repr__(self):
		return 'This is the class "work".'
	
	@staticmethod
	def status():
		return print("Don't disturb, I am working.")
	

df1 = work()
print(df1)
print(df1.creator())
print(df1.age)
print(df1.status())
