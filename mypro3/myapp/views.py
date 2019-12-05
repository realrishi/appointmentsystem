from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Reg,Apnt,Regd,Reply,Feed,Replyfeed
def index(request):
    return render(request,"myapp/index.html")
def plogin(request):
    return render(request,"myapp/plogin.html")
def preg(request):
    return render(request,"myapp/preg.html")
def admin(request):
    return render(request,"myapp/admin.html")
def regcode(request):
  email = request.GET["txtemail"]
  pa =    request.GET["txtpass"]
  mobile = request.GET["txtmobile"]
  address=request.GET["txtaddress"]
  date = request.GET["date"]
  obj = Reg(emailid=email,password=pa,mobileno=mobile,address=address,date=date)
  obj.save()  
  return HttpResponse("<h3>you registered successfully</h3>")

def logincode(request):
  email = request.POST["txtemail"]
  pa    = request.POST["txtpass"]
  objemail = Reg.objects.filter(emailid=email)
  objpass = Reg.objects.filter(password=pa)
  if(objemail.count()==0):
    s = "invalid emailid"
  elif(objpass.count()==0):
    s = "invalid password"  
  else:
    request.session['uid'] = email

    return redirect('userdash')
    
  return HttpResponse(s)

def apntcode(request):
  email = request.GET["txtemail"]
  at =    request.GET["txtapntto"]
  ad = request.GET["txtapntdesc"]
  date = request.GET["date"]
  time = request.GET["time"]
  obj = Apnt(emailid=email,apntto=at,apntdesc=ad,date=date,time=time)
  obj.save() 
  return HttpResponse("appointment added successfully")

def userdash(request):
	udata=request.session['uid']
	return render(request,"myapp/userdash.html",{'uid':udata}) 

def logout(request):
  del request.session['uid']
  return redirect('index')

def viewapnt(request):
  #res = Feed.objects.all()
  udata=request.session['uid']
  rdata=request.session['uid']
  res = Apnt.objects.filter(emailid=udata)
  reps = Reply.objects.filter(replyto=rdata)
  return render(request,"myapp/viewapnt.html",{'apntdata':res,'replydata':reps}) 
def editapnt(request):
  data = request.GET["apntid"]
  rec = Apnt.objects.get(id=data)
  return render(request,"myapp/editapnt.html",{'apntdata':rec}) 
def updateapntcode(request):
  data = request.GET["txtid"]
  s = Apnt.objects.get(id=data)
  s.apntto=request.GET["txtapntto"]
  s.apntdesc=request.GET["txtapntdesc"]
  s.date=request.GET["date"]
  s.time=request.GET["time"]
  s.save()
  return redirect("viewapnt")
  
def deleteapnt(request):
  data = request.GET["apntid"]
  rec = Apnt.objects.get(id=data)
  rec.delete()
  return redirect("viewapnt") 

def dlogin(request):
    return render(request,"myapp/dlogin.html")
def dreg(request):
    return render(request,"myapp/dreg.html")
def regdcode(request):
  email = request.GET["txtemail"]
  pa =    request.GET["txtpass"]
  mobile = request.GET["txtmobile"]
  address=request.GET["txtaddress"]
  date = request.GET["date"]
  obj = Regd(emailid=email,password=pa,mobileno=mobile,address=address,date=date)
  obj.save()  
  return HttpResponse("<h3>you registered successfully</h3>")

def logindcode(request):
  email = request.POST["txtemail"]
  pa    = request.POST["txtpass"]
  objemail = Regd.objects.filter(emailid=email)
  objpass = Regd.objects.filter(password=pa)
  if(objemail.count()==0):
    s = "invalid emailid"
  elif(objpass.count()==0):
    s = "invalid password"  
  else:
    request.session['uid'] = email

    return redirect('viewdapnt')

  return HttpResponse(s)
def viewdapnt(request):
  #res = Apnt.objects.all()
  udata=request.session['uid']
  res = Apnt.objects.filter(apntto=udata)
  return render(request,"myapp/viewdapnt.html",{'apntdata':res}) 

def reply(request):
  #reps = Reply.objects.all()
  rdata=request.session['uid']
  reps = Reply.objects.filter(replyto=rdata)
  return render(request,"myapp/reply.html",{'replydata':reps})
'''def replyapnt(request):
  data = request.GET["apntid"]
  rec = Apnt.objects.get(id=data)
  return render(request,"myapp/replyapnt.html",{'apntdata':rec})'''

def replycode(request):
  d2 = request.GET["txtemail"]
  d3 = request.GET["txtreplyto"]
  d4 = request.GET["txtapntdesc"]
  d5 = request.GET["date"]
  d6 = request.GET["time"]
  obj = Reply(emailid=d2,replyto=d3,replydesc=d4,date=d5,time=d6)
  obj.save()
  return HttpResponse("Your Reply Added Sucessfully")

def pdesh(request):
    return render(request,"myapp/pdesh.html")
def ddesh(request):
    return render(request,"myapp/ddesh.html")
def about(request):
    return render(request,"myapp/about.html")
def feedback(request):
    return render(request,"myapp/feedback.html")

def feedcode(request):
  email = request.GET["txtemail"]
  fbto = request.GET["txtfbto"]
  fbdesc = request.GET["txtfbdesc"]
  date = request.GET["date"]
  time = request.GET["time"]
  obj = Feed(emailid=email,fbto=fbto,fbdesc=fbdesc,date=date,time=time)
  obj.save() 
  return HttpResponse("feedback added successfully")

def viewfeed(request):
  #res = Feed.objects.all()
  udata=request.session['uid']
  rdata=request.session['uid']
  res = Feed.objects.filter(emailid=udata)
  reps = Replyfeed.objects.filter(replyfto=rdata)
  return render(request,"myapp/viewfeed.html",{'feeddata':res,'replyfdata':reps})

def editfeed(request):
  data = request.GET["fbid"]
  rec = Feed.objects.get(id=data)
  return render(request,"myapp/editfeed.html",{'feeddata':rec})

def updatefeed(request):
  data = request.GET["txtid"]
  s = Feed.objects.get(id=data)
  s.fbto=request.GET["txtfbto"]
  s.fbdesc=request.GET["txtfbdesc"]
  s.date=request.GET["date"]
  s.time=request.GET["time"]
  s.save()
  return redirect("viewfeed")

def loginfcode(request):
  email = request.POST["txtemail"]
  pa    = request.POST["txtpass"]
  objemail = Reg.objects.filter(emailid=email)
  objpass = Reg.objects.filter(password=pa)
  if(objemail.count()==0):
    s = "invalid emailid"
  elif(objpass.count()==0):
    s = "invalid password"  
  else:
    request.session['uid'] = email

    return redirect('feeddash')
    
  return HttpResponse(s)

def logindfcode(request):
  email = request.POST["txtemail"]
  pa    = request.POST["txtpass"]
  objemail = Regd.objects.filter(emailid=email)
  objpass = Regd.objects.filter(password=pa)
  if(objemail.count()==0):
    s = "invalid emailid"
  elif(objpass.count()==0):
    s = "invalid password"  
  else:
    request.session['uid'] = email

    return redirect('viewdfeed')
    
  return HttpResponse(s)

def dflogin(request):
    return render(request,"myapp/dflogin.html")

def pflogin(request):
    return render(request,"myapp/pflogin.html")

def feeddash(request):
  udata=request.session['uid']
  return render(request,"myapp/feeddash.html",{'uid':udata})

def deletefeed(request):
  data = request.GET["fbid"]
  rec = Feed.objects.get(id=data)
  rec.delete()
  return redirect("viewfeed")

def viewdfeed(request):
  #res = Apnt.objects.all()
  udata=request.session['uid']
  res = Feed.objects.filter(fbto=udata)
  return render(request,"myapp/viewdfeed.html",{'feeddata':res}) 

def replyfeed(request):
  #reps = Reply.objects.all()
  rdata=request.session['uid']
  reps = Replyfeed.objects.filter(replyfto=rdata)
  return render(request,"myapp/replyfeed.html",{'replyfdata':reps})
'''def replyapnt(request):
  data = request.GET["apntid"]
  rec = Apnt.objects.get(id=data)
  return render(request,"myapp/replyapnt.html",{'apntdata':rec})'''

def replyfcode(request):
  d2 = request.GET["txtemail"]
  d3 = request.GET["txtreplyfto"]
  d4 = request.GET["txtfeeddesc"]
  d5 = request.GET["date"]
  d6 = request.GET["time"]
  obj = Replyfeed(emailid=d2,replyfto=d3,replyfdesc=d4,date=d5,time=d6)
  obj.save()
  return HttpResponse("Your Feed Reply Added Sucessfully")