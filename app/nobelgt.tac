import sys
# twistd, when running as root (i.e. in docker), does not include current path in path. We fix that here.
sys.path.append('.')

from twisted.application import internet, service
from server import NobelGTServerFactory

port = 9000
factory = NobelGTServerFactory()

application = service.Application("nobelgt")
ngtService = internet.TCPServer(port, factory)
ngtService.setServiceParent(application)