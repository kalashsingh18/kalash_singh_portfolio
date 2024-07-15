from django.db import models
import json


class message(models.Model):
    name = models.TextField()
    email = models.EmailField(primary_key=True)
    message = models.TextField()
class projects(models.Model):
    project_name=models.TextField(primary_key=True)
    project_description=models.TextField()
class skills(models.Model):
    items = models.TextField()
    def set_items(self, items_list):
        self.items = json.dumps(items_list)
    def get_items(self):
        return json.loads(self.items)
