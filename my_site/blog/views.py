from django.shortcuts import render
from django.http import HttpResponse, Http404

blogs = [
    {"title":"My first blog", "content": "lorem"}
]

def starting_page(request):
    # try:
        # return HttpResponse("hi")
        return render(request, "blog/index.html", {"latest_blogs": blogs[-3:0]})
    # except:
        # return Http404()

def posts(request):
    # try:
        # return HttpResponse("hi")
        return render(request, "blog/blog-list.html", {"blogs": blogs})
    # except:
        # return Http404()

def post_details(request):
        pass
