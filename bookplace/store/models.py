from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,default='')
    class Meta:
        verbose_name_plural= 'Categories'
        ordering = ('title',)

    def __str__(self):
        return self.title    

class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'Ciorna'),
        (WAITING_APPROVAL, 'Asteapta aprobare'),
        (ACTIVE, 'Activ'),
        (DELETED, 'Sters')
    )

    user = models.ForeignKey(User, related_name='products',on_delete=models.CASCADE)
    category=models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='uploads/pdfs/', blank=False, null=False ,  validators=[FileExtensionValidator(allowed_extensions=["pdf","epub"])])
    image = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)
    editie = models.IntegerField()
    editura = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=50)
    limba = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)