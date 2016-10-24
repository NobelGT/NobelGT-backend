from distutils.core import setup

setup(
        name='NobelGT-backend',
        version='',
        packages=['app', 'env.lib.python2.7.distutils', 'env.lib.python2.7.encodings',
                  'env.lib.python2.7.site-packages.pip', 'env.lib.python2.7.site-packages.pip.req',
                  'env.lib.python2.7.site-packages.pip.vcs', 'env.lib.python2.7.site-packages.pip.utils',
                  'env.lib.python2.7.site-packages.pip.compat', 'env.lib.python2.7.site-packages.pip.models',
                  'env.lib.python2.7.site-packages.pip._vendor', 'env.lib.python2.7.site-packages.pip._vendor.distlib',
                  'env.lib.python2.7.site-packages.pip._vendor.distlib._backport',
                  'env.lib.python2.7.site-packages.pip._vendor.colorama',
                  'env.lib.python2.7.site-packages.pip._vendor.html5lib',
                  'env.lib.python2.7.site-packages.pip._vendor.html5lib.trie',
                  'env.lib.python2.7.site-packages.pip._vendor.html5lib.filters',
                  'env.lib.python2.7.site-packages.pip._vendor.html5lib.serializer',
                  'env.lib.python2.7.site-packages.pip._vendor.html5lib.treewalkers',
                  'env.lib.python2.7.site-packages.pip._vendor.html5lib.treeadapters',
                  'env.lib.python2.7.site-packages.pip._vendor.html5lib.treebuilders',
                  'env.lib.python2.7.site-packages.pip._vendor.lockfile',
                  'env.lib.python2.7.site-packages.pip._vendor.progress',
                  'env.lib.python2.7.site-packages.pip._vendor.requests',
                  'env.lib.python2.7.site-packages.pip._vendor.requests.packages',
                  'env.lib.python2.7.site-packages.pip._vendor.requests.packages.chardet',
                  'env.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3',
                  'env.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.util',
                  'env.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.contrib',
                  'env.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages',
                  'env.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
                  'env.lib.python2.7.site-packages.pip._vendor.packaging',
                  'env.lib.python2.7.site-packages.pip._vendor.cachecontrol',
                  'env.lib.python2.7.site-packages.pip._vendor.cachecontrol.caches',
                  'env.lib.python2.7.site-packages.pip._vendor.pkg_resources',
                  'env.lib.python2.7.site-packages.pip.commands', 'env.lib.python2.7.site-packages.pip.operations',
                  'env.lib.python2.7.site-packages.zope.interface',
                  'env.lib.python2.7.site-packages.zope.interface.tests',
                  'env.lib.python2.7.site-packages.zope.interface.common',
                  'env.lib.python2.7.site-packages.zope.interface.common.tests',
                  'env.lib.python2.7.site-packages.geopy', 'env.lib.python2.7.site-packages.geopy.geocoders',
                  'env.lib.python2.7.site-packages.numpy', 'env.lib.python2.7.site-packages.numpy.ma',
                  'env.lib.python2.7.site-packages.numpy.doc', 'env.lib.python2.7.site-packages.numpy.fft',
                  'env.lib.python2.7.site-packages.numpy.lib', 'env.lib.python2.7.site-packages.numpy.core',
                  'env.lib.python2.7.site-packages.numpy.f2py', 'env.lib.python2.7.site-packages.numpy.compat',
                  'env.lib.python2.7.site-packages.numpy.linalg', 'env.lib.python2.7.site-packages.numpy.random',
                  'env.lib.python2.7.site-packages.numpy.testing', 'env.lib.python2.7.site-packages.numpy.distutils',
                  'env.lib.python2.7.site-packages.numpy.distutils.command',
                  'env.lib.python2.7.site-packages.numpy.distutils.fcompiler',
                  'env.lib.python2.7.site-packages.numpy.matrixlib', 'env.lib.python2.7.site-packages.numpy.polynomial',
                  'env.lib.python2.7.site-packages.txaio', 'env.lib.python2.7.site-packages.wheel',
                  'env.lib.python2.7.site-packages.wheel.test',
                  'env.lib.python2.7.site-packages.wheel.test.simple.dist.simpledist',
                  'env.lib.python2.7.site-packages.wheel.test.complex-dist.complexdist',
                  'env.lib.python2.7.site-packages.wheel.tool', 'env.lib.python2.7.site-packages.wheel.signatures',
                  'env.lib.python2.7.site-packages.twisted', 'env.lib.python2.7.site-packages.twisted.tap',
                  'env.lib.python2.7.site-packages.twisted.web', 'env.lib.python2.7.site-packages.twisted.web.test',
                  'env.lib.python2.7.site-packages.twisted.web._auth', 'env.lib.python2.7.site-packages.twisted.cred',
                  'env.lib.python2.7.site-packages.twisted.cred.test', 'env.lib.python2.7.site-packages.twisted.mail',
                  'env.lib.python2.7.site-packages.twisted.mail.test',
                  'env.lib.python2.7.site-packages.twisted.mail.scripts',
                  'env.lib.python2.7.site-packages.twisted.news', 'env.lib.python2.7.site-packages.twisted.news.test',
                  'env.lib.python2.7.site-packages.twisted.pair', 'env.lib.python2.7.site-packages.twisted.pair.test',
                  'env.lib.python2.7.site-packages.twisted.test', 'env.lib.python2.7.site-packages.twisted.conch',
                  'env.lib.python2.7.site-packages.twisted.conch.ui',
                  'env.lib.python2.7.site-packages.twisted.conch.ssh',
                  'env.lib.python2.7.site-packages.twisted.conch.test',
                  'env.lib.python2.7.site-packages.twisted.conch.client',
                  'env.lib.python2.7.site-packages.twisted.conch.insults',
                  'env.lib.python2.7.site-packages.twisted.conch.scripts',
                  'env.lib.python2.7.site-packages.twisted.conch.openssh_compat',
                  'env.lib.python2.7.site-packages.twisted.names', 'env.lib.python2.7.site-packages.twisted.names.test',
                  'env.lib.python2.7.site-packages.twisted.trial', 'env.lib.python2.7.site-packages.twisted.trial.test',
                  'env.lib.python2.7.site-packages.twisted.trial._dist',
                  'env.lib.python2.7.site-packages.twisted.trial._dist.test',
                  'env.lib.python2.7.site-packages.twisted.words', 'env.lib.python2.7.site-packages.twisted.words.im',
                  'env.lib.python2.7.site-packages.twisted.words.test',
                  'env.lib.python2.7.site-packages.twisted.words.xish',
                  'env.lib.python2.7.site-packages.twisted.words.protocols',
                  'env.lib.python2.7.site-packages.twisted.words.protocols.jabber',
                  'env.lib.python2.7.site-packages.twisted.logger',
                  'env.lib.python2.7.site-packages.twisted.logger.test',
                  'env.lib.python2.7.site-packages.twisted.python',
                  'env.lib.python2.7.site-packages.twisted.python.test',
                  'env.lib.python2.7.site-packages.twisted.runner',
                  'env.lib.python2.7.site-packages.twisted.runner.test',
                  'env.lib.python2.7.site-packages.twisted.spread', 'env.lib.python2.7.site-packages.twisted.plugins',
                  'env.lib.python2.7.site-packages.twisted.scripts',
                  'env.lib.python2.7.site-packages.twisted.scripts.test',
                  'env.lib.python2.7.site-packages.twisted._threads',
                  'env.lib.python2.7.site-packages.twisted._threads.test',
                  'env.lib.python2.7.site-packages.twisted.internet',
                  'env.lib.python2.7.site-packages.twisted.internet.test',
                  'env.lib.python2.7.site-packages.twisted.internet.iocpreactor',
                  'env.lib.python2.7.site-packages.twisted.persisted',
                  'env.lib.python2.7.site-packages.twisted.persisted.test',
                  'env.lib.python2.7.site-packages.twisted.protocols',
                  'env.lib.python2.7.site-packages.twisted.protocols.gps',
                  'env.lib.python2.7.site-packages.twisted.protocols.mice',
                  'env.lib.python2.7.site-packages.twisted.protocols.test',
                  'env.lib.python2.7.site-packages.twisted.protocols.haproxy',
                  'env.lib.python2.7.site-packages.twisted.protocols.haproxy.test',
                  'env.lib.python2.7.site-packages.twisted.enterprise',
                  'env.lib.python2.7.site-packages.twisted.application',
                  'env.lib.python2.7.site-packages.twisted.application.test',
                  'env.lib.python2.7.site-packages.twisted.application.twist',
                  'env.lib.python2.7.site-packages.twisted.application.twist.test',
                  'env.lib.python2.7.site-packages.twisted.application.runner',
                  'env.lib.python2.7.site-packages.twisted.application.runner.test',
                  'env.lib.python2.7.site-packages.twisted.positioning',
                  'env.lib.python2.7.site-packages.twisted.positioning.test',
                  'env.lib.python2.7.site-packages.autobahn', 'env.lib.python2.7.site-packages.autobahn.test',
                  'env.lib.python2.7.site-packages.autobahn.wamp', 'env.lib.python2.7.site-packages.autobahn.wamp.test',
                  'env.lib.python2.7.site-packages.autobahn.asyncio',
                  'env.lib.python2.7.site-packages.autobahn.twisted',
                  'env.lib.python2.7.site-packages.autobahn.rawsocket',
                  'env.lib.python2.7.site-packages.autobahn.rawsocket.test',
                  'env.lib.python2.7.site-packages.autobahn.websocket',
                  'env.lib.python2.7.site-packages.autobahn.websocket.test',
                  'env.lib.python2.7.site-packages.setuptools', 'env.lib.python2.7.site-packages.setuptools.extern',
                  'env.lib.python2.7.site-packages.setuptools.command', 'env.lib.python2.7.site-packages.sqlalchemy',
                  'env.lib.python2.7.site-packages.sqlalchemy.ext',
                  'env.lib.python2.7.site-packages.sqlalchemy.ext.declarative',
                  'env.lib.python2.7.site-packages.sqlalchemy.orm', 'env.lib.python2.7.site-packages.sqlalchemy.sql',
                  'env.lib.python2.7.site-packages.sqlalchemy.util', 'env.lib.python2.7.site-packages.sqlalchemy.event',
                  'env.lib.python2.7.site-packages.sqlalchemy.engine',
                  'env.lib.python2.7.site-packages.sqlalchemy.testing',
                  'env.lib.python2.7.site-packages.sqlalchemy.testing.suite',
                  'env.lib.python2.7.site-packages.sqlalchemy.testing.plugin',
                  'env.lib.python2.7.site-packages.sqlalchemy.dialects',
                  'env.lib.python2.7.site-packages.sqlalchemy.dialects.mssql',
                  'env.lib.python2.7.site-packages.sqlalchemy.dialects.mysql',
                  'env.lib.python2.7.site-packages.sqlalchemy.dialects.oracle',
                  'env.lib.python2.7.site-packages.sqlalchemy.dialects.sqlite',
                  'env.lib.python2.7.site-packages.sqlalchemy.dialects.sybase',
                  'env.lib.python2.7.site-packages.sqlalchemy.dialects.firebird',
                  'env.lib.python2.7.site-packages.sqlalchemy.dialects.postgresql',
                  'env.lib.python2.7.site-packages.sqlalchemy.databases',
                  'env.lib.python2.7.site-packages.sqlalchemy.connectors',
                  'env.lib.python2.7.site-packages.pkg_resources',
                  'env.lib.python2.7.site-packages.pkg_resources.extern',
                  'env.lib.python2.7.site-packages.pkg_resources._vendor',
                  'env.lib.python2.7.site-packages.pkg_resources._vendor.packaging'],
        url='',
        license='',
        author='Cem Gokmen',
        author_email='cgokmen@gatech.edu',
        description=''
)