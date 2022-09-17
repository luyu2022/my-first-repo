def email_slider():
    print('welcome to the email slicer\n')
    your_email=input('Enter your email address:')
    
    (username,domain)=your_email.split("@")
    (domain,extention)=domain.split(".")
    print("username:",username)
    print("domain:",domain)
    print("extention:",extention)
while True:

    email_slider()