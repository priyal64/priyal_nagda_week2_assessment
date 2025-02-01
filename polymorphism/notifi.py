# •	14. Implement method 
# overriding for a `Notification` class where `send()` is overridden 
# in `EmailNotification` and `SMSNotification`.

class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self,message,logo):
        print(logo,"i am a notification from email: ",message)

class SMSNotification(Notification):
    def send(self,message,logo):
        print(logo,"i am a notification from sms:",message)
sms=SMSNotification()
sms.send("your recharge plan is going to expire soon please recharge fast....","SMS")

mail=EmailNotification()
mail.send("You logged into this device ignore if you loggend in ,if you are not then click this button to block or report...","email")

