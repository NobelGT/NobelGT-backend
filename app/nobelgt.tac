from twisted.application import internet, service
from server import NobelGTServerFactory
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile

port = 9000
factory = NobelGTServerFactory()

# this is the important bit
application = service.Application("nobelgt")  # create the Application
ngtService = internet.TCPServer(port, factory) # create the service
# add the service to the application
ngtService.setServiceParent(application)

logfile = DailyLogFile("nobelgt.log", "/tmp")
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)