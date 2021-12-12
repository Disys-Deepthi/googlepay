import googlepay

Deepthi=googlepay.Google_pay("Deeps.jayadevan@gmail.com","9940442831","Deepthi_Jayadevan")
Deepthi.open_gpay()
Deepthi.email_verification()
Deepthi.mobile_verification()
Deepthi.name_verification()
Deepthi.otp_verification(502792,502792)
Deepthi.Bank_verification()
Deepthi.PanCard_Verification()
Deepthi.set_Pin("2002")
Deepthi.Enter_your_Pin(2002,2002)

class Phone_pe(googlepay.Google_pay):                                                                                          
    def __init__(self,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

    def open_phonepe(self):
        print("Phone pe")
        
Deeps=Phone_pe("Deeps.jayadevan@gmail.com","9940442831","Deepthi_Jayadevan")
Deeps.open_phonepe()
Deeps.mobile_verification()
Deeps.name_verification()
Deeps.otp_verification(860695,860695)
Deeps.Bank_verification()
Deeps.PanCard_Verification()
Deeps.set_Pin("2002")
Deeps.Enter_your_Pin(2002,2002)

        
googlepay=[{"name":"Deepthi","gpaynum":9940442831,"type":"personal","transaction":"regular"},                     
           {"name":"nethra","gpaynum":8825555140,"type":"personal","transaction":"regular"},
           {"name":"jyo","gpaynum":9600114878,"type":"personal","transaction":"rare"},
           {"name":"praveen","gpaynum":9360763652,"type":"personal","transaction":"never"},
           {"name":"mithh","gpaynum":8596266985,"type":"personal","transaction":"rare"},
           {"name":"akash","gpaynum":9597916931,"type":"personal","transaction":"rare"},
           {"name":"sarveshi","gpaynum":8056469214,"type":"personal","transaction":"regular"},
           {"name":"yashvi","gpaynum":9962454833,"type":"personal","transaction":"rare"},
           {"name":"sudha","gpaynum":8015341851,"type":"personal","transaction":"rare"},
           {"name":"lakshmi","gpaynum":7305624091,"type":"personal","transaction":"rare"},
           {"name":"krishnan","gpaynum":8939509826,"type":"personal","transaction":"rare"},
           {"name":"latha","gpaynum":6369121983,"type":"personal","transaction":"regular"},
           {"name":"ashok","gpaynum":9833807044,"type":"personal","transaction":"regular"},
           {"name":"jyothi","gpaynum":9941297487,"type":"personal","transaction":"rare"},
           {"name":"rajan","gpaynum":7200001990,"type":"personal","transaction":"regular"},
           {"name":"geetha","gpaynum":6382880108,"type":"personal","transaction":"rare"},
           {"name":"rajamohan","gpaynum":9941656319,"type":"personal","transaction":"regular"},
           {"name":"jayadevan","gpaynum":9500075619,"type":"personal","transaction":"rare"},
           {"name":"prabu","gpaynum":8072512570,"type":"personal","transaction":"regular"},
           {"name":"hrithik","gpaynum":6382761961,"type":"personal","transaction":"rare"},
           {"name":"akshay","gpaynum":9791045340,"type":"personal","transaction":"regular"},
           {"name":"rambo","gpaynum":9841032642,"type":"personal","transaction":"regular"},
           {"name":"rathna","gpaynum":6383908036,"type":"personal","transaction":"regular"},
           {"name":"kp","gpaynum":8248631340,"type":"personal","transaction":"rare"},
           {"name":"rama","gpaynum":6374339918,"type":"personal","transaction":"regular"},
           {"name":"giri","gpaynum":9840644601,"type":"personal","transaction":"regular"},
           {"name":"hari","gpaynum":9379641175,"type":"personal","transaction":"regular"},
           {"name":"shwetha","gpaynum":8124252926,"type":"personal","transaction":"regular"},
           {"name":"vicky","gpaynum":9176093745,"type":"personal","transaction":"regular"},
           {"name":"sabari","gpaynum":9176358088,"type":"personal","transaction":"regular"},
           {"name":"shrish","gpaynum":7305331140,"type":"personal","transaction":"rare"},
           {"name":"vivnish","gpaynum":6384316771,"type":"personal","transaction":"regular"},]


for i in googlepay:                                                                                                             
    for j,k in i.items():                                                                                                       
        print(f"{j}:{k}")
    

