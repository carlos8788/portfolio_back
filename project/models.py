from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url_repo = models.URLField()
    url_capture = CloudinaryField('url_capture')
    
    def __str__(self) -> str:
        return self.name
    
    def to_dict(self):
        return{
            "name": self.name,
            "description": self.description,
            "url_repo": self.url_repo,
            "url_capture": self.url_capture.url
        }