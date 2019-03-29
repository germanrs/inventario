from import_export import resources
from .models import Laptop

class LaptopResource(resources.ModelResource):
    class Meta:
        model = Laptop