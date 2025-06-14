from Observer.NotificationAlertObserver import NotificationAlertObserver


class EmailAlertObserverImpl(NotificationAlertObserver):

    def __init__(self, observable, emailId):
        self.observable = observable
        self.emailId = emailId
    
    def update(self):
        self.send_email()

    def send_email(self):
        print("Email sent to ", self.emailId)

    
