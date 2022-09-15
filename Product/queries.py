from .models import product
def queryAll():
    return product.objects.all()

