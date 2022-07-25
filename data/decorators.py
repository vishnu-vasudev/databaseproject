from django.shortcuts import redirect

def login_required(func):
    def wrap(request, *args, **kwargs):
        if "stud-id" in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrap