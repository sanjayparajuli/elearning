from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class OrderField(models.PositiveBigIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)
    

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.for_fields) is None:
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    query = {
                        field: getattr(model_instance, field)
                        for field in self.for_fields
                    }
