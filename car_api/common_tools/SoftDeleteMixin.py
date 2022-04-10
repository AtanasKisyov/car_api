from datetime import datetime

from django.db import models


class SoftDeleteMixin(models.Model):

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True
