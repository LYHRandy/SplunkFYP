def onemap_connection():
    try:
        totalPopulation = {"PopulationQuery" : 
                           [{'Area' : 'Woodlands','totalPopulation' : '247700', 'age00-04' : '13100', 'age05-09' : '15800', 'age10-14' : '20300', 'age15-19' : '21300', 'age20-24' : '18400', 'age25-29' : '17000', 'age30-34' : '19000', 'age35-39' : '20400', 'age40-44' : '22800', 'age45-49' : '22600', 'age50-54' : '19100', 'age55-59' : '14200', 'age60-64' : '2600',  'Over65' : '14400', 'malePopulation' : '124800', 'female' : '122900'}, 
                            {'Area' : 'Sembawang', 'totalPopulation' : '73300', 'age00-04' : '5100', 'age05-09' : '5300', 'age10-14' : '5200', 'age15-19' : '4300', 'age20-24' : '4700', 'age25-29' : '5000', 'age30-34' : '7100', 'age35-39' : '7900', 'age40-44' : '6700', 'age45-49' : '5800', 'age50-54' : '5200', 'age55-59' : '4100', 'age60-64' : '9300',  'Over65' : '4300', 'malePopulation' : '36400', 'female' : '36900'}, 
                            {'Area' : 'Yishun', 'totalPopulation' : '187300', 'age00-04' : '8600', 'age05-09' : '9600', 'age10-14' : '11100', 'age15-19' : '13100', 'age20-24' : '15600', 'age25-29' : '14500', 'age30-34' : '14400', 'age35-39' : '14200', 'age40-44' : '14200', 'age45-49' : '16500', 'age50-54' : '16700', 'age55-59' : '14100', 'age60-64' : '10000',  'Over65' : '14700', 'malePopulation' : '92900', 'female' : '94400'},
                            {'Area' : 'Mandai','totalPopulation' : '2600', 'age00-04' : '200', 'age05-09' : '200', 'age10-14' : '200', 'age15-19' : '200', 'age20-24' : '200', 'age25-29' : '200', 'age30-34' : '200', 'age35-39' : '200', 'age40-44' : '200', 'age45-49' : '200', 'age50-54' : '200', 'age55-59' : '200', 'Over65' : '200', 'malePopulation' : '1300', 'female' : '1300'},
                            {'Area' : 'Ang Mo Kio', 'totalPopulation' : '178800', 'age00-04' : '7500', 'age05-09' : '8100', 'age10-14' : '9100', 'age15-19' : '10000', 'age20-24' : '10800', 'age25-29' : '11800', 'age30-34' : '14100', 'age35-39' : '14300', 'age40-44' : '13500', 'age45-49' : '14500', 'age50-54' : '14300', 'age55-59' : '14000', 'age60-64' : '12700',  'Over65' : '24100', 'malePopulation' : '86600', 'female' : '92200'}, 
                            {'Area' : 'Serangoon', 'totalPopulation' :  '123400', 'age00-04' : '4600', 'age05-09' : '5700', 'age10-14' : '7200', 'age15-19' : '8800', 'age20-24' : '9700', 'age25-29' : '8300', 'age30-34' : '8000', 'age35-39' : '8300', 'age40-44' : '8900', 'age45-49' : '10000', 'age50-54' : '11000', 'age55-59' : '10600', 'age60-64' : '8100',  'Over65' : '14200', 'malePopulation' : '59900', 'female' : '63500'}, 
                            {'Area' : 'SengKang', 'totalPopulation': '177800', 'age00-04' : '13600', 'age05-09' : '13000', 'age10-14' : '11600', 'age15-19' : '10400', 'age20-24' : '10100', 'age25-29' : '11900', 'age30-34' : '18800', 'age35-39' : '19400', 'age40-44' : '15500', 'age45-49' : '13100', 'age50-54' : '12600', 'age55-59' : '10100', 'age60-64' : '7100',  'Over65' : '10600', 'malePopulation' : '87900', 'female' : '89900'}, 
                            {'Area' : 'Punggol','totalPopulation' : '74500', 'age00-04' : '7700', 'age05-09' : '6300', 'age10-14' : '4200', 'age15-19' : '3100', 'age20-24' : '3000', 'age25-29' : '5500', 'age30-34' : '9700', 'age35-39' : '10100', 'age40-44' : '6500', 'age45-49' : '4700', 'age45-49' : '4700', 'age50-54' : '3900', 'age55-59' : '3300', 'age60-64' : '2600',  'Over65' : '3900', 'malePopulation' : '36800', 'female' : '37700'},
                            {'Area' : 'Pasir Ris','totalPopulation' : '135800', 'age00-04' : '21000', 'age05-09' : '7700', 'age10-14' : '11000', 'age15-19' : '14100', 'age20-24' : '10800', 'age25-29' : '7200', 'age30-34' : '8200', 'age35-39' : '9700', 'age40-44' : '11500', 'age45-49' : '14900', 'age45-49' : '14900', 'age50-54' : '12000', 'age55-59' : '8400', 'age60-64' : '5500',  'Over65' : '8700', 'malePopulation' : '67300', 'female' : '68500'}, 
                            {'Area' : 'Changi','totalPopulation' : '2500', 'age00-04' : '200', 'age05-09' : '200', 'age10-14' : '200', 'age15-19' : '200', 'age20-24' : '200', 'age25-29' : '100', 'age30-34' : '200', 'age35-39' : '300', 'age40-44' : '200', 'age45-49' : '200', 'age50-54' : '200', 'age55-59' : '100', 'Over65' : '200', 'malePopulation' : '1200', 'female' : '1300'}, 
                            {'Area' : 'Hougang', 'totalPopulation' : '217500', 'age00-04' : '8500', 'age05-09' : '10500', 'age10-14' : '13300', 'age15-19' : '16100', 'age20-24' : '17000', 'age25-29' : '14800', 'age30-34' : '14600', 'age35-39' : '15700', 'age40-44' : '16300', 'age45-49' : '19000', 'age50-54' : '19900', 'age55-59' : '17400', 'age60-64' : '12800',  'Over65' : '21600', 'malePopulation' : '107100', 'female' : '110400'}, 
                            {'Area' : 'Toa Payoh', 'totalPopulation' : '126300', 'age00-04' : '5100', 'age05-09' : '5700', 'age10-14' : '6300', 'age15-19' : '7300', 'age20-24' : '7500', 'age25-29' : '7600', 'age30-34' : '8900', 'age35-39' : '10000', 'age40-44' : '9800', 'age45-49' : '10100', 'age50-54' : '10300', 'age55-59' : '9500', 'age60-64' : '8300',  'Over65' : '19900', 'malePopulation' : '60700', 'female' : '65600'}, 
                            {'Area' : 'Bishan', 'totalPopulation' : '92800', 'age00-04' : '3900', 'age05-09' : '4700', 'age10-14' : '5300', 'age15-19' : '6500', 'age20-24' : '7200', 'age25-29' : '5700', 'age30-34' : '6200', 'age35-39' : '6900', 'age40-44' : '7200', 'age45-49' : '7700', 'age50-54' : '8100', 'age55-59' : '7400', 'age60-64' : '5900',  'Over65' : '10100', 'malePopulation' : '45200', 'female' : '47600'}, 
                            {'Area' : 'Kallang', 'totalPopulation' : '102700', 'age00-04' : '4600', 'age05-09' : '4600', 'age10-14' : '4700', 'age15-19' : '5000', 'age20-24' : '5500', 'age25-29' : '6400', 'age30-34' : '8200', 'age35-39' : '8800', 'age40-44' : '8500', 'age45-49' : '7900', 'age50-54' : '8300', 'age55-59' : '7600', 'age60-64' : '7000',  'Over65' : '15600', 'malePopulation' : '51300', 'female' : '51400'}, 
                            {'Area' : 'Geylang', 'totalPopulation' : '119500', 'age00-04' : '5200', 'age05-09' : '5500', 'age10-14' : '6100', 'age15-19' : '7200', 'age20-24' : '8000', 'age25-29' : '8000', 'age30-34' : '9000', 'age35-39' : '9500', 'age40-44' : '8900', 'age45-49' : '9600', 'age50-54' : '10000', 'age55-59' : '9300', 'age60-64' : '7500',  'Over65' : '15700', 'malePopulation' : '59300', 'female' : '60200'}, 
                            {'Area' : 'Marine Parade','totalPopulation' : '48400', 'age00-04' : '13100', 'age05-09' : '15800', 'age10-14' : '20300', 'age15-19' : '21300', 'age20-24' : '18400', 'age25-29' : '2400', 'age30-34' : '3300', 'age35-39' : '4200', 'age40-44' : '4400', 'age45-49' : '3800', 'age50-54' : '3600', 'age55-59' : '3300', 'age60-64' : '3000',  'Over65' : '7200', 'malePopulation' : '22800', 'female' : '25600'}, 
                            {'Area' : 'Bedok','totalPopulation' : '295400', 'age00-04' : '12800', 'age05-09' : '14400', 'age10-14' : '16600', 'age15-19' : '19100', 'age20-24' : '20900', 'age25-29' : '19500', 'age30-34' : '21200', 'age35-39' : '22500', 'age40-44' : '22300', 'age45-49' : '23600', 'age50-54' : '24700', 'age55-59' : '22900', 'age60-64' : '19600',  'Over65' : '35300', 'malePopulation' : '144500', 'female' : '150900'}, 
                            {'Area' : 'Tampines','totalPopulation' : '259900', 'age00-04' : '11500', 'age05-09' : '13000', 'age10-14' : '16500', 'age15-19' : '20800', 'age20-24' : '21700', 'age25-29' : '18800', 'age30-34' : '18800', 'age35-39' : '18300', 'age40-44' : '19200', 'age45-49' : '22300', 'age50-54' : '23700', 'age55-59' : '20500', 'age60-64' : '14200',  'Over65' : '20600', 'malePopulation' : '127800', 'female' : '132100'}, 
                            {'Area' : 'Novena', 'totalPopulation' : '47100', 'age00-04' : '2400', 'age05-09' : '2600', 'age10-14' : '2500', 'age15-19' : '2600', 'age20-24' : '2700', 'age25-29' : '2600', 'age30-34' : '3400', 'age35-39' : '4100', 'age40-44' : '4200', 'age45-49' : '4000', 'age50-54' : '3600', 'age55-59' : '3200', 'age60-64' : '2700',  'Over65' : '6500', 'malePopulation' : '22700', 'female' : '24400'}, 
                            {'Area' : 'Newton', 'totalPopulation' : '6400', 'age00-04' : '800', 'age05-09' : '400', 'age10-14' : '800', 'age15-19' : '800', 'age20-24' : '800', 'age25-29' : '800', 'age30-34' : '400', 'age35-39' : '700', 'age40-44' : '700', 'age45-49' : '600', 'age50-54' : '600', 'age55-59' : '400', 'age60-64' : '400',  'Over65' : '800', 'malePopulation' : '2900', 'female' : '3500'}, 
                            {'Area' : 'Bukit Timah', 'totalPopulation'  : '72000', 'age00-04' : '3200', 'age05-09' : '4600', 'age10-14' : '4600', 'age15-19' : '5100', 'age20-24' : '5000', 'age25-29' : '3700', 'age30-34' : '3800', 'age35-39' : '5500', 'age40-44' : '6500', 'age45-49' : '6200', 'age50-54' : '5700', 'age55-59' : '5100', 'age60-64' : '4400',  'Over65' : '8600', 'malePopulation' : '33600', 'female' : '38400'}, 
                            {'Area' : 'Queenstown', 'totalPopulation'  : '97900', 'age00-04' : '4500', 'age05-09' : '4300', 'age10-14' : '4600', 'age15-19' : '4900', 'age20-24' : '5200', 'age25-29' : '5900', 'age30-34' : '7700', 'age35-39' : '8400', 'age40-44' : '8100', 'age45-49' : '8000', 'age50-54' : '7200', 'age55-59' : '6700', 'age60-64' : '6400',  'Over65' : '16000', 'malePopulation' : '46400', 'female' : '51500'}, 
                            {'Area' : 'Clementi', 'totalPopulation' : '91200', 'age00-04' : '4200', 'age05-09' : '4300', 'age10-14' : '4600', 'age15-19' : '4800', 'age20-24' : '5100', 'age25-29' : '5800', 'age30-34' : '7300', 'age35-39' : '7700', 'age40-44' : '7300', 'age45-49' : '7500', 'age50-54' : '6700', 'age55-59' : '6900', 'age60-64' : '6900',  'Over65' : '12100', 'malePopulation' : '43800', 'female' : '47400'}, 
                            {'Area' : 'Jurong East', 'totalPopulation' : '86400', 'age00-04' : '3600', 'age05-09' : '4300', 'age10-14' : '5000', 'age15-19' : '5400', 'age20-24' : '6400', 'age25-29' : '6700', 'age30-34' : '6800', 'age35-39' : '6700', 'age40-44' : '6600', 'age45-49' : '6700', 'age50-54' : '7000', 'age55-59' : '7000', 'age60-64' : '5800',  'Over65' : '8400', 'malePopulation' : '43300', 'female' : '43100'}, 
                            {'Area' : 'Jurong West', 'totalPopulation' : '271800', 'age00-04' : '15200', 'age05-09' : '16700', 'age10-14' : '17800', 'age15-19' : '19100', 'age20-24' : '19200', 'age25-29' : '20200', 'age30-34' : '24900', 'age35-39' : '24200', 'age40-44' : '22600', 'age45-49' : '22200', 'age50-54' : '20100', 'age55-59' : '18200', 'age60-64' : '13600',  'Over65' : '17800', 'malePopulation' : '138000', 'female' : '133800'}, 
                            {'Area' : 'Bukit Batok', 'totalPopulation' : '142700', 'age00-04' : '6400', 'age05-09' : '7700', 'age10-14' : '9200', 'age15-19' : '10000', 'age20-24' : '10800', 'age25-29' : '10500', 'age30-34' : '10600', 'age35-39' : '11200', 'age40-44' : '11700', 'age45-49' : '12500', 'age50-54' : '12600', 'age55-59' : '11000', 'age60-64' : '7700',  'Over65' : '10800', 'malePopulation' : '70300', 'female' : '72400'}, 
                            {'Area' : 'Bukit Panjang', 'totalPopulation' : '130900', 'age00-04' : '6700', 'age05-09' : '7800', 'age10-14' : '9000', 'age15-19' : '9700', 'age20-24' : '10700', 'age25-29' : '9100', 'age30-34' : '9600', 'age35-39' : '10600', 'age40-44' : '10500', 'age45-49' : '11100', 'age50-54' : '11200', 'age55-59' : '9100', 'age60-64' : '6300',  'Over65' : '9500', 'malePopulation' : '65300', 'female' : '65600'}, 
                            {'Area' : 'Choa Chu Kang', 'totalPopulation' : '174400', 'age00-04' : '8300', 'age05-09' : '10400', 'age10-14' : '13700', 'age15-19' : '16100', 'age20-24' : '13200', 'age25-29' : '11400', 'age30-34' : '12200', 'age35-39' : '13400', 'age40-44' : '15400', 'age45-49' : '17500', 'age50-54' : '14400', 'age55-59' : '10700', 'age60-64' : '7100',  'Over65' : '10600', 'malePopulation' : '87100', 'female' : '87300'}, 
                            {'Area' : 'Bukit Merah', 'totalPopulation' : '157500', 'age00-04' : '7800', 'age05-09' : '6900', 'age10-14' : '6900', 'age15-19' : '7300', 'age20-24' : '10700', 'age25-29' : '9600', 'age30-34' : '13000', 'age35-39' : '13700', 'age40-44' : '12000', 'age45-49' : '11700', 'age50-54' : '11800', 'age55-59' : '11700', 'age60-64' : '11200',  'Over65' : '25700', 'malePopulation' : '76800', 'female' : '80700'}, 
                            {'Area' : 'Outram', 'totalPopulation' : '21900', 'age00-04' : '1300', 'age05-09' : '800', 'age10-14' : '700', 'age15-19' : '800', 'age20-24' : '1000', 'age25-29' : '1300', 'age30-34' : '2200', 'age35-39' : '1900', 'age40-44' : '1600', 'age45-49' : '1500', 'age50-54' : '1600', 'age55-59' : '1600', 'age60-64' : '1600',  'Over65' : '4000', 'malePopulation' : '11100', 'female' : '10800'}, 
                            {'Area' : 'Singapore River','totalPopulation' : '2600', 'age00-04' : '200', 'age05-09' : '200', 'age10-14' : '100', 'age20-24' : '100', 'age25-29' : '100', 'age30-34' : '300', 'age35-39' : '400', 'age40-44' : '400', 'age45-49' : '200', 'age50-54' : '200', 'age55-59' : '200',  'Over65' : '200', 'malePopulation' : '1100', 'female' : '1500'}, 
                            {'Area' : 'River Valley','totalPopulation' : '8700', 'age00-04' : '300', 'age05-09' : '500', 'age10-14' : '500', 'age15-19' : '500', 'age20-24' : '500', 'age25-29' : '600', 'age30-34' : '700', 'age35-39' : '900', 'age40-44' : '900', 'age45-49' : '800', 'age50-54' : '700', 'age55-59' : '600', 'age60-64' : '400',  'Over65' : '900', 'malePopulation' : '3900', 'female' : '4800'}, 
                            {'Area' : 'Tanglin','totalPopulation' : '17700', 'age00-04' : '900', 'age05-09' : '1100', 'age10-14' : '1100', 'age15-19' : '1000', 'age20-24' : '900', 'age25-29' : '800', 'age30-34' : '1200', 'age35-39' : '1600', 'age40-44' : '1900', 'age45-49' : '1600', 'age50-54' : '1400', 'age55-59' : '1200', 'age60-64' : '1000',  'Over65' : '2000', 'malePopulation' : '8200', 'female' : '9500'}, 
                            {'Area' : 'Downtown Core', 'totalPopulation' : '3900', 'age00-04' : '1300', 'age05-09' : '100', 'age10-14' : '200', 'age15-19' : '200', 'age20-24' : '200', 'age25-29' : '200', 'age30-34' : '400', 'age35-39' : '400', 'age40-44' : '400', 'age45-49' : '300', 'age50-54' : '300', 'age55-59' : '200', 'age60-64' : '200',  'Over65' : '600', 'malePopulation' : '2000', 'female' : '1900'}, 
                            {'Area' : 'Rochor', 'totalPopulation' : '15100', 'age00-04' : '600', 'age05-09' : '600', 'age10-14' : '600', 'age15-19' : '600', 'age20-24' : '800', 'age25-29' : '1000', 'age30-34' : '1300', 'age35-39' : '1400', 'age40-44' : '1100', 'age45-49' : '1100', 'age50-54' : '1300', 'age55-59' : '1100', 'age60-64' : '1100',  'Over65' : '2500', 'malePopulation' : '7700', 'female' : '7400'}]}
        
        popLength = len(totalPopulation['PopulationQuery'])
        
        for i in range(popLength):
            for key in sorted(totalPopulation['PopulationQuery'][i]):
                print key, ':','"' + totalPopulation['PopulationQuery'][i][key] + '"'       
        
    except KeyError, e:
        print "Error!! Wrong Key defined! ********" , e, "***********"
        
        
if __name__ == '__main__':
    onemap_connection()
