from django.shortcuts import render
from labeling.models import Labeling as label
from labeling.models import Project as projectmanage
from labeling.models import Group as group
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from labeling.form import CreateProjectForm, addmemberForm
# Create your views here.
def labeling(request, id):
    id2 = int(request.GET.get('id2'))
    frame = id2+1
    project = projectmanage.objects.get(id=id)
    pictures = project.labeling_set.all()
    p = pictures[id2]
    if 'vehicle' in request.POST and request.POST['vehicle'] != '':
        p.choice = request.POST['vehicle']
        p.save()
        id2 += 1
        if id2 == pictures.count():
            projectmanage.objects.filter(id=id).update(state = "Checking")
            return HttpResponseRedirect("/projects/")
        else:
            return HttpResponseRedirect("/labeling/"+id+"/?id2="+str(id2))
    elif id:
        if id2 == pictures.count()-1:
            message = "按下去以上傳"
        return render(request,'labeling.html',locals())
    else:
        return HttpResponseRedirect("/projects/")

def project(request):
    user = User.objects.get(username = request.user)
    usergroup = user.group_set.all()
    return render(request,'projects.html',locals())

def createproject(request):
    if 'project_name' in request.POST and  request.POST['project_name'] !='' and request.FILES.getlist('img'):
        form = CreateProjectForm(request.POST)
        image = request.FILES.getlist('img')
        if form.is_valid():
            name = form.cleaned_data['project_name']
            description = form.cleaned_data['description']
            #date_time = datetime.datetime.now()
            projectmanage.objects.create(name = name, description = description, member = request.user, state = "Labeling")

            p = projectmanage.objects.all().order_by("-id")[0] #取得最新一筆資料的ID
            g = group.objects.create(project = p)
            g.member.add(request.user)
            for img in image:
                label.objects.create(project = p, image = img)
            form = CreateProjectForm()
            return HttpResponseRedirect("/projects/")
    else:
        form = CreateProjectForm()
    return render(request,'createProject.html',locals())

def check(request):
    projects = projectmanage.objects.filter(state = 'Checking')
    return render(request,'check.html',locals())

def checkimg(request, id):
    id2 = int(request.GET.get('id2'))
    page = int(request.GET.get('page'))
    project = projectmanage.objects.get(id=id)
    frame = project.labeling_set.filter(judge = False).count()
    pictures = project.labeling_set.all()

    p = pictures[id2]
    while(p.judge == True):
        id2 += 1
        p = pictures[id2]
    if 'judge' in request.POST and request.POST['judge'] != '':
        p.comment = request.POST['comment']
        p.judge = True if request.POST['judge']=="accept" else False
        p.save()
        id2 += 1
        page += 1
        if id2 == pictures.count():
            if project.labeling_set.filter(judge = False).count() == 0: #如果全部都通過了
                projectmanage.objects.filter(id=id).update(state = "Finish")
            else:
                projectmanage.objects.filter(id=id).update(state = "Rechecking")
            return HttpResponseRedirect("/projects/")
        else:
            return HttpResponseRedirect("/checkimg/"+id+"/?id2="+str(id2)+"&&page="+str(page))
    elif id:
        if id2 == pictures.count()-1:
            message = "按下去以回傳"
        return render(request,'checkimg.html',locals())
    else:
        return HttpResponseRedirect("/projects/")
def relabeling(request, id):
    id2 = int(request.GET.get('id2'))
    page = int(request.GET.get('page'))
    project = projectmanage.objects.get(id=id)
    frame = project.labeling_set.filter(judge = False).count()
    pictures = project.labeling_set.all()
    p = pictures[id2]
    while(p.judge == True):
        id2 += 1
        p = pictures[id2]
    if 'vehicle' in request.POST and request.POST['vehicle'] != '':
        p.choice = request.POST['vehicle']
        p.save()
        id2 += 1
        page += 1
        if id2 >= pictures.count():
            projectmanage.objects.filter(id=id).update(state = "Checking")
            return HttpResponseRedirect("/projects/")
        else:
            return HttpResponseRedirect("/relabeling/"+id+"/?id2="+str(id2)+"&&page="+str(page))
    elif id:
        if id2 == pictures.count()-1:
            message = "按下去以上傳"
        return render(request,'relabeling.html',locals())
    else:
        return HttpResponseRedirect("/projects/")

def projectOverview(request, id):
    p = projectmanage.objects.get(id=id)
    user = User.objects.get(username = request.user)
    userproject = user.project_set.all()
    return render(request,'projectOverview.html',locals())

def addMember(request, id):
    p = projectmanage.objects.get(id=id)
    g = group.objects.get(project = p)
    if 'name' in request.POST and request.POST['name'] != '':
        form = addmemberForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            try:
                n = User.objects.get(username = name)
                g.member.add(n)
            except:
                pass
            form = addmemberForm()
            return render(request,'addMember.html',locals())
    else:
        form = addmemberForm()
    return render(request,'addMember.html',locals())
def test(request):
    return render(request,'test.html',locals())
