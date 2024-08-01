from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from .models import Post

blogs = [
        {
          "title":"My first blog", 
          "content": """<p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae ex sit amet justo mollis fermentum.
                    Integer et tellus auctor, ultrices dolor id, varius ipsum. Duis volutpat posuere justo, id lobortis
                    enim vestibulum id. Pellentesque nec eros eu odio auctor sodales sit amet eget ex.
                </p>
                <p>
                    Proin volutpat elit eget orci pellentesque, eget ultricies lectus tincidunt. Proin maximus, purus a
                    rutrum tristique, justo mi dictum risus, vel sodales leo nulla eu orci. Integer ut libero ac tortor
                    consequat suscipit at id justo. Proin consectetur ultricies tellus, sed efficitur libero finibus a.
                </p>
                <p>
                    Sed pulvinar eros sit amet consectetur ultrices. Aliquam vel bibendum odio. In hac habitasse platea
                    dictumst. Curabitur laoreet odio eu velit tincidunt, sed congue neque ullamcorper.
                </p>""", 
            "description": "dddddddddddddddddddddddddd ddddddddddddddddd adada daadda addamad da", 
            "slug":"my-first-blog", 
            "date": datetime.date(2024,1,1), 
            "author": "Hariom Sharma", 
            "image": "hero.jpg" 
        },
        {
          "title":"My first blog", 
          "content": """<p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae ex sit amet justo mollis fermentum.
                    Integer et tellus auctor, ultrices dolor id, varius ipsum. Duis volutpat posuere justo, id lobortis
                    enim vestibulum id. Pellentesque nec eros eu odio auctor sodales sit amet eget ex.
                </p>
                <p>
                    Proin volutpat elit eget orci pellentesque, eget ultricies lectus tincidunt. Proin maximus, purus a
                    rutrum tristique, justo mi dictum risus, vel sodales leo nulla eu orci. Integer ut libero ac tortor
                    consequat suscipit at id justo. Proin consectetur ultricies tellus, sed efficitur libero finibus a.
                </p>
                <p>
                    Sed pulvinar eros sit amet consectetur ultrices. Aliquam vel bibendum odio. In hac habitasse platea
                    dictumst. Curabitur laoreet odio eu velit tincidunt, sed congue neque ullamcorper.
                </p>""", 
            "description": "dddddddddddddddddddddddddd ddddddddddddddddd adada daadda addamad da", 
            "slug":"my-first-blog", 
            "date": datetime.date(2024,1,1), 
            "author": "Hariom Sharma", 
            "image": "hero.jpg" 
        },
        {
          "title":"My first blog", 
          "content": """<p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae ex sit amet justo mollis fermentum.
                    Integer et tellus auctor, ultrices dolor id, varius ipsum. Duis volutpat posuere justo, id lobortis
                    enim vestibulum id. Pellentesque nec eros eu odio auctor sodales sit amet eget ex.
                </p>
                <p>
                    Proin volutpat elit eget orci pellentesque, eget ultricies lectus tincidunt. Proin maximus, purus a
                    rutrum tristique, justo mi dictum risus, vel sodales leo nulla eu orci. Integer ut libero ac tortor
                    consequat suscipit at id justo. Proin consectetur ultricies tellus, sed efficitur libero finibus a.
                </p>
                <p>
                    Sed pulvinar eros sit amet consectetur ultrices. Aliquam vel bibendum odio. In hac habitasse platea
                    dictumst. Curabitur laoreet odio eu velit tincidunt, sed congue neque ullamcorper.
                </p>""", 
            "description": "dddddddddddddddddddddddddd ddddddddddddddddd adada daadda addamad da", 
            "slug":"my-first-blog", 
            "date": datetime.date(2024,1,1), 
            "author": "Hariom Sharma", 
            "image": "hero.jpg" 
        },
        {
          "title":"My first blog", 
          "content": """<p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae ex sit amet justo mollis fermentum.
                    Integer et tellus auctor, ultrices dolor id, varius ipsum. Duis volutpat posuere justo, id lobortis
                    enim vestibulum id. Pellentesque nec eros eu odio auctor sodales sit amet eget ex.
                </p>
                <p>
                    Proin volutpat elit eget orci pellentesque, eget ultricies lectus tincidunt. Proin maximus, purus a
                    rutrum tristique, justo mi dictum risus, vel sodales leo nulla eu orci. Integer ut libero ac tortor
                    consequat suscipit at id justo. Proin consectetur ultricies tellus, sed efficitur libero finibus a.
                </p>
                <p>
                    Sed pulvinar eros sit amet consectetur ultrices. Aliquam vel bibendum odio. In hac habitasse platea
                    dictumst. Curabitur laoreet odio eu velit tincidunt, sed congue neque ullamcorper.
                </p>""", 
            "description": "dddddddddddddddddddddddddd ddddddddddddddddd adada daadda addamad da", 
            "slug":"my-first-blog", 
            "date": datetime.date(2024,1,1), 
            "author": "Hariom Sharma", 
            "image": "hero.jpg" 
        },
        {
          "title":"My first blog", 
          "content": """<p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae ex sit amet justo mollis fermentum.
                    Integer et tellus auctor, ultrices dolor id, varius ipsum. Duis volutpat posuere justo, id lobortis
                    enim vestibulum id. Pellentesque nec eros eu odio auctor sodales sit amet eget ex.
                </p>
                <p>
                    Proin volutpat elit eget orci pellentesque, eget ultricies lectus tincidunt. Proin maximus, purus a
                    rutrum tristique, justo mi dictum risus, vel sodales leo nulla eu orci. Integer ut libero ac tortor
                    consequat suscipit at id justo. Proin consectetur ultricies tellus, sed efficitur libero finibus a.
                </p>
                <p>
                    Sed pulvinar eros sit amet consectetur ultrices. Aliquam vel bibendum odio. In hac habitasse platea
                    dictumst. Curabitur laoreet odio eu velit tincidunt, sed congue neque ullamcorper.
                </p>""", 
            "description": "dddddddddddddddddddddddddd ddddddddddddddddd adada daadda addamad da", 
            "slug":"my-first-blog", 
            "date": datetime.date(2024,1,1), 
            "author": "Hariom Sharma", 
            "image": "hero.jpg" 
        },
        {
          "title":"My first blog", 
          "content": """<p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae ex sit amet justo mollis fermentum.
                    Integer et tellus auctor, ultrices dolor id, varius ipsum. Duis volutpat posuere justo, id lobortis
                    enim vestibulum id. Pellentesque nec eros eu odio auctor sodales sit amet eget ex.
                </p>
                <p>
                    Proin volutpat elit eget orci pellentesque, eget ultricies lectus tincidunt. Proin maximus, purus a
                    rutrum tristique, justo mi dictum risus, vel sodales leo nulla eu orci. Integer ut libero ac tortor
                    consequat suscipit at id justo. Proin consectetur ultricies tellus, sed efficitur libero finibus a.
                </p>
                <p>
                    Sed pulvinar eros sit amet consectetur ultrices. Aliquam vel bibendum odio. In hac habitasse platea
                    dictumst. Curabitur laoreet odio eu velit tincidunt, sed congue neque ullamcorper.
                </p>""", 
            "description": "dddddddddddddddddddddddddd ddddddddddddddddd adada daadda addamad da", 
            "slug":"my-first-blog", 
            "date": datetime.date(2024,1,1), 
            "author": "Hariom Sharma", 
            "image": "hero.jpg" 
        },
        {
          "title":"My Camel blog", 
          "content": """<p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae ex sit amet justo mollis fermentum.
                    Integer et tellus auctor, ultrices dolor id, varius ipsum. Duis volutpat posuere justo, id lobortis
                    enim vestibulum id. Pellentesque nec eros eu odio auctor sodales sit amet eget ex.
                </p>
                <p>
                    Proin volutpat elit eget orci pellentesque, eget ultricies lectus tincidunt. Proin maximus, purus a
                    rutrum tristique, justo mi dictum risus, vel sodales leo nulla eu orci. Integer ut libero ac tortor
                    consequat suscipit at id justo. Proin consectetur ultricies tellus, sed efficitur libero finibus a.
                </p>
                <p>
                    Sed pulvinar eros sit amet consectetur ultrices. Aliquam vel bibendum odio. In hac habitasse platea
                    dictumst. Curabitur laoreet odio eu velit tincidunt, sed congue neque ullamcorper.
                </p>""", 
            "description": "dddddddddddddddddddddddddd ddddddddddddddddd adada daadda addamad da", 
            "slug":"my-camel-blog", 
            "date": datetime.date(2024,1,1), 
            "author": "Hariom Sharma", 
            "image": "camel.jpg" 
        }
]

def starting_page(request):
    # try:
        # return HttpResponse("hi")
        posts = Post.objects.order_by('-date')[:4]
        return render(request, "blog/index.html", {"blogs": posts})
    # except:
    #     print("hi")
    #     raise Http404()

def all_posts(request):
    try:
        # return HttpResponse("hi")
        blogs = Post.objects.all()
        return render(request, "blog/all-blogs.html", {"blogs": blogs})
    except:
        raise Http404()

def post_details(request, slug):
    # try:
        blog = Post.objects.get(slug=slug)
        if blog is not None:
            return render(request, "blog/single-blog.html", {"blog": blog})
        else: 
            # return HttpResponse("sssssssssssssssss")
            raise Http404()
    # except:
    #     raise Http404()