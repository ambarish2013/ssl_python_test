import urllib2
import requests
import ssl

try:
    ##sslContext = ssl.create_default_context(cafile="/Users/ambarish/Desktop/code/selfsignedhttps/rootCA.pem")
    ##response = urllib2.urlopen('https://localhost:8081/', context=sslContext) 
    response = urllib2.urlopen('https://localhost:8081/')
    print 'response headers: "%s"' % response.info()
    html = response.read()
    print 'response: "%s"' % html
except IOError, e:
    if hasattr(e, 'code'): # HTTPError
        print 'http error code: ', e.code
    elif hasattr(e, 'reason'): # URLError
        print "can't connect, reason: ", e.reason
    else:
        raise
        