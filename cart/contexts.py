from django.shortcuts import get_object_or_404
from projects.models import Projects


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    project_count = 0
    
    for id, quantity in cart.items():
        project = get_object_or_404(Projects, pk=id)
        total += quantity * project.price
        project_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'project': project})
    
    return {'cart_items': cart_items, 'total': total, 'project_count': project_count}