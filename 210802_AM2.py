#class USB:
#    def __init__(self, capacity):
#        self.capacity = capacity
    
#    def info(self):
#        print('{}GB USB'.format(self.capacity))

#usb = USB(64)
#usb.info()

class Service:
    def __init__(self, service):    
        self.service = service
       print ('{} Service가 시작되었습니다.'.format(self.service))


    def __del__(self):
        print("{} Service가 종료되었습니다.".format(self.service))

s= Service('길 안내')
del s 