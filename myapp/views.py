from django.shortcuts import render,redirect


# Create your views here.


# view>> view for creating new Movie
# Create View method:GET,POST
# url:localhost:8000/mov/add/
from django.views.generic import View

from myapp.forms import MovieForm
from myapp.models import Movies
from django.contrib import messages



class MovieCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=MovieForm()
        return render(request,"movie_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data

            Movies.objects.create(
                title=data.get("title"),
                genre=data.get("genre"),
                language=data.get("language"),
                year=data.get("year"),
                run_time=data.get("run_time"),
                director=data.get("director"),
            )
            messages.success(request,"movie hasbeen added")

            return redirect("movie-list")
        else:
            messages.error(request,"failed")
            return render(request,"movie_add.html",{"form":form_instance})
        

# listing movies
# method:list
# url:localhost:8000/movies/all/

class MovieListView(View):
    def get(self,request,*args,**kwargs):
        qs=Movies.objects.all()
        return render(request,"movie_list.html",{"movies":qs})
    

# moviedetail view
# url:lh:8000/movies/<int:pk>/
# url:lh:8000/movies/1/
# method:get



class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movies.objects.get(id=id)
        return render(request,"movie_detail.html",{"movie":qs})
    

# MovieDeleteView
# url:lh:8000/movie/<int:pk>/remove
# method:get


class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movies.objects.get(id=id).delete()

        messages.success(request,"movie removed")
        return redirect("movie-list")    #import redirect(#django>shortcut>redirect)
    



class MovieUpdateView(View):
    def get(self,request,*args,**kwargs):  


        id=kwargs.get("pk")
        movie_object=Movies.objects.get(id=id)

        movie_dictionary={
            "title":movie_object.title,
            "genre":movie_object.genre,
            "language":movie_object.language,
            "year":movie_object.year,
            "run_time":movie_object.run_time,
            "director":movie_object.director

        }




        form_instance=MovieForm(initial=movie_dictionary)

        return render(request,"movie_edit.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):
        form_instance=MovieForm(request.POST)
        if form_instance.is_valid():

            data=form_instance.cleaned_data
            id=kwargs.get("pk")
            Movies.objects.filter(id=id).update(**data)

            return redirect("movie-list")

        else:
            return render(request,"movie_edit.html",{"form":form_instance})


            

    


        
