from django.shortcuts import render
import wikipedia
from simple_image_download import simple_image_download as simp

# Create your views here.
def index(request):
    if request.method == "POST":
        celebrity = request.POST['celebrity_name']

        # for getting celebrity wiki summary
        try:
            celebrity_summary = wikipedia.summary(celebrity,sentences=10)
        except wikipedia.exceptions.DisambiguationError or wikipedia.exceptions.PageError:
            celebrity_summary = f"{celebrity} page not found please Try with another name!"

        # for getting celebrity photo
        response         = simp.simple_image_download
        celebrity_photos = response().urls(celebrity, 5)

        # for getting celebrity name from wikipedia summary
        if celebrity_summary.find('(') != -1:
            celebrity_name =  celebrity_summary[:celebrity_summary.find('(')]
        else:
            celebrity_name = celebrity

        context = {
            'celebrity_photos': celebrity_photos,
            'celebrity_summary':celebrity_summary,
            'celebrity_name': celebrity_name,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
