from django.http  import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect
from django.urls import reverse
from django.template import loader
# Create your views here.

class TempClass:
   x=5


def hello(request):
  # template=loader.get_template('app/hello.html')
   list=['Alpha',"Beta"]
   temp=TempClass()
   is_authenticated=False
   context={"name":"ALI","age":"21", "first_list":list,"temp_object":temp, "is_authenticated":is_authenticated}
   # return HttpResponse(template.render(context,request))
   return render(request,'app/hello.html',context)


job_title=[
    "First Job",
    "Second Job",
    "Third Job"
]

job_description=[
     "First Job Description",
     "Second Job Description",
     "Third Job Description"
]

def job_lists(request):
#    lists_of_jobs="<ul>"
#    for i in job_title:
#       job_id= job_title.index(i)
#       detail_url=reverse('job_detail',args=(job_id,))
#       lists_of_jobs+=f"<li><a href='{detail_url}'>{i}</a></li>"
#    lists_of_jobs+="</ul>"
#    return HttpResponse(lists_of_jobs)
 context={"job_title":job_title}
 return render(request,"app/job-lists.html",context)
    

def job_detail(request,id):
 try:
      if id==0:
        return redirect(reverse('jobs_home'))
      context={"job_title":job_title[id],"job_description":job_description[id]}
      return render(request,"app/job-detail.html",context)
     # return_html= f"<h1>{job_title[id]}</h1>  <h3>{job_description[id]}</h3>"
     # return HttpResponse(return_html)
 except:
    return HttpResponseNotFound("Not Found")