from django.db import models

# User
class User(models.Model):
  user_name = models.CharField(max_length=20, primary_key=True, null=False)
  user_password = models.CharField(max_length=20, null=True)
  
  def __str__(self):
    return self.user_name

  def get_delete_url(self) :
    return f"deleteuser/{self.pk}/"


class MycarAll(models.Model):
  mycar_speed = models.IntegerField(default=0, null=True)
  mycar_battery = models.IntegerField(default=0, null=True)
  mycar_color = models.TextField(null=True)
  mycar_encoder_or = models.IntegerField(default=0, null = True)
  mycar_encoder_ac = models.IntegerField(default=0, null = True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  user_name = models.ForeignKey("User", on_delete=models.CASCADE, db_column='user_name')
  check_time = models.IntegerField(default=0, null = True)

  def get_delete_url(self) :
    return f"deletemycarall/{self.pk}/"
  

class Mycar(models.Model):
  mycar_speed = models.IntegerField(default=0, null=True)
  mycar_battery = models.IntegerField(default=0, null=True)
  mycar_color = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  user_name = models.ForeignKey("User", on_delete=models.CASCADE, db_column='user_name')

  def get_delete_url(self) :
    return f"deletemycar/{self.pk}/"
  
  def get_update_url(self) :
    return f"updatemycar/{self.pk}/"

