import sys

print("login validation program")
 
if len(sys.argv) == 4:
    mobile = sys.argv[1]
    email = sys.argv[2]
    password = sys.argv[3]
else:
     
    mobile = "9999999999"
    email = "default@gmail.com"
    password = "admin123"

print("Mobile:", mobile)
print("Email:", email)
print("Password:", password)

