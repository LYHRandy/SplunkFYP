import csv, sys, splunk.Intersplunk, string
from SVY21 import *
argpassed = splunk.Intersplunk.getKeywordsAndOptions()
    
results = splunk.Intersplunk.readResults(None, None, True)

# error messages
# Expected search syntax:
# sourcetype="NEADengue" | integratedanalysis chained
if len(argpassed[0]) < 1:
    splunk.Intersplunk.parseError("Arguments expected: 'chained'")
elif len(argpassed[0]) > 1:
    splunk.Intersplunk.parseError("Too Many Arguments. Arguments expected: 'chained'")

else:
    if "chained" in argpassed[0][0]:
        try:
            for resultset in results:
                NECollection = resultset['XY']
                NECollection = NECollection.replace('|',' ').replace(',',' ').split()
                NorthingsList = NECollection[1::2]
                EastingsList = NECollection[::2]
                 
                NorthingsSum = 0.0
                EastingsSum = 0.0
                 
                for x in range(len(NorthingsList)):
                    NorthingsSum += float(NorthingsList[x])
                    EastingsSum += float(EastingsList[x])
                if(len(NorthingsList) != 0):
                    NorthingListLen =  10 if len(NorthingsList) == 0 else len(NorthingsList)
                    EastingListLen = 10 if len(EastingsList) == 0 else len(EastingsList)
                     
                    NorthingMidPt = NorthingsSum / float(NorthingListLen)
                    EastingMidPt = EastingsSum / float(EastingListLen)
                     
                    (lat, lon) = SVY21().computeLatLon(NorthingMidPt, EastingMidPt) 
                    thelat = float(repr(lat))
                    thelon = float(repr(lon))
                    resultset['LATITUDE'] = thelat
                    resultset['LONGITUDE'] = thelon
                    if (1.389977 > thelat > 1.310177 and 104.036209 > thelon > 103.975269):
                        resultset['AREA'] = 'Changi'
                    elif (1.373331 > thelat > 1.347589 and 103.96394 > thelon > 103.931152):
                        resultset['AREA'] = 'Tampines'
                    elif (1.345015 > thelat > 1.314124 and 103.96085 > thelon > 103.903858):
                        resultset['AREA'] = 'Bedok'
                    elif (1.408168 > thelat > 1.353252 and 103.972152 > thelon > 103.926491):
                        resultset['AREA'] = 'Pasir Ris'
                    elif (1.369384 > thelat > 1.336091 and 103.901085 > thelon > 103.94643):
                        resultset['AREA'] = 'Paya Lebar'
                    elif (1.320302 > thelat > 1.297134 and 103.975441 > thelon > 103.875877):
                        resultset['AREA'] = 'Marine Parade'
                    elif (1.32854 > thelat > 1.310349 and 103.914474 > thelon > 103.869156):
                        resultset['AREA'] = 'Geylang'
                    elif (1.343299 > thelat > 1.32854 and 103.892845 > thelon > 103.835167):
                        resultset['AREA'] = 'Toa Payoh'
                    elif (1.421897 > thelat > 1.383456 and 103.917907 > thelon > 103.899711):
                        resultset['AREA'] = 'Punggol'
                    elif (1.433566 > thelat > 1.398558 and 103.887008 > thelon > 103.868469):
                        resultset['AREA'] = 'Seletar'
                    elif (1.399244 > thelat > 1.375219 and 103.908981 > thelon > 103.854049):
                        resultset['AREA'] = 'Sengkang'
                    elif (1.390664 > thelat > 1.334718 and 103.895591 > thelon > 103.873962):
                        resultset['AREA'] = 'Hougang'
                    elif (1.395126 > thelat > 1.336778 and 103.887695 > thelon > 103.855766):
                        resultset['AREA'] = 'Serangoon'
                    elif (1.396499 > thelat > 1.354282 and 103.860573 > thelon > 103.818001):
                        resultset['AREA'] = 'Ang Mo Kio'
                    elif (1.370071 > thelat > 1.341926 and 103.861603 > thelon > 103.824867):
                        resultset['AREA'] = 'Bishan'
                    elif (1.460337 > thelat > 1.42224 and 103.857483 > thelon > 103.84375):
                        resultset['AREA'] = 'Simpang'
                    elif (1.474752 > thelat > 1.433909 and 103.825897 > thelon > 103.803924):
                        resultset['AREA'] = 'Sembawang'
                    elif (1.456905 > thelat > 1.422583 and 103.801864 > thelon > 103.774429):
                        resultset['AREA'] = 'Woodlands'
                    elif (1.437342 > thelat > 103.770622 and 1.412973 > thelon > 103.826584):
                        resultset['AREA'] = 'Mandai'
                    elif (1.441803 > thelat > 1.383113 and 103.854736 > thelon > 103.808044):
                        resultset['AREA'] = 'Yishun'
                    elif (1.419494 > thelat > 1.320646 and 103.84478 > thelon > 103.770622):
                        resultset['AREA'] = 'Central Water Catchment'
                    elif (1.263325 > thelat > 1.236553 and 103.870872 > thelon > 103.806869):
                        resultset['AREA'] = 'Sentosa'
                    elif (1.292672 > thelat > 1.25955 and 103.878281 > thelon > 103.79657):
                        resultset['AREA'] = 'Bukit Merah'
                    elif (1.310692 > thelat > 1.250454 and 103.811161 > thelon > 103.769619):
                        resultset['AREA'] = 'Queenstown'
                    elif (1.347246 > thelat > 1.308118 and 103.813564 > thelon > 103.764469):
                        resultset['AREA'] = 'Bukit Timah'
                    elif (1.323906 > thelat > 1.294217 and 103.829529 > thelon > 103.802578):
                        resultset['AREA'] = 'Tanglin'
                    elif (1.308289 > thelat > 1.292157 and 103.84103 > thelon > 103.824551):
                        resultset['AREA'] = 'Orchard'
                    elif (1.28821 > thelat > 1.259893 and 103.880684 > thelon > 103.833649):
                        resultset['AREA'] = 'Marina South'
                    elif (1.297306 > thelat > 1.281345 and 103.907806 > thelon > 103.866264):
                        resultset['AREA'] = 'Marina East'
                    elif (1.339523 > thelat > 1.312923 and 103.85133 > thelon > 103.819401):
                        resultset['AREA'] = 'Novena'
                    elif (1.329055 > thelat > 1.296276 and 103.88446 > thelon > 103.844635):
                        resultset['AREA'] = 'Kallang'
                    elif (1.342269 > thelat > 1.291128 and 103.771335 > thelon > 103.748848):
                        resultset['AREA'] = 'Clementi'
                    elif (1.353252 > thelat > 1.298336 and 103.756401 > thelon > 103.72121):
                        resultset['AREA'] = 'Jurong East'
                    elif (1.36252 > thelat > 1.331972 and 103.72945 > thelon > 103.678295):
                        resultset['AREA'] = 'Jurong West'
                    elif (1.327167 > thelat > 1.304857 and 103.719494 > thelon > 103.684475):
                        resultset['AREA'] = 'Boon Lay'
                    elif (1.326481 > thelat > 1.302111 and 103.697521 > thelon > 103.658211):
                        resultset['AREA'] = 'Pioneer'
                    elif (1.343814 > thelat > 1.208063 and 103.661129 > thelon > 103.602592):
                        resultset['AREA'] = 'Tuas'
                    elif (1.293187 > thelat > 1.228486 and 103.738548 > thelon > 103.657009):
                        resultset['AREA'] = 'Jurong Island'
                    elif (1.237926 > thelat > 1.172709 and 103.807213 > thelon > 103.709537):
                        resultset['AREA'] = 'Ring of islands'
                    elif (1.376935 > thelat > 1.350163 and 103.744186 > thelon > 103.707107):
                        resultset['AREA'] = 'Tenga'
                    elif (1.426359 > thelat > 1.329226 and 103.73423 > thelon > 103.642906):
                        resultset['AREA'] = 'Western Catchment Area'
                    elif (1.4521 > thelat > 1.41366 and 103.734573 > thelon > 103.698181):
                        resultset['AREA'] = 'Lim Chu Kang'
                    elif (1.402677 > thelat > 1.373846 and 103.758606 > thelon > 103.734916):
                        resultset['AREA'] = 'Choa Chua Kang'
                    elif (1.441117 > thelat > 1.394096 and 103.771995 > thelon > 103.740066):
                        resultset['AREA'] = 'Sungei Kadut'
                    elif (1.387918 > thelat > 1.340896 and 103.789161 > thelon > 103.754143):
                        resultset['AREA'] = 'Bukit Panjang'
                    elif (1.374876  > thelat > 1.343299 and 103.777832 > thelon > 103.730797):
                        resultset['AREA'] = 'Bukit Batok'
                    else:
                        resultset['AREA'] = 'Others'
        except Exception, e:
            splunk.Intersplunk.parseError("Error detected. Hint: Check that data source has XY! Error Message Dump: " + str(e))
    else:
        splunk.Intersplunk.parseError("Check case and typos in argument. Argument expected: 'chained'")
splunk.Intersplunk.outputResults(results)        # Pass result back to SPLUNK