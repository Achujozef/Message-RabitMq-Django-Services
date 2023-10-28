from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, ProductUser

def product_list(request):
    products = Product.objects.all()
    return JsonResponse(list(products.values()), safe=False)

def like_product(request, id):
    user_id = request.GET.get('user_id')
    product = get_object_or_404(Product, id=id)

    try:
        ProductUser.objects.create(user_id=user_id, product=product)
        # Add your publish logic here
        return JsonResponse({'message': 'success'})
    except:
        return JsonResponse({'message': 'You already liked this product'}, status=400)
