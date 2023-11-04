from django.shortcuts         import render

def completeRequest(request):
  return render(request, "sign-in.html")


def rejectRequest(request):
  return render(request, "about.html")