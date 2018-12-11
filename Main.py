from pyfcm import FCMNotification
import random


push_service = FCMNotification(api_key="AAAA8un-MkA:APA91bFJnBY7q37ERY3cq4F5QULtsV_-YuWLG1e_CxhSfRKzeusdlx-PW73cDdHCzNign3YZvdFv0yeg0O6UikwdVCgo1cmOamrJRqXWHBG19WPJfNS3dXg4fRyGQMa66c5fF3MYOoqG") #api_key from firebase project
registration_ids = [None] #The id of the client(s) to receive messages
    
message_title = "Hello World"
    
message_body_short = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis."
message_body_average = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis."
message_body_long = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis.","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis."
messages = [message_body_short, message_body_average, message_body_long] 
    
def random_messages():
    for i in range(50):
        result = push_service.notify_multiple_devices(registration_ids=registration_ids,
                                         message_title=message_title,
                                         message_body=messages[random.randint(0,2)])
        
        
def variety_messages():
    for j in range(3):
        for i in range(25):
            result = push_service.notify_multiple_devices(registration_ids=registration_ids,
                                             message_title=message_title,
                                             message_body=messages[j])

def consistent_average():
    while True:
        result = push_service.notify_multiple_devices(registration_ids=registration_ids,
                                         message_title=message_title,
                                         message_body=messages[1])
        

def stress_test():
    while True:
        result = push_service.notify_multiple_devices(registration_ids=registration_ids,
                                         message_title=message_title,
                                         message_body=messages[0])
        


if __name__ == '__main__':
    
    choice = input("Choose the test type with a number of 1-4: \n 1: Send 50 random messages. \n 2: Send 25 of each message type \n 3: Measure the delay between receiving average messages. \n 4: Stress test \n")

    if choice == 1:
        random_messages()
    elif choice == 2:
        variety_messages()
    elif choice == 3:
        consistent_average()
    elif choice == 4:
        stress_test()
    else: 
        print("Input error")
        exit(1)
    
    result = push_service.notify_multiple_devices(registration_ids=registration_ids,
                                         message_title=message_title,
                                         message_body=message_body_short)
    
    print(result)

    