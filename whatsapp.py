#print("Hello ASma AShaaz")

from twilio.rest import Client 
##Second commit message
account_sid = 'AC96d7c9577e19f6a0eb5550b426bad749' 
auth_token = '0bb9c3657273efa1ee8aed167121ffcd' 
client = Client(account_sid, auth_token) 
 
def send_mess():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Sample test body message Shaikuuuu Asma Ashaaz',      
                                to='whatsapp:+919885695500' 
                            ) 
    
    print(message.sid)