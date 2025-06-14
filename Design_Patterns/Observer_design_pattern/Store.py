from Observable.IphoneObservableImpl import IphoneObservableImpl
from Observer.EmailAlertObserverImpl import EmailAlertObserverImpl
from Observer.MobileAlertObserverImpl import MobileAlertObserverImpl

if __name__ == "__main__":
    iphoneStockObservable = IphoneObservableImpl()

    observer1 = EmailAlertObserverImpl(iphoneStockObservable ,"xyz@gmail.com")
    observer2 = EmailAlertObserverImpl(iphoneStockObservable ,"abc@gmail.com")
    observer3 = MobileAlertObserverImpl(iphoneStockObservable ,"1234567890")

    iphoneStockObservable.add(observer1)
    iphoneStockObservable.add(observer2)
    iphoneStockObservable.add(observer3)

    iphoneStockObservable.setStockCount(15)
