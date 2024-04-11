from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Content
from .forms import ContentForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.

class IndexLV(ListView):
    model=Content

class ContentCV(CreateView):
    model = Content
    fields = ['title','content']
    success_url=reverse_lazy('index')

class ContentDV(DeleteView):
    model=Content
    success_url=reverse_lazy('index')

def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content = content
            # comment.author = request.user  # 현재 로그인한 사용자를 저자로 설정
            comment.save()
            return redirect('detail', pk=content.pk)
    else:
        form = CommentForm()
    return render(request, 'board/content_detail.html', {'object': content, 'form': form})