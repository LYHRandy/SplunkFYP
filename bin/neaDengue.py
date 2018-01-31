import sys
import urllib2
import json
import logging
import xml.dom.minidom
import time
from SVY21 import SVY21

logging.root
logging.root.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logging.root.addHandler(handler)

SCHEME = """<scheme>
    <title>OneMap(Dengue Cluster)</title>
    <description>Get data from OneMap(Dengue Cluster).</description>
    <use_external_validation>true</use_external_validation>
    <streaming_mode>simple</streaming_mode>
    <endpoint>
        <args>
            <arg name="TokenKey">
                <title>TokenKey</title>
           <description>Your Token Key here</description>
            </arg>
        </args>
    </endpoint>
</scheme>
"""

def do_scheme():
    print SCHEME
    
def onemap_connection(tokenKey):  
    #formating python dict
    try:
        url = 'http://www.onemap.sg/API/services.svc/mashupData?token=' + tokenKey +'&themeName=Dengue_cluster&otptFlds=HYPERLINK,NAME&extents=-4423.6,15672.6,69773.4,52887.4'
        page = urllib2.urlopen(url)
        content = page.read()
        dengueDict = json.loads(content)
        dengueDictLength = len(dengueDict['SrchResults'])
        holder = ''
        newXY = {'xy':[]}
        XY = {'coordinate' : []}
        b = 0
        for i in range(dengueDictLength):
            for key in sorted(dengueDict['SrchResults'][i]):
                holder += '"' + key + '"="'+ dengueDict['SrchResults'][i][key]+'",'
                holder += '\n'

        print holder
        
    except Exception, e:
        print e
    
        
        




      


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

def run():
    #config = get_config()
        
    #tokenKey=config["TokenKey"] 
        
        #validate_anconfig(TokenKey)

    #while True:
    tokenKey = 'qo/s2TnSUmfLz+32CvLC4RMVkzEFYjxqyti1KhByvEacEdMWBpCuSSQ+IFRT84QjGPBCuz/cBom8PfSm3GjEsGc8PkdEEOEr'
    onemap_connection(tokenKey)
            #date_time()
        #time.sleep(43200)
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "--scheme":
            do_scheme()
    else:
        # just request data from onemap
        while True:
            run()
            time.sleep(43200)