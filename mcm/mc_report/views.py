from django.shortcuts import render, get_object_or_404
from .models import L1_Name, Issue_History
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView)

def l1_list(request):
    l1names = L1_Name.objects.all()
    return render(request, 'mc_report/l1_list.html', {'l1names': l1names})

def issue_list(request, pk):
    l1_name = get_object_or_404(L1_Name, pk=pk)
    issues = Issue_History.objects.filter(l1_name=l1_name)
    return render(request, 'mc_report/issue_list.html', {'issues': issues})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'mc_report/post_edit.html', {'form': form})


class IssueCreateView(CreateView):
    creates = Issue_History.objects.all()
    #更新後のリダイレクト先
    def get_success_url(self):
        return reverse('mc_report:issues', 'Issue_form.html',kwargs={'pk': self.object.pk})
