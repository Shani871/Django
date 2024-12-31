from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from  .view import *


urlpatterns = [
   path("home/",emp_home),
   path("add-emp/",emp_add),
   path("delete-emp/<int:emp_id>",emp_delete),
    path("update-emp/<int:emp_id>", update_emp, name="edit_emp"),
   path("about/",about),
   path("testimonials/",testimonials),

    
]