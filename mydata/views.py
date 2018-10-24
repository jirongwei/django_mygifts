from django.http import JsonResponse,HttpResponse

from gift import models

import json

# mydata首页
def mydata(request):

    if request.method=='POST':
        with open('giftappDATE_gift.json','r+',encoding='utf-8') as fp:
            gifts=json.load(fp)

            for gift in gifts:
                res = models.Gifts(**gift).save()






        return HttpResponse('ok')