import http
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from  .forms import *
from .forms import TicketForm
from .models import *
from django.core.paginator import Paginator
from django.views.generic import ListView , DetailView
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def post(request):
#
#     post  = Post.objects.all()
#     paginator = Paginator(post, 2)
#     page_number = request.GET.get('page'  , 1)
#     posts = paginator.page(page_number)
#     context = {
#         "posts" : posts
#     }
#
#     return  render(request , 'mains/post.html' , context)

class PostListView(ListView):
    model = Post
    paginate_by = 2
    context_object_name = 'posts'
    template_name = 'mains/post.html'
    ordering = ['-id']

def inner_post(request , id):
    comment_form = CommentForm()
    context = {
        "post" : Post.objects.get(id=id),
        "form" : comment_form
    }
    return render(request , 'mains/inner_post.html' , context)

# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = 'post'
#     template_name = 'mains/inner_post.html'
#     pk_url_kwarg = 'id'



def ticket(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            print(ticket_form.cleaned_data)
            Ticket.objects.create(**ticket_form.cleaned_data)
            return redirect('project1:ticket')
    else:
        ticket_form = TicketForm()

    return render(request, 'froms/ticket.html', {'form': ticket_form})

@require_POST
def comment_view(request , post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
       comment =  form.save(commit=False)
       comment.post = post
       comment.save()
       return render(request , 'froms/comment.html' , context={  'comment': comment , 'post' : post } )
    return render(request , 'froms/comment.html' , context={  'form' : form, 'post' : post } )

