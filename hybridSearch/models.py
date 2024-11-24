from django.db import models

# Table 1: Magazine Info
class MagazineInfo(models.Model):
    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=255)  
    publication_date = models.DateField()  
    category = models.CharField(max_length=100) 

    def __str__(self):
        return self.title

# Table 2: Magazine Content
class MagazineContent(models.Model):
    id = models.AutoField(primary_key=True)  
    magazine = models.ForeignKey(
        MagazineInfo, 
        on_delete=models.CASCADE, 
        related_name='contents'
    )  # Foreign key to MagazineInfo
    content = models.TextField() 
    vector_representation = models.JSONField()  # JSON representation for vector data (Django 3.1+)

    def __str__(self):
        return f"Content for {self.magazine.title}"
