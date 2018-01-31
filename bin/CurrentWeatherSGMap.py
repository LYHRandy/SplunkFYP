import sys
import xml.dom.minidom, xml.sax.saxutils
import logging
import httplib
from socket import timeout
import datetime
import time
import urllib2

SCHEME = """<scheme>
    <title>NEA Weather Map</title>
    <description>Get data from NEA</description>
    <streaming_mode>simple</streaming_mode>
    <endpoint>
        <args>
            <arg name="AccountKey">
                <title>AccountKey</title>
                <description>Your Account Key.</description>
            </arg>
            <arg name="UniqueUserID">
                <title>UniqueUserID</title>
                <description>Your Unique User ID.</description>
            </arg>
        </args>
    </endpoint>
</scheme>
"""

def do_scheme():
        print SCHEME

def nea_connection(accountKey,uniqueUserID):
        url="https://api.projectnimbus.org/neaodataservice.svc/NowcastSet"
        request = urllib2.Request(url)
        request.add_header("accept", "*/*")
        request.add_header('AccountKey', accountKey)
        request.add_header('UniqueUserID', uniqueUserID)
        result = urllib2.urlopen(request)
        for line in result.readlines():
                print line
                
#read XML configuration passed from splunkd
def get_config():
    config = {}

    try:
        # read everything from stdin
        config_str = sys.stdin.read()

        # parse the config XML
        doc = xml.dom.minidom.parseString(config_str)
        root = doc.documentElement
        conf_node = root.getElementsByTagName("configuration")[0]
        if conf_node:
            logging.debug("XML: found configuration")
            stanza = conf_node.getElementsByTagName("stanza")[0]
            if stanza:
                stanza_name = stanza.getAttribute("name")
                if stanza_name:
                    logging.debug("XML: found stanza " + stanza_name)
                    config["name"] = stanza_name

                    params = stanza.getElementsByTagName("param")
                    for param in params:
                        param_name = param.getAttribute("name")
                        logging.debug("XML: found param '%s'" % param_name)
                        if param_name and param.firstChild and \
                           param.firstChild.nodeType == param.firstChild.TEXT_NODE:
                            data = param.firstChild.data
                            config[param_name] = data
                            logging.debug("XML: '%s' -> '%s'" % (param_name, data))

        
        if not config:
            raise Exception, "Invalid configuration received from Splunk."
                        
    except Exception, e:
        raise Exception, "Error getting Splunk configuration via STDIN: %s" % str(e)

    return config
    
"""def validate_config(accountKey,uniqueUserID):
        try:
                url="https://api.projectnimbus.org/neaodataservice.svc/NowcastSet"
                request = urllib2.Request(url)
                request.add_header("accept", "*/*")
                request.add_header('AccountKey', accountKey)
                request.add_header('UniqueUserID', uniqueUserID)
                result = urllib2.urlopen(request)
                if resp.status != 200:
                        raise Exception,"HTTP request to NEA data returned with status code %d" % (result.getcode())
                        logging.error("Invalid accountKey and GUID %s , %s" % (accountKey,uniqueUserID))
                result.close()
    except Exception,e:
                print "Invalid configuration specified: %s" % str(e)    
"""

#def date_time():
       # print "The time now is: " + str(datetime.datetime.now())

        
def run():
                
        config = get_config()
        
        AccountKey=config["AccountKey"]
        UniqueUserID=config["UniqueUserID"]        
       
        #validate_config(AccountKey,UniqueUserID)
        while True:
                nea_connection(AccountKey,UniqueUserID)
                #date_time()
                time.sleep(300)
                
      
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "--scheme":
            do_scheme()
    else:
        
        run()
        sys.exit(0)

