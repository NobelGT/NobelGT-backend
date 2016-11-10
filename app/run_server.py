from twisted.application import internet, service
from server import NobelGTServerFactory

port = 9000
factory = NobelGTServerFactory()

application = service.Application("nobelgt")
ngtService = internet.TCPServer(port, factory)
ngtService.setServiceParent(application)