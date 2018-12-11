from pyfcm import FCMNotification

if __name__ == '__main__':
    push_service = FCMNotification(api_key="null") #api_key from firebase project
    registration_ids = [None] #The id of the client to receive messages
    
    message_title = "Hello World"
    
    message_body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis."
    
    
    result = push_service.notify_multiple_devices(registration_ids=registration_ids,
                                         message_title=message_title,
                                         message_body=message_body)
    
    print(result)
    