from django.shortcuts import render
from django.views.generic import TemplateView

def pat_func(request):
    return render(request, 'second_task/func_template.html')

class pat_class(TemplateView):
    template_name = 'second_task/class_template.html'