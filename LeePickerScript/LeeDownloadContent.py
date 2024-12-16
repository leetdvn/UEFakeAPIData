import urllib
import json
import base64

#url='https://api.github.com/repos/MrLeeTa/leePicker/src/git/trees/master?recursive=1'
url='https://api.github.com/repos/MrLeeTa/icontemp/git/trees/master?recursive=1'
imgUrl='https://api.github.com/repos/MrLeeTa/icontemp/git/blobs/ad199c18e92d8dd5fd514a327095c9c24c8b5aa1'
filename='C:/Users/thang/Documents/GitHub/UEFakeAPIData/IMAGE/testImg.png'
abc =urllib.urlopen(url)
#data=data.decode("utf-8")
jsdata=json.load(abc)
print(json.dumps(jsdata,indent=4))
#print(data.decode("utf-8"))
# with open(filename,'wb') as f:
#     f.write(json.dumps(jsdata,indent=4))
#     f.close()
    #print(stat)
# jsdata = json.load(abc)
#store_list = [{'url': item['url']} for item in json_array]

# json_array = jsdata.get("tree")
# contents =[p["path"] for p in json_array]
# #print(json_array)

# #print("number : ",len(contents))
# for elm in contents:
#     print(elm)
imgdata = urllib.urlopen(imgUrl)
imgjson=json.load(imgdata)
content = imgjson.get("content")
img = base64.b64decode(content)
# with open(filename,'wb') as f:
#     f.write(img)
#     f.close()
