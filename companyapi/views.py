from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home Page Requested")
    friends = [
        'Ankit',
        'Ravi',
        'Shyam'
    ]
    return JsonResponse(friends, safe=False)