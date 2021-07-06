from django.shortcuts import render,redirect
from . models import Category, Photo
# Create your views here.
def gallery(request):
  category = request.GET.get('category')
  # if no category shows all
  if category == None:
    photos = Photo.objects.all()
  # else filter with category
  else:
    photos = Photo.objects.filter(category__name=category)

  categories = Category.objects.all()

  context = {'categories':categories, 'photos':photos}
  return render(request,'photos/gallery.html',context)

def view_photo(request,pk):
  photo = Photo.objects.get(id=pk)


  return render(request,'photos/photo.html',{"photo":photo})

def add_photo(request):
  categories = Category.objects.all()

  if request.method == "POST":
    data = request.POST
    # input 'name' is 'image'
    image = request.FILES.get('image')

    # if there is a category use the category
    if data['category'] != 'none':
      category = Category.objects.get(id=data['category'])
    # if there is a new category use the new category 
    elif data['category_new'] != '':
      category, created = Category.objects.get_or_create(name=data['category_new'])
    # if there is no category say None
    else:
      category = None

    photo = Photo.objects.create(
      category = category,
      description = data['description'],
      image = image,
    )

    return redirect('gallery')
  context = {'categories':categories}
  return render(request,'photos/add.html',context)