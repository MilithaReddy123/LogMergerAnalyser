import psutil 
 
def getServiceStatus(name): 
 
        service = None 
        try: 
            service = psutil.win_service_get(name) 
            service = service.as_dict() 
        except Exception as ex: 
            print (str(ex))
        if service and service['status'] == 'running' : 
            return 'running'
        return 'not running'
