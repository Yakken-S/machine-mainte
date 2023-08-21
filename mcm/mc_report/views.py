from django.shortcuts import render, get_object_or_404
from .models import L1_Name, Issue_History

# Create your views here.
def l1_list(request):
    l1names = L1_Name.objects.all()
    return render(request, 'mc_report/l1_list.html', {'l1names':l1names})

def issue_list(request, pk):
    issues = get_object_or_404(Issue_History, pk=l1_name)
    return render(request, 'mc_report/issue_history.html', {'issues': issues})