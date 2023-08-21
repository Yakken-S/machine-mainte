from django.shortcuts import render, get_object_or_404
from .models import L1_Name, Issue_History

# ここでビューを作成します。
def l1_list(request):
    l1names = L1_Name.objects.all()
    return render(request, 'mc_report/l1_list.html', {'l1names': l1names})

def issue_list(request, pk):
    l1_name = get_object_or_404(L1_Name, pk=pk)
    issues = Issue_History.objects.filter(l1_name=l1_name)
    return render(request, 'mc_report/issue_list.html', {'issues': issues})