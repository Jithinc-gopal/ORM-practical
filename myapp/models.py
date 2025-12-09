from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='team_members'
    )
    
    def __str__(self):
        return self.name
    

class EmployeeProfile(models.Model):  
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.employee.name}'s Profile"
    

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(
        Employee,
            on_delete=models.SET_NULL,
            null=True,
            related_name='headed_department'
            )
    def __str__(self):
            return self.name
    
        
class Project(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(
            Department,
            on_delete=models.CASCADE,
            related_name='projects'
            )    
    members =models.ManyToManyField(
            Employee,
            related_name='projects'
        )

    def __str__(self):
              return self.title