import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import render_to_string

posts = [
    {
        "id":1,
        "title": "HTML in a nutshell",
        "content": "May indulgence difficulty ham can put especially. Bringing remember for supplied her why was "
                   "confined. Middleton principle did she procuring extensive believing add. Weather adapted prepare "
                   "oh is calling. These wrong of he which there smile to my front. He fruit oh enjoy it of whose "
                   "table. Cultivated occasional old her unpleasing unpleasant. At as do be against pasture covered "
                   "viewing started. Enjoyed me settled mr respect no spirits civilly.",
        "date": datetime.datetime.now(),
        "author": "Eden Lovely"
    },
    {
        "id": 2,
        "title": "JavaScript the hard way",
        "content": "Greatly cottage thought fortune no mention he. Of mr certainty arranging am smallness by "
                   "conveying. Him plate you allow built grave. Sigh sang nay sex high yet door game. She dissimilar "
                   "was favourable unreserved nay expression contrasted saw. Past her find she like bore pain open. "
                   "Shy lose need eyes son not shot. Jennings removing are his eat dashwood. Middleton as pretended "
                   "listening he smallness perceived. Now his but two green spoil drift.",
        "date": datetime.datetime.now(),
        "author": "Annie Adegbite"
    },
    {
        "id": 3,
        "title": "CSS the hard way",
        "content": "Ecstatic advanced and procured civility not absolute put continue. Overcame breeding or my "
                   "concerns removing desirous so absolute. My melancholy unpleasing imprudence considered in "
                   "advantages so impression. Almost unable put piqued talked likely houses her met. Met any nor may "
                   "through resolve entered. An mr cause tried oh do shade happy.",
        "date": datetime.datetime.now(),
        "author": "Ife Olarewaju"
    },
    {
        "id": 4,
        "title": "Love the right way",
        "content": "Delightful unreserved impossible few estimating men favourable see entreaties. She propriety "
                   "immediate was improving. He or entrance humoured likewise moderate. Much nor game son say feel. "
                   "Fat make met can must form into gate. Me we offending prevailed discovery.",
        "date": datetime.datetime.now(),
        "author": "Gabriel Ladden"
    },

]


# Create your views here.
def index(request):
    # return HttpResponse(render_to_string("posts/index.html"))
    return render(request, "posts/index.html", context={"posts": posts})


def post_detail(request, post_id):
    post = posts[post_id - 1]
    return render(request, "posts/post-details.html", {"post": post})
