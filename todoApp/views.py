from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import todoApp
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    todo_items = todoApp.objects.all().order_by('-added_date')
    return render(request, 'index.html', {
        "todo_items": todo_items,
    })


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = todoApp.objects.create(added_date= current_date, text = content)
    length_of_todos = todoApp.objects.all().count()
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    todoApp.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")


