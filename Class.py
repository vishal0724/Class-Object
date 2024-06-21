# print('welcome back')
# #%%
# print('I have created a new cell')
#%%
class work:
	def __init__(self):
		# print('I am in the constructor')
		self.name = 'Vishal'
		self.age = 20

	def creator(self):
		print('{} is the creator of this class'.format(self.name))
	
	def __repr__(self):
		return 'This is the class "work".'
# %%
df1 = work()
print(df1)
print(df1.creator())
df1.age
# %%
de = 'str'