from pyfcm import FCMNotification

if __name__ == '__main__':
    push_service = FCMNotification(api_key="AAAA8un-MkA:APA91bFJnBY7q37ERY3cq4F5QULtsV_-YuWLG1e_CxhSfRKzeusdlx-PW73cDdHCzNign3YZvdFv0yeg0O6UikwdVCgo1cmOamrJRqXWHBG19WPJfNS3dXg4fRyGQMa66c5fF3MYOoqG") #api_key from firebase project
    registration_ids = [None] #The id of the client to receive messages
    
    message_title = "Hello World"
    
    message_body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis."
    
    
    result = push_service.notify_multiple_devices(registration_ids=registration_ids,
                                         message_title=message_title,
                                         message_body=message_body)
    
    print(result)
    