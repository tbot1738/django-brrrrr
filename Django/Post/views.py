from django.shortcuts import render
from .models import UserPicHandler as UPH
from django.shortcuts import redirect

def Home_Page(request):

    return render(request, "post.html")



def ImageUploader(request):
    pic = request.FILES["Choose File"]
    picHandler = UPH(image=pic);
    picHandler.save();
    return redirect("/")



