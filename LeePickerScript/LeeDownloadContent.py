'''Python2.7.11 Maya2020'''
import json
import urllib,json,base64,urllib2
import os

#github api url rate api 5000 call per hour 80 call per mins
githuburl='https://api.github.com/repos/MrLeeTa/icontemp/git/trees/master?recursive=1'
#gitlab api url rate api
'''
api url gitlab https://gitlab.com/api/v4/projects/65502564/repository/tree?recursive=true&path=Config
api file url gitlab https://gitlab.com/api/v4/projects/61603606/repository/files/Config%2FDefaultEngine%2Eini?ref=main
'''
gitlaburl='https://gitlab.com/api/v4/projects/65506411/repository/tree?recursive=true'
gitlabfile=str('https://gitlab.com/api/v4/projects/65502564/repository/files/{folder}%2F{filename}%2E{extention}?ref=main')
api_base_url='https://api.onedrive.com/v1.0/'

#imgUrl='https://api.github.com/repos/MrLeeTa/icontemp/git/blobs/ad199c18e92d8dd5fd514a327095c9c24c8b5aa1'
'''Root Folder'''
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

    def LeeGetContentFromGithubDLC(self,inRootFolder="",url=""):
        '''
        Get Download Content From Url
        '''
        if inRootFolder=="" or inRootFolder is None or not url: 
            print("download fail wrong inRootFolder Path..")
            return
        
        #get json array from github folder
        urltrees = self.GetJsonArrayFromUrl(url,"tree")

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
    
    def LeeGetContentFromGitLabDLC(self,inRootFolder="",inurl=""):
        '''
        Get Download Content From Url
        '''
        if inRootFolder=="" or inRootFolder is None or not inurl: 
            print("download fail wrong inRootFolder Path..")
            return

        ##Authorization: Bearer
        # request = urllib2.Request(inurl,iDATA)
        # print(request)
        #base64string = base64.encodestring('%s:%s' % (KEY, SECRET)).replace('\n', '')
        #urldata= urllib.urlopen('https://gitlab.com/api/v4/projects/65502564/repository/tree?recursive=true')
        #print(result)

        # oauthUrl="https://mygitlabinstance.com/api/v4/user"
        # pwmgr= urllib2.HTTPPasswordMgrWithDefaultRealm()
        # pwmgr.add_password(None,oauthUrl,"leetdvn225","leM!nhduy1203")
        # Oauth=urllib2.HTTPBasicAuthHandler(pwmgr)
        # opener = urllib2.build_opener(Oauth)
        # urllib2.install_opener(opener)

        # request = urllib2.Request("http://gitlab.com/v4/user")
        # username='leetdvn225@gmail.com'
        # pw='leM!nhduy1203'
        # base64string = base64.encodestring('%s:%s'%(username,pw)).replace('\n', '')
        # request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib.urlopen(nUrl)
        jsdata= json.load(result)
        print(jsdata)
        # response = urllib2.urlopen(inurl)
        # url = response.read().strip()
        # request = urllib2.Request(inurl,iDATA,header)
        # result = urllib.urlopen(request)
        #print("Check Url : ",url)


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

'''
git hub get url
# LeeDLC=LeeContentDLC()
# LeeDLC.LeeGetContentFromGithubDLC(icondir,githuburl)
'''
#LeeDLC.LeeGetContentFromGitLabDLC(icondir,gitlaburl)

#print("DLC runing")

authority='https://login.microsoftonline.com/consumers/'

headers= {
    'Authorization': 'Bearer' + access_token
}

folder_id=''
target_dir=''


# username='leetdvn225@gmail.com'

file_name="C:/Users/leepl/OneDrive/Documents/maya/2020/prefs/icons/bcd.txt"

params = {
          'grant_type': 'refresh_token', 
          'client_id': APPLICATION_ID,
          'refresh_token': CLIENT_SECRET
         }
response = urllib2.Request('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=params)
new_refresh_token=response.get_data()["refresh_token"]

# Download the file
responseDownload = urllib2.Request('https://graph.microsoft.com/v1.0/me/drive/root:LeeTdvn_CV2022:content',headers=headers)
print(responseDownload.get_data())
# with open(file_name, 'wb') as file:
#     file.write(responseDownload)
# access_token = response.json()['access_token']
# new_refresh_token = response.json()['refresh_token']