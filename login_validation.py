import sys
if len(sys.argv) != 4:
    print("Usage: python login_validation.py 1234567890 anjum@gmail.com 12345")
    sys.exit()
    mobile = sys.argv[1]
    email = sys.argv[2] 
    password = sys.argv[3]
    print("login validation program")
    #validation
    valid_mobile = "1234567890"
    valid_email = "user@gmail.com"
    valid_password = "admin123"
    if (mobile == valid_mobile and email == valid_email and password == valid_password):
        print("Login Successful") 
    else:
        print("Invalid Login credientials")
        
