class LeeContentDLC():
    def __init__(self) -> None:
        pass
    # def GetJsonDataFromUrl(self,inUrl=str):
    #     '''
    #     Read Git Hub Content Json
    #     '''
    #     if not inUrl or not inUrl.startswith("https"): 
    #         print("wrong url")
    #         return None

    #     urldata = urllib.urlopen(inUrl)
    #     return json.load(urldata)


    # def GetJsonArrayFromUrl(self,url=str,inKey=str):
    #     if not inKey or not url: return []

    #     urljsdata = self.GetJsonDataFromUrl(url)

    #     return urljsdata.get(inKey)
    
    # def GetContentBase64(self,inContent=str):
    #     '''
    #     Get decode Content Base64
    #     '''
    #     if not inContent or not inContent: return str()

    #     return base64.b64decode(inContent)


    # def LeeGetContentDLC(self):
    #     '''
    #     Get Download Content From Url
    #     '''
    #     global iurl
    #     urlimages = self.GetJsonArrayFromUrl(iurl)
    #     imagepaths=self.GetJsonArrayFromUrl("path")

    #     print(urlimages)
    #     pass


# LeeDLC=LeeContentDLC()
# LeeDLC.LeeGetContentDLC()
# abc =urllib.urlopen(url)
# #data=data.decode("utf-8")
# jsdata=json.load(abc)
# print(json.dumps(jsdata,indent=4))

# imgdata = urllib.urlopen(imgUrl)
# imgjson=json.load(imgdata)
# content = imgjson.get("content")
# img = base64.b64decode(content)
# with open(filename,'wb') as f:
#     f.write(img)
#     f.close()