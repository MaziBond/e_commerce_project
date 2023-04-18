from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from product_pages.models import Product, Review
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    products = get_list_or_404(Product)
    context = { 'products': products }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def reviews(request, product_id):
    product = Product.objects.get(pk=product_id)
    review_form = ReviewForm(request.POST)
    if request.method == 'POST' and review_form.is_valid():
        content = review_form.cleaned_data['content']
        rating = review_form.cleaned_data['rating']

        review = Review.objects.create(author=request.user,
                                       product=product,
                                       content=content,
                                       rating=rating)

        review.save()
        return redirect('get-reviews', product_id=product_id)
    else:
        review_form = ReviewForm()
    context = {
        'form': review_form,
        'product': product
    }
    return render(request, 'dashboard/give_review.html', context)

@login_required(login_url='login')
def get_all_reviews(request, product_id):
    product = Product.objects.get(pk=product_id)
    reviews = product.reviews.all()
    context = {'reviews': reviews,
               'product': product}
    return render(request, 'dashboard/review.html', context)


@login_required(login_url='login')
def get_single_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'dashboard/view_single_review.html', {'review': review })
