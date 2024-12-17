import urllib,json,base64
import os
iurl='https://api.github.com/repos/MrLeeTa/icontemp/git/trees/master?recursive=1'
#imgUrl='https://api.github.com/repos/MrLeeTa/icontemp/git/blobs/ad199c18e92d8dd5fd514a327095c9c24c8b5aa1'
iRootFolder="C:/Users/leepl/Documents/GitHub/UEFakeAPIData/IMAGE/"
icondir=str("C:/Users/{}/OneDrive/Documents/maya/2020/prefs/icons/").format(os.environ['USERNAME'])

class LeeContentDLC():
    def __init__(self):
        pass

    def GetJsonDataFromUrl(self,inUrl=str):
        '''
        Read Git Hub Content Json
        '''
        if not inUrl or not inUrl.startswith("https"): 
            print("wrong url")
            return None

        urldata = urllib.urlopen(inUrl)
        return json.load(urldata)
    
    def GetJsonArrayFromUrl(self,url,inKey):
        if not inKey or not url:
            print(inKey)
            return []

        urljsdata = self.GetJsonDataFromUrl(url)

        return urljsdata.get(inKey)
    
    def GetArrayFromJsonArray(self,inArray=[],inkey=""):
        if not inArray or not inkey: return []

        return [p.get(inkey) for p in inArray]    

    def GetContentBase64(self,inContent=str):
        '''
        Get decode Content Base64
        '''
        if not inContent or not inContent: return str()

        return base64.b64decode(inContent)

    def GetDirectoryFromFile(self,infile=str):
        if not infile or infile=="":
            print("file path can't not isEmpty")
            return ""

        infile.replace("\\","/")
        split = infile.split('/')

        directory = infile.replace(split[-1],"")
        return directory

    def LeeGetContentDLC(self,inRootFolder=""):
        '''
        Get Download Content From Url
        '''
        if inRootFolder=="" or inRootFolder is None: 
            print("download fail wrong inRootFolder Path..")
            return
        
        #get json array from github folder
        urltrees = self.GetJsonArrayFromUrl(iurl,"tree")

        #get img file path name
        imgfiles=self.GetArrayFromJsonArray(urltrees,"path")

        #all item url content data base
        urls = self.GetArrayFromJsonArray(urltrees,"url")

        for i,url in enumerate(urls):
            fpath = inRootFolder + imgfiles[i]
            if os.path.exists(fpath): continue

            dir = self.GetDirectoryFromFile(fpath)
            if not os.path.exists(dir): os.makedirs(dir,0o666)

            self.MakeFileContentFromUrl(url,fpath)

            print(str("DLC : {}").format(imgfiles[i]))
            pass
        
        print("DLC Completed..",len(urls),urltrees)

    def MakeFileContentFromUrl(self,inUrl="",inPath=""):
        if not inUrl or inUrl=="": return

        urldata = self.GetJsonDataFromUrl(inUrl)

        imgcontent = urldata.get("content")

        if imgcontent is None: return
        img = base64.b64decode(imgcontent)
        with open(inPath,'wb') as f:
            f.write(img)
            f.close()

LeeDLC=LeeContentDLC()
LeeDLC.LeeGetContentDLC(icondir)
# directory = LeeDLC.GetDirectoryFromFile(filename)

# directory += "abc/dasd/dasdad/"
# mode = 0o666
# os.makedirs(directory,mode)

