class Google_pay:                                                                                   
    
    def __init__(self,Email_ID,Phone_number,Name):                                                                 
        self.emailid=Email_ID
        self.mobile=Phone_number
        self.name=Name
        
    def open_gpay(self):
        print("Google Pay")
        
    def email_verification(self):
        if type(self.emailid) == str:                                                                               
            if len(self.emailid) <= 35:                                                                              
                print("email_id verified")
            else:
                raise ValueError("the emailid should not contain more 35 values")
        else:
            raise TypeError("invalid emailid")
    def mobile_verification(self):
        if (len(self.mobile)==10):
            if type(self.mobile) == str:                                                                           
                print("phone number verified")
            else:
                raise TypeError("the phone should contain only integers ")
        else:
            raise ValueError("the phone number should not be grater than or lesser than 10")
        
    def name_verification(self):
        if type(self.name) == str:
            if len(self.name) <= 25:                                                                                
                print("name verified")
            else:
                raise ValueError("The name should contain lesser than or equal to 25 characters")
        else:
            raise TypeError("The name should contain letters only")

    def otp_verification(self,code,otp):
        if(otp==code):
            print("otp verified")
        else:
            raise ValueError("The otp you are entered is not correct")

    def Bank_verification(self):
        self.account_number="985612384587"
        if (len(self.account_number) == 12):
            print("Account number verified")
        else:
            raise ValueError("Inavlid Account number")

    def PanCard_Verification(self):
        self.pan_number="CGQPJ2021L"
        if (len(self.pan_number) == 10):
            print("pan card verified")
        else:
            raise ValueError("Inavlid Pan number")

    def set_Pin(self,number):
        self.pin=number
        if (len(self.pin)==4 or len(self.pin) ==6):
            print("your pin is successfully created")
        else:
            raise ValueError("Invalid pin number")

    def Enter_your_Pin(self,match,pin):
        self.match=match
        self.pin=pin
        if self.match==self.pin:
            print("DONE")
        else:
            raise ValueError("pin not matched")
