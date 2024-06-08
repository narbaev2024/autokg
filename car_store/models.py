from django.db import models

class Category(models.Model):
    objects = None
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name

class CarMake(models.Model):
    objects = None
    car_make_name = models.CharField(max_length=16)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_make_name

class Model(models.Model):
    model_name = models.CharField(max_length=16, unique=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    objects = None
    car_name = models.CharField(max_length=16, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    car_model = models.ForeignKey(Model, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=16)
    CHOICES_DRIVE = (
     ("Задний", "Задний"),
     ("Передний", "Передний"),
     ("Полный привод", "Полный привод")
    )
    drive = models.CharField(verbose_name="Привод", max_length=16, choices=CHOICES_DRIVE)
    CHOICES_ENGINE = (
     ("Бензин", "Бензин"),
     ("Газ", "Газ"),
     ("Дизель", "Дизель")
    )
    engine = models.CharField(max_length=14,choices=CHOICES_ENGINE, null=True, blank=True)
    volume = models.FloatField(default=0.8)


    def __str__(self):
        return self.car_name


class CarImage(models.Model):
    image = models.ImageField(upload_to='img')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)