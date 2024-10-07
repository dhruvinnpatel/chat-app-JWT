from django.db import models
from authn.models import UserData

class Messages(models.Model):
    sender_name = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='sender')
    reciever_name = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='receiver')
    description = models.TextField()
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"To:{self.reciever_name} From:{self.sender_name}"
    
    class Meta:
        ordering = ('timestamp',)
        
        
class Friends(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    friend = models.IntegerField()  
    
    def __str__(self):
        return f"{self.friend}"
     
    