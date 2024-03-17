#arxu
import requests
url = "https://ap.paymasterbd.net/login_registration/"
headers = {
    "Host": "ap.paymasterbd.net",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "90",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.14.9",
}

data = {
    "phone_number": input("Enter the phone number: "),
    "fcm_key": "",
    "device_id": "97bfda77edefe5",
    "sms_hash_code": input("Enter the message: "),
}

response = requests.post(url, headers=headers, data=data, verify=False)

#print(response.status_code)
print(response.text)

# Your wicked logo goes here:
print('''
                                                                                               
                                                                                               
               AAA               RRRRRRRRRRRRRRRRR   XXXXXXX       XXXXXXXUUUUUUUU     UUUUUUUU
              A:::A              R::::::::::::::::R  X:::::X       X:::::XU::::::U     U::::::U
             A:::::A             R::::::RRRRRR:::::R X:::::X       X:::::XU::::::U     U::::::U
            A:::::::A            RR:::::R     R:::::RX::::::X     X::::::XUU:::::U     U:::::UU
           A:::::::::A             R::::R     R:::::RXXX:::::X   X:::::XXX U:::::U     U:::::U 
          A:::::A:::::A            R::::R     R:::::R   X:::::X X:::::X    U:::::D     D:::::U 
         A:::::A A:::::A           R::::RRRRRR:::::R     X:::::X:::::X     U:::::D     D:::::U 
        A:::::A   A:::::A          R:::::::::::::RR       X:::::::::X      U:::::D     D:::::U 
       A:::::A     A:::::A         R::::RRRRRR:::::R      X:::::::::X      U:::::D     D:::::U 
      A:::::AAAAAAAAA:::::A        R::::R     R:::::R    X:::::X:::::X     U:::::D     D:::::U 
     A:::::::::::::::::::::A       R::::R     R:::::R   X:::::X X:::::X    U:::::D     D:::::U 
    A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::RXXX:::::X   X:::::XXX U::::::U   U::::::U 
   A:::::A             A:::::A   RR:::::R     R:::::RX::::::X     X::::::X U:::::::UUU:::::::U 
  A:::::A               A:::::A  R::::::R     R:::::RX:::::X       X:::::X  UU:::::::::::::UU  
 A:::::A                 A:::::A R::::::R     R:::::RX:::::X       X:::::X    UU:::::::::UU    
AAAAAAA                   AAAAAAARRRRRRRR     RRRRRRRXXXXXXX       XXXXXXX      UUUUUUUUU      
                                                                                               
                                                                                               
                                                                                               
                                                                                               
                                                                                               
                                                                                               
                                                                                               
''')
