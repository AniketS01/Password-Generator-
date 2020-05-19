import random

upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nums = ["1","2","3","4","5","6","7","8","9","10"]
lower_case = ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
special = ["@","!","#","$","&"]

x = random.choice(upper_case)
y = random.choice(lower_case)
z = random.choice(nums)
p = random.choice(special)
q = random.choice(lower_case)
r = random.choice(lower_case)
s = random.choice(nums)

# you can set it as per your criteria
password = x+y+s+r+q+z+p+y

print(password)

