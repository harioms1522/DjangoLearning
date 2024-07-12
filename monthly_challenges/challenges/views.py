from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

message_mappings = {
    "january": "Go to gym daily!",
    "feburary": "Hi there its fab and holiday",
    "march": None,
    "april": "Complete django in the first 2 weeks!"
}

# Get all the values in this dict in an array
message_arr = list(message_mappings.values())

# def monthly_challenge(request, month):
#     print(month)
#     return  HttpResponse(message_mappings[month]) if (message_mappings.get(month) != None) else HttpResponseNotFound("This Month is not supported!") 

def index(request):
    # html = "<ul>"
    # for item in list(message_mappings.items()):
    #     print(item)
    #     redirect_url = reverse("monthly-challange", args=[item[0]])
    #     html += f"<a href={redirect_url} blank ><li>{item[0]}</li> </a>"
    # html += "</ul>"
    # return HttpResponse(html)

    return render(request, "challenges/index.html", {"months": list(message_mappings.keys())})


def monthly_challenge(request, month):
    # try:
        # return HttpResponse(message_mappings[month])
        # response_data = render_to_string("challenges/challange.html")
        # return HttpResponse(response_data)

        # We can use directly render
        challange = message_mappings[month]
        return render(request, "challenges/challange.html", {
            "month": month,
            "challange": challange
        })
    # except: 
        # return HttpResponseNotFound("<h1>This Month is not supported!</h1>")
        raise Http404()

# def month_challenge_by_number(request, month):
#     monthNumber = int(month)
#     if monthNumber-1 > len(message_arr):
#         return HttpResponseNotFound("This month is not supported!")
#     return HttpResponse(message_arr[monthNumber-1])

def month_challenge_by_number(request, month):
    months = list(message_mappings.keys())
    try: 
        forward_month = months[month-1]
        # return HttpResponseRedirect(f"/challenges/{forward_month}")
        redirect_url = reverse("monthly-challange", args=[forward_month])
        return HttpResponseRedirect(redirect_url)
    except: 
        # return HttpResponseNotFound("<h1>This Month is not supported!</h1>")
        raise Http404()
