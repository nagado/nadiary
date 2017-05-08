from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

import datetime
from models import Post
from forms import NewPostForm


def main(request):
    return HttpResponse("TODO: display all records, best to display first whatever and use paginator of some sort.")

class NewPost(ListView):
    form_class = NewPostForm
    template_name = "new_post.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
 
        return render(request, self.template_name, {'new_post_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            header = form.cleaned_data['header']
            body = form.cleaned_data['body']
            date = datetime.datetime.now()
            print "PASSED"
            new_post = Post.objects.create(header=header, body=body, created=date)
            return redirect('posts')

        return render(request, self.template_name, {'new_post_form': form})


class Posts(ListView):
    template_name = "posts.html"

    def get(self, request, *args, **kwargs):
        post_list = []
        
        for post in Post.objects.all():
            post_list.append({'header': post.header, 'body': post.body})

        return render(request, self.template_name, {'post_list': post_list})

