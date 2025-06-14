from Observer.NotificationAlertObserver import NotificationAlertObserver

class MobileAlertObserverImpl(NotificationAlertObserver):

    def __init__(self, observable, mobile_number):
        self.observable = observable
        self.mobile_number = mobile_number
    
    def update(self):
        self.send_msg_on_mobile()

    def send_msg_on_mobile(self):
        print("Mobile msg sent to ", self.mobile_number)

    
