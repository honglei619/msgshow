# *- coding:utf-8 -*
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.utils.timezone import now, timedelta
from django.shortcuts import render_to_response
from myapp.models import Queue,Result
# Create your views here.
def show(request):
    #date = now().date() + timedelta(days=-2)  # 昨天
    #status = Queue.objects.filter(status = False)

    displayListQueue = Result.objects.filter(queue__status = False)
    #displayListQueue = Queue.objects.filter(Result__yellow_grain_rice = 8)
    #displayListQueue = Result.object.all() #取出所有结果

    displayList = displayListQueue.order_by("-inspection_creat_time") #对所有结果进行排序:按种类正序,创建时间逆序排序

    return render_to_response('show.html', {'displayList': displayList})