from django.http import HttpResponse
from django.shortcuts import render
import os
from bmgtk.settings import BASE_DIR
from baomiguan.models import anwserTable
#from imageDeal import readImgDict
file_path = os.path.join(BASE_DIR, 'statics/images')
def home(request):
    return render(request,"index.html")
def search(request):
    print(request)
    keyStr = request.GET.get('mykey')
    searchkey=keyStr
    print("searchkey:",searchkey)
    context={}
    # filter相当于SQL中的WHERE，可设置条件过滤结果 __icontains 忽略大小写的模糊查找
    response2 = anwserTable.objects.filter(question__icontains=searchkey).values("imgpath") 
    #print("response:",response2)
    finds=list()
    for pos in response2:
        #strpp="/images/IMG_0240.png"
        pp=pos.get('imgpath')
        strpp="/images/"+pp
        #print(strpp)
        #print(pp)
        finds.append(strpp)
        
    print(finds)
    context['imgs']=finds
    return render(request,"index.html",context)
