from django.db import models
from datetime import datetime

# Create your models here.
class ShowsManager(models.Manager):
    def basic_valid(self,postData,shows):
        errors = {}

        if len(postData['title']) < 3 or len(postData['title'])  > 50:
            errors["title"] = "Show tittle should be at least 3 characters and not more than 50 characters"
        
        #for show in shows:
            #if show.title == postData['title']:
                #errors["title"] = "Show alrready exist"
        
        if len(postData['desc']) > 0:
            if len(postData['desc']) < 10 or len(postData['desc']) > 300:
                errors['desc'] = "Show description should be at least 10 characters and not more than 300 character"
        
        if postData['network'] == 'default':
            errors['network'] = "Please select a Network for your Show"

        if datetime.strptime(postData['release_date'],"%Y-%m-%d").date() > datetime.today().date():
            errors['release_date'] = "Shows have to be alrready released"
        


        
        return errors

class UsersManager(models.Manager):
    def user_valid(self,userData):
        errors = {}

        if len(userData['name']) < 3 or len(userData['name'])  > 45:
                errors["name"] = "Username must be at least 3 character and not more than 45 characters" 

        return errors

class Networks(models.Model):
    name = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f'{self.id} {self.name}'

class Shows(models.Model):
    title = models.CharField(max_length=255,unique=True)
    desc = models.CharField(max_length=855)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    network = models.ForeignKey(Networks,related_name="show",on_delete = models.CASCADE)
    img = models.URLField(default="https://img.freepik.com/free-vector/tv-show-neon-sign-style-text_44523-738.jpg?size=338&ext=jpg")
    objects = ShowsManager()
    
    def __repr__(self) -> str:
        return f'{self.id} {self.title}'

class Users(models.Model):
    name = models.CharField(max_length=45,unique=True)
    email = models.EmailField(max_length=155,unique=True)
    password = models.CharField(max_length=255)
    allowed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

    def __repr__(self) -> str:
        return f'{self.id} {self.name}'

