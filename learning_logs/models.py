from django.db import models

# Create your models here.

# Model for the learning topics
class Topic(models.Model):
    ''' A topic that the user can learn about'''
    text= models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''String representation of the model'''
        return self.text

class Entries(models.Model):
    '''From the Topics youve learned you add entries about'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    knew_before = models.TextField()
    know_now = models.TextField()
    ties_in = models.TextField()
    example_1 = models.TextField()
    example_2 = models.TextField()
    example_3 = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."
