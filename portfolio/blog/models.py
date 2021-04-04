from django.db import models

#add blog app into setting, url, views, html

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.body

    def summary(self):
        sum = re.sub(r'\s\S*$',r" ...",self.body[:200])
        sum = re.sub(r'\. \.\.$',r'. ',sum)
        return sum[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime(" %b %d, %Y")

#title CharField
#pub_date DateTimeField
#body TextField
#image ImageField

#python manage.py makemigrations
#python manage.py migrate
#add to admin
#def __str

#update views
#update blog.html