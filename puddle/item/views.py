from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm
from .models import Items

def detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]


    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    # Below is passing a check for the New Item.
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else: 
        form = NewItemForm

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })



