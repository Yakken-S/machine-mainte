from django.shortcuts import render, get_object_or_404, redirect
from .models import L1_Name, Issue_History
from .forms import PostForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q

def l1_list(request):
    l1names = L1_Name.objects.all()
    return render(request, 'mc_report/l1_list.html', {'l1names': l1names})

def issue_list(request, pk):
    l1_name = get_object_or_404(L1_Name, pk=pk)
    issues = Issue_History.objects.filter(l1_name=l1_name)
    return render(request, 'mc_report/issue_list.html', {'issues': issues})

def post_issue(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('l1_list')
    else:
        form = PostForm(initial={
            "created_id": request.user, 
            "updated_id": request.user
        })
    return render(request, 'mc_report/post_edit.html', {'form': form})

def update_issue(request, pk):
    issue = get_object_or_404(Issue_History, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=issue)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('l1_list')
    else:
        form = PostForm(instance=issue) 

    return render(request, 'mc_report/update_issue.html', {'form': form, 'issue': issue})


@require_POST
def delete_issue(request, pk):
    issue = get_object_or_404(Issue_History, pk=pk)
    issue.delete()
    return redirect('l1_list')


def index(request):
    alarmnum = Issue_History.objects.order_by('-id')
    """ 検索機能の処理 """
    keyword = request.GET.get('keyword')

    if keyword:
        alarmnum = alarmnum.filter(
                 Q(title__icontains=keyword)
               )
        messages.success(request, '「{}」の検索結果'.format(keyword))

    return render(request, 'issue_list.html', {'alarmnum': alarmnum })