from django.db import models

# Create your models here.
class Item(models.Model) :

    photo_thumb = models.ImageField(blank=True, upload_to="images")
    item_name = models.CharField(max_length=40) # 제품 이름
    type = models.CharField(max_length=8) # 상품종류
    price = models.IntegerField()
    item_text = models.CharField(max_length=400, null=True) # 제품 설명


    def __str__(self) -> str:
        return self.item_name

class ItemDetail(models.Model) :
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.IntegerField()
    remaining = models.IntegerField()

    type = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.task

class Photo(models.Model) : # 사진 여러개
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    path = models.ImageField(blank=True, upload_to="images/detail")