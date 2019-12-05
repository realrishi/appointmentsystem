from django.db import models

class Reg(models.Model):
	
    emailid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mobileno = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateField('date published')
    
    def __str__(self):
        return self.emailid

class Apnt(models.Model):
    
    emailid = models.CharField(max_length=200)
    apntto = models.CharField(max_length=200)
    apntdesc = models.CharField(max_length=200)
    date = models.DateField('date published')
    time = models.TimeField('time published')
    def __str__(self):
        return self.apntto  

class Regd(models.Model):
	
    emailid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mobileno = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateField('date published')
    
    def __str__(self):
        return self.emailid
    

class Reply(models.Model):
    
    emailid= models.CharField(max_length=200)
    replyto = models.CharField(max_length=200)
    replydesc = models.CharField(max_length=200)
    date = models.DateField('date published')
    time = models.TimeField('time published')
    
    def __str__(self):
        return self.emailid        

class Feed(models.Model):
    
    emailid = models.CharField(max_length=200)
    fbto = models.CharField(max_length=200)
    fbdesc = models.CharField(max_length=200)
    date = models.DateField('date published')
    time = models.TimeField('time published')
    def __str__(self):
        return self.fbto

class Replyfeed(models.Model):
    
    emailid= models.CharField(max_length=200)
    replyfto = models.CharField(max_length=200)
    replyfdesc = models.CharField(max_length=200)
    date = models.DateField('date published')
    time = models.TimeField('time published')
    
    def __str__(self):
        return self.emailid