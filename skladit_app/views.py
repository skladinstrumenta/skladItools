# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("ПЕРВАЯ страница нашего сайта, and now it's at the skladit_app.urls")


def second_page(request):
    return HttpResponse("Page number 2")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, page_id, name=""):
    print(request.GET)
    if page_id >= 33:
        return HttpResponse(
            "This is an article #{} and it more than 32. {}".format(page_id, "Name of this article is {}".format(
                name) if name else "This is unnamed article"))
    else:
        return HttpResponse(
            "This is an article #{}. {}".format(page_id, "Name of this article is {}".format(
                name) if name else "This is unnamed article"))


def reqget(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"i see this dict request.Get {catid}")
