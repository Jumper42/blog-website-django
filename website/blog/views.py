from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Post
from .forms import CommentForm


class HomeView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]


class DetailPostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tag.all(),
            "form": CommentForm(),
            "comments": post.comments.all().order_by("-date"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            print(comment)
            post_url = reverse("post-detail-page", args=[slug])
            return HttpResponseRedirect(post_url)
        context = {
            "post": post,
            "tags": post.tag.all(),
            "form": CommentForm(),
            "comments": post.comments.all().order_by("-date"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html', context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None:
            context["posts"] = []
            context["has_post"] = False
        else:
            context["posts"] = Post.objects.filter(id__in=stored_posts)
            context["has_post"] = True

        return render(request, 'blog/read-later.html', context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts

        read_later_url = reverse("read-later")
        return HttpResponseRedirect(read_later_url)
