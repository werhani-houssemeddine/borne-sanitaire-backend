from lib.HTTP import HTTP_REQUEST, HTTP_RESPONSE

class DeviceMiddleware:
  @staticmethod
  def checkDevice(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def addNewDevice(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def createNewDevice(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def getCurrentDevice(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def getMyDevices(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass