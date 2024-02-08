from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url_repo = models.URLField()
    url_capture = CloudinaryField('url_capture')
    date = models.DateField(auto_now_add=False, blank=True, null=True, editable=True)
    
    def __str__(self) -> str:
        return self.name
    
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "url_repo": self.url_repo,
            "url_capture": self.url_capture.url,
            "date": self.date
        }