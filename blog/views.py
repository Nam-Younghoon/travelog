from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Tag, Comment, ReplyComment
from .forms import PostForm, CommentForm, ReplyCommentForm
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = '-created_at'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        posts = context['posts']
        for post in posts:
            total = 0
            for comment in post.comments.all():
                total += len(comment.replys.all())
            total += len(post.comments.all())
            setattr(post, 'reply_count', total)

        return context

    
class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        pk = object.pk
        post = Post.objects.get(pk=pk)
        post.views_count += 1
        post.save()
        return super().get_object(queryset)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['commentForm'] = CommentForm()
        context['recommentForm'] = ReplyCommentForm()
        return context
    
    
class BlogWriteView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_write.html'

    def form_valid(self, form: BaseModelForm):
        postForm = form.save(commit=False)
        postForm.author = self.request.user
        response = super().form_valid(form)

        tags = self.request.POST.get('tag')
        if tags:
            tags = tags.split(',')
            for tag in tags:
                tag = tag.strip()
                _tag, _ = Tag.objects.get_or_create(name=tag)
                if _:
                    _tag.slug = slugify(tag, allow_unicode=True)
                    _tag.save()
                self.object.tags.add(_tag)

        return response

    def get_success_url(self):
        # return super().get_success_url()
        return reverse('blog:blog_detail', args=[str(self.object.pk)])

class BlogEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_write.html'
    redirect_unauthenticated_users = True

    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user
    
    def get_context_data(self, **kwargs):
        # return super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        if self.object.tags.all():
            tag_list = []
            for t in self.object.tags.all():
                tag_list.append(t.name)
            context['tag_default'] = ', '.join(tag_list)

        return context
    
    def form_valid(self, form: BaseModelForm):
        response = super().form_valid(form)
        self.object.tags.clear()

        tags = self.request.POST.get('tag')
        if tags:
            tags = tags.split(',')
            for tag in tags:
                tag = tag.strip()
                _tag, _ = Tag.objects.get_or_create(name=tag)
                if _:
                    _tag.slug = slugify(tag, allow_unicode=True)
                    _tag.save()
                self.object.tags.add(_tag)

        return response

    def get_success_url(self):
        # return super().get_success_url()
        return reverse('blog:blog_detail', args=[str(self.object.pk)])
    
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog_list')
    redirect_unauthenticated_users = True

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user
    
class BlogCommentView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CommentForm
    template_name = None

    def form_valid(self, form: BaseModelForm):
        commentForm = form.save(commit=False)
        commentForm.post = self.get_object()
        commentForm.author = self.request.user
        commentForm.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog:blog_detail', args=[str(self.get_object().pk)])
    
class BlogCommentReplyView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = ReplyCommentForm
    template_name = None

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        recommentForm = form.save(commit=False)
        recommentForm.author = self.request.user
        recommentForm.comment = self.get_object()
        recommentForm.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog:blog_detail', args=[str(self.get_object().post.pk)])


class BlogCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user
    
    def get_success_url(self):
        return reverse('blog:blog_detail', args=[str(self.get_object().post.pk)])
    
class BlogReplyCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ReplyComment

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user
    
    def get_success_url(self):
        return reverse('blog:blog_detail', args=[str(self.get_object().comment.post.pk)])

class BlogSearchView(ListView):
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            posts = context['posts']
            for post in posts:
                total = 0
                for comment in post.comments.all():
                    total += len(comment.replys.all())
                total += len(post.comments.all())
                setattr(post, 'reply_count', total)

            return context

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '')

        if q:
            queryset = queryset.distinct().filter(
                Q(title__icontains=q) | Q(category__type__iexact=q) | Q(tags__name__iexact=q)
            )
        else:
            queryset = queryset.none()

        return queryset

    def get_ordering(self):
        ordering = self.request.GET.get('sort', '')
        if ordering == 'latest':
            return '-created_at'
        elif ordering == 'past':
            return 'created_at'
        


blog_list = BlogListView.as_view()
blog_detail = BlogDetailView.as_view()
blog_write = BlogWriteView.as_view()
blog_edit = BlogEditView.as_view()
blog_delete = BlogDeleteView.as_view()
blog_search = BlogSearchView.as_view()
blog_comment = BlogCommentView.as_view()
blog_comment_reply = BlogCommentReplyView.as_view()
blog_delete_comment = BlogCommentDeleteView.as_view()
blog_delete_recomment = BlogReplyCommentDeleteView.as_view()
