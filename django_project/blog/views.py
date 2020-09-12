from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from blog.models import Post


# Create your views here.


def home(request):
    return render(request,'blog/home.html')


def about(request):
    return render(request,'blog/about.html',)

class PostListView(ListView):
    context={
        'post':Post.objects.all()
    }
    model=Post
    template_name='blog/blogpost.html'
    context_object_name='post'
    ordering=['-posted_date']


class PostCreateView(CreateView):
    model=Post
    template_name='blog/createpost.html'
    fields=['title','content']

    def form_valid(self,form):
        form.instance.posted_user=self.request.user
        return super().form_valid(form)


def read(request):
    return render(request,'blog/read.html')