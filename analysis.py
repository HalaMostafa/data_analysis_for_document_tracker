from data_processing import dataProcessing



class documentTrackerAnalysis:
    def __init__(self,userId:str,documentId:str,df):
        self.userId = userId
        self.documentId = documentId
        self.df= df
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
        self.possibleMessages = {
            "noAlsoLikeData":"Readers of this document don't read other documents",
        }
    def checkDocumentIdStatus(self,display,fileName):
        """checks if document id exist in the file
        """
        if self.documentId not in list(self.df["env_doc_id"].unique()):
            display.log("can't find"+self.documentId+"in"+fileName)
            return False
        else:
            return True

    def checkUserIdStatus(self,display,fileName):
        """checks if user id exist in the file
        """
        if self.userId not in list(self.df["visitor_uuid"].unique()):
            display.log("can't find"+self.userId+"in"+fileName)
            return False
        else:
            return True


    def getViewsByCountryContinents(self,countcolumn:str):
        """analyse, for a given document, from which countries and
        continents the document has been viewed
        - Args:
            - countcolumn:(string)  country or continent
        - return pandas series 
        """
        #filter df by document id self.df["env_doc_id"]
        filtereddf = self.df[self.df["env_doc_id"]==self.documentId]
        if countcolumn == "country":
            # create country column to groupby it 
            filtereddf["country"] = filtereddf["visitor_country"].apply(lambda x:self.country_to_continent[x])
            count = filtereddf["country"].value_counts()
        elif countcolumn =="continent":
            count = filtereddf["visitor_country"].value_counts()
        return count

    # def getViewsByBrowser(self):
    #     """examine the visitor useragent field and count the number of
    #     occurrences for each value in the input file.
    #     """

    def getTopTenUsers(self):
        """For each user, the total time spent reading documents. The top 10 readers,
        based on this analysis,get top 10 users whose the total time spent reading documents.
        - Args:
            -df[['visitor_uuid','event_readtime']]
        - return list of to 10 user ids whose spent most time 
        """
        readEvent = self.df[self.df['env_type']=='reader']
        readTimePerUser = readEvent.groupby('visitor_uuid')['event_readtime'].sum().sort_values(ascending=False)
        topTen = readTimePerUser.iloc[:10]
        return list(topTen.index)

    def getReaders(self):
        """In order to calculate Also Likes
        this function  will do the first taske
        it will returns list of all visitor UUIDs of readers of given document
        """
        return list(self.df["visitor_uuid"][self.df["env_doc_id"] == self.documentId].unique())

    def getDocuments(self):
        """returns all document UUIDs that have been read by each given visitor.
        """
        users = self.getReaders() #list of all usersIds who had the given documentId
        filteredDf = self.df[(self.df["visitor_uuid"].isin(users))&(self.df["env_doc_id"]!=self.documentId)]#other documents had been read by specific users
        return filteredDf.groupby('env_doc_id')['visitor_uuid'].value_counts().reset_index(name= "count").drop(columns = ["count"])

    def sortDocuments(self,N=10):
        """return a list of “liked” documents,
        sorted by the sorting function parameter
        - Args:
            -   N (int) top N documents default 10
        """
        documentToReaders = self.getDocuments()
        if  len(documentToReaders)!=0:# check if there is no also likes
            # count reader per document to get the top N (top10)
            documentcount = documentToReaders.groupby("env_doc_id")["env_doc_id"].count().reset_index(name="docCount")
            documentToReaders = documentToReaders.merge(documentcount, how="left", on="env_doc_id").sort_values(by="docCount",ascending = False)
        return documentToReaders.head(N)#get top 10 documnets
