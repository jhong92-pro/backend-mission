from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Item, ItemDetail, Photo

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    # 밑에 명시 안하면 자동 생성 question_list
    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Item.objects.all()
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'shop/detail.html', {'item':item})