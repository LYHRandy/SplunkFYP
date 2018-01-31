import xml.dom.minidom, xml.sax.saxutils
import logging
import httplib
from socket import timeout
import datetime
import time
import simplejson as json
import urllib2
import sys, os, platform, re
import sched, time
from xml.dom import minidom
import re
from bs4 import BeautifulSoup as soup
import math
import splunk.Intersplunk



#===============================================================================
# #set up logging suitable for splunkd comsumption
# logging.root
# logging.root.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(levelname)s %(message)s')
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)
# logging.root.addHandler(handler)
#===============================================================================


#===============================================================================
# #necessary to allow unbuffered writing for the Splunk Indexer
# class Unbuffered:
#     def __init__(self, stream):
#         self.stream = stream
#     def write(self, data):
#         self.stream.write(data)
#         self.stream.flush()
#     def __getattr__(self, attr):
#         return getattr(self.stream, attr)
#===============================================================================


SCHEME = """<scheme>
    <title>CurrentWeatherSG</title>
    <description>Get data from forecast.</description>
    <use_external_validation>true</use_external_validation>
    <streaming_mode>simple</streaming_mode>
    <endpoint>
        <args>
            <arg name="intervalone">
                <title>Intervalone</title>
                <description>How long to refresh this query?</description>
            </arg>
        </args>  
    </endpoint>
</scheme>
"""

def weather_Connection(intervalone):
   
    url = "http://www.haze.gov.sg/haze-update/past-24-hour-psi-reading.aspx"
    web_soup = soup(urllib2.urlopen(url))
    table = web_soup.findAll('table')[2]
    rows = table.findAll('tr')[1]
    rows2 = table.findAll('tr')[3]
    cols = rows.findAll('strong')
    cols2 = rows2.findAll('strong')
    if len(cols2)< 2:
        psiAverage = cols[1].string
    else:
        psiAverage = cols2[1].string
         
    print 'psiAverage : ' + psiAverage
    splunk.Intersplunk.outputResults(psiAverage)

  

def do_scheme():
    print SCHEME
    
 
def get_response(url):
    conn.request('GET', url)
    result = conn.getresponse()
    data = result.read()
    return json.loads(data)        
## Printing
# def print_forecast(name,di):
    
    
  

    
#read XML configuration passed from splunkd
def get_config():
    #Read XML Configuration data passed from splunkd on stdin
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
            splunk.Intersplunk.parseError("Invalid configuration received from Splunk.")
        
    except Exception, e:
        splunk.Intersplunk.parseError("Error getting Splunk configuration via STDIN: %s" % str(e))
    
    return config
        

def run():
    #The Main function that starts the action. The thread will sleep for however many seconds are configured via the Input.
        config = get_config()

        intervalone = config["intervalone"]
        #intervalone = 40

        while True:
                weather_Connection(intervalone)
                logging.info("Sleeping for %s seconds" %(intervalone))
                time.sleep(float(intervalone))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "--scheme":
            do_scheme()

    else:
        run()    

    sys.exit(0)
