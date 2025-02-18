from tortoise import fields, models

class ShortLink(models.Model):
    id = fields.IntField(pk=True)
    original_url = fields.CharField(max_length=2048)
    short_url = fields.CharField(max_length=20, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)