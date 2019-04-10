from django.shortcuts import render
#crear vistas

def post_list(request):
    return render(request, 'acora/post_list.html',{})

