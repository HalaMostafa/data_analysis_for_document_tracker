import httpagentparser
import matplotlib.pyplot as plt
import numpy as np
from pandas import json_normalize
from tkinter import messagebox
from charts import *


class documentTrackerAnalysis:
    def __init__(self,df, userId:str,documentId:str,):
        self.userId = userId
        self.documentId = documentId
        self.df = df
        self.country_to_continent = {
            'AF': 'Asia',
            'AX': 'Europe',
            'AL': 'Europe',
            'DZ': 'Africa',
            'AS': 'Oceania',
            'AD': 'Europe',
            'AO': 'Africa',
            'AI': 'North America',
            'AQ': 'Antarctica',
            'AG': 'North America',
            'AR': 'South America',
            'AM': 'Asia',
            'AW': 'North America',
            'AU': 'Oceania',
            'AT': 'Europe',
            'AZ': 'Asia',
            'BS': 'North America',
            'BH': 'Asia',
            'BD': 'Asia',
            'BB': 'North America',
            'BY': 'Europe',
            'BE': 'Europe',
            'BZ': 'North America',
            'BJ': 'Africa',
            'BM': 'North America',
            'BT': 'Asia',
            'BO': 'South America',
            'BQ': 'North America',
            'BA': 'Europe',
            'BW': 'Africa',
            'BV': 'Antarctica',
            'BR': 'South America',
            'IO': 'Asia',
            'VG': 'North America',
            'BN': 'Asia',
            'BG': 'Europe',
            'BF': 'Africa',
            'BI': 'Africa',
            'KH': 'Asia',
            'CM': 'Africa',
            'CA': 'North America',
            'CV': 'Africa',
            'KY': 'North America',
            'CF': 'Africa',
            'TD': 'Africa',
            'CL': 'South America',
            'CN': 'Asia',
            'CX': 'Asia',
            'CC': 'Asia',
            'CO': 'South America',
            'KM': 'Africa',
            'CD': 'Africa',
            'CG': 'Africa',
            'CK': 'Oceania',
            'CR': 'North America',
            'CI': 'Africa',
            'HR': 'Europe',
            'CU': 'North America',
            'CW': 'North America',
            'CY': 'Asia',
            'CZ': 'Europe',
            'DK': 'Europe',
            'DJ': 'Africa',
            'DM': 'North America',
            'DO': 'North America',
            'EC': 'South America',
            'EG': 'Africa',
            'SV': 'North America',
            'GQ': 'Africa',
            'ER': 'Africa',
            'EE': 'Europe',
            'ET': 'Africa',
            'FO': 'Europe',
            'FK': 'South America',
            'FJ': 'Oceania',
            'FI': 'Europe',
            'FR': 'Europe',
            'GF': 'South America',
            'PF': 'Oceania',
            'TF': 'Antarctica',
            'GA': 'Africa',
            'GM': 'Africa',
            'GE': 'Asia',
            'DE': 'Europe',
            'GH': 'Africa',
            'GI': 'Europe',
            'GR': 'Europe',
            'GL': 'North America',
            'GD': 'North America',
            'GP': 'North America',
            'GU': 'Oceania',
            'GT': 'North America',
            'GG': 'Europe',
            'GN': 'Africa',
            'GW': 'Africa',
            'GY': 'South America',
            'HT': 'North America',
            'HM': 'Antarctica',
            'VA': 'Europe',
            'HN': 'North America',
            'HK': 'Asia',
            'HU': 'Europe',
            'IS': 'Europe',
            'IN': 'Asia',
            'ID': 'Asia',
            'IR': 'Asia',
            'IQ': 'Asia',
            'IE': 'Europe',
            'IM': 'Europe',
            'IL': 'Asia',
            'IT': 'Europe',
            'JM': 'North America',
            'JP': 'Asia',
            'JE': 'Europe',
            'JO': 'Asia',
            'KZ': 'Asia',
            'KE': 'Africa',
            'KI': 'Oceania',
            'KP': 'Asia',
            'KR': 'Asia',
            'KW': 'Asia',
            'KG': 'Asia',
            'LA': 'Asia',
            'LV': 'Europe',
            'LB': 'Asia',
            'LS': 'Africa',
            'LR': 'Africa',
            'LY': 'Africa',
            'LI': 'Europe',
            'LT': 'Europe',
            'LU': 'Europe',
            'MO': 'Asia',
            'MK': 'Europe',
            'MG': 'Africa',
            'MW': 'Africa',
            'MY': 'Asia',
            'MV': 'Asia',
            'ML': 'Africa',
            'MT': 'Europe',
            'MH': 'Oceania',
            'MQ': 'North America',
            'MR': 'Africa',
            'MU': 'Africa',
            'YT': 'Africa',
            'MX': 'North America',
            'FM': 'Oceania',
            'MD': 'Europe',
            'MC': 'Europe',
            'MN': 'Asia',
            'ME': 'Europe',
            'MS': 'North America',
            'MA': 'Africa',
            'MZ': 'Africa',
            'MM': 'Asia',
            'NA': 'Africa',
            'NR': 'Oceania',
            'NP': 'Asia',
            'NL': 'Europe',
            'NC': 'Oceania',
            'NZ': 'Oceania',
            'NI': 'North America',
            'NE': 'Africa',
            'NG': 'Africa',
            'NU': 'Oceania',
            'NF': 'Oceania',
            'MP': 'Oceania',
            'NO': 'Europe',
            'OM': 'Asia',
            'PK': 'Asia',
            'PW': 'Oceania',
            'PS': 'Asia',
            'PA': 'North America',
            'PG': 'Oceania',
            'PY': 'South America',
            'PE': 'South America',
            'PH': 'Asia',
            'PN': 'Oceania',
            'PL': 'Europe',
            'PT': 'Europe',
            'PR': 'North America',
            'QA': 'Asia',
            'RE': 'Africa',
            'RO': 'Europe',
            'RU': 'Europe',
            'RW': 'Africa',
            'BL': 'North America',
            'SH': 'Africa',
            'KN': 'North America',
            'LC': 'North America',
            'MF': 'North America',
            'PM': 'North America',
            'VC': 'North America',
            'WS': 'Oceania',
            'SM': 'Europe',
            'ST': 'Africa',
            'SA': 'Asia',
            'SN': 'Africa',
            'RS': 'Europe',
            'SC': 'Africa',
            'SL': 'Africa',
            'SG': 'Asia',
            'SX': 'North America',
            'SK': 'Europe',
            'SI': 'Europe',
            'SB': 'Oceania',
            'SO': 'Africa',
            'ZA': 'Africa',
            'GS': 'Antarctica',
            'SS': 'Africa',
            'ES': 'Europe',
            'LK': 'Asia',
            'SD': 'Africa',
            'SR': 'South America',
            'SJ': 'Europe',
            'SZ': 'Africa',
            'SE': 'Europe',
            'CH': 'Europe',
            'SY': 'Asia',
            'TW': 'Asia',
            'TJ': 'Asia',
            'TZ': 'Africa',
            'TH': 'Asia',
            'TL': 'Asia',
            'TG': 'Africa',
            'TK': 'Oceania',
            'TO': 'Oceania',
            'TT': 'North America',
            'TN': 'Africa',
            'TR': 'Asia',
            'TM': 'Asia',
            'TC': 'North America',
            'TV': 'Oceania',
            'UG': 'Africa',
            'UA': 'Europe',
            'AE': 'Asia',
            'GB': 'Europe',
            'US': 'North America',
            'UM': 'Oceania',
            'VI': 'North America',
            'UY': 'South America',
            'UZ': 'Asia',
            'VU': 'Oceania',
            'VE': 'South America',
            'VN': 'Asia',
            'WF': 'Oceania',
            'EH': 'Africa',
            'YE': 'Asia',
            'ZM': 'Africa',
            'ZW': 'Africa'
        }

    def getViewsByCountryContinents(self,countcolumn:str,messagebox=messagebox):
        """analyse, for a given document, from which countries and
        continents the document has been viewed
        - Args:
            - countcolumn:(string)  country or continent
        - return pandas series 
        """
        #check if doc id is valid
        if len(self.documentId) == 0:
            messagebox.showinfo("Warning","Enter the Subject Document ID")
        else:    
            try:
        #filter df by document id self.df["env_doc_id"]
                filtereddf = self.df[self.df["env_doc_id"]==self.documentId]
                if countcolumn == "country":
                    # create country column to groupby it 
                    filtereddf["country"] = filtereddf["visitor_country"].apply(lambda x:self.country_to_continent[x])
                    count = filtereddf["country"].value_counts()
                elif countcolumn =="continent":
                    count = filtereddf["visitor_country"].value_counts()
                # return count
                return createHistogram(x_Axis=list(count.index),y_axis=list(count),x_label=countcolumn,y_label="Count",title="Views By Country\Contenient")
            except Exception:
                messagebox.showinfo("wARNING","Enter a valid Subject Document Id") ##EDIT THIS LINE

    def getTopTenUsers(self):
        """For each user, the total time spent reading documents. The top 10 readers,
        based on this analysis,get top 10 users whose the total time spent reading documents.
        - Args:
            -df[['visitor_uuid','event_readtime']]
        - return list of to 10 user ids whose spent most time 
        """
        readEvent = self.df.loc[self.df['env_type']=='reader'].copy()
        readTimePerUser = readEvent.groupby('visitor_uuid')['event_readtime'].sum().sort_values(ascending=False)
        topTen =  readTimePerUser.iloc[:10] #topTen
        return createHistogram(x_Axis=list(topTen.index),y_axis=list(topTen),x_label="User ID",y_label="Total Reading Time",title="Top Ten Users",rotate=True)


    
    # GET VIEWS BY BROWSER:
    def getBrowesrData(self):
        """return pandas data frame contains all browser informations from userAgent
        the df will contain the followwing columns:
        ['bot', 'platform.name', 'platform.version', 'os.name', 'os.version',
       'browser.name', 'browser.version', 'dist.name', 'dist.version',
       'flavor.name', 'flavor.version']
        """
        browser = self.df["visitor_useragent"].apply(lambda x: httpagentparser.detect(x))
        return json_normalize(data =browser)

    def get_full_browser(self):
        """
        browser by version
        """
        browesrData =  self.getBrowesrData()
        browesrData["browserNameVersion"] = browesrData["browser.name"]+browesrData["browser.version"]
        browsercount = browesrData["browserNameVersion"].value_counts()
        browsercount = browsercount.iloc[:10]
        # return browsercount
        return createHistogram(x_Axis=list(browsercount.index),y_axis=list(browsercount),x_label="Browser Name",y_label="Browser Count",title="Top Ten Browser Per Version Count",rotate=True)
    #Getting full browser list without any splitting                    
    def get_browser(self):
        """get views by Browser
        """
        browesrData =  self.getBrowesrData()
        browsercount = browesrData["browser.name"].dropna().value_counts()

        return createHistogram(
            x_Axis=list(browsercount.index),
            y_axis=list(browsercount),
            x_label="Browser Name",
            y_label="Browser Count",
            title="Browser Count",rotate=True)
    

    def getOSPerBrowser(self):
        """ get Operating system used by reader
        """
        browesrData =  self.getBrowesrData()
        osPerBrowser = browesrData.groupby("browser.name")["os.name"].value_counts().unstack().fillna(0).reset_index()
        #drop columns contain zero values
        colsToDrop = [col for col in osPerBrowser.columns if col != "browser.name" and sum(osPerBrowser[col]) == 0]
        osPerBrowser = osPerBrowser.drop(columns=colsToDrop)
        osPerBrowser.plot(x="browser.name",kind='bar',stacked=True,title='Operating System Per Browser',legend=True)
        plt.xticks(rotation = 90)
        plt.tight_layout()
        plt.grid(True,axis='y')
        plt.show()

        

