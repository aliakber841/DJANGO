from django.urls import path
from app import views


urlpatterns = [
    path('',views.job_lists,name='jobs_home'),
    path('job/<int:id>',views.job_detail, name='job_detail')
]
