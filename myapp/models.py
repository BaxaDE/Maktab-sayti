from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify

XODIM =(
    ('uqi', 'Fan o\'qituvchisi'),
    ('rah', 'Rahbariyat a\'zosi'),
)

class Rahbariyat(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    lavozimi = models.CharField(max_length=200)
    tamomlagan_oliygohi = models.CharField(max_length=500, help_text='Qaysi oliygohni tamomlagan',verbose_name='educated_on')
    toifa = models.CharField(max_length=50)
    ish_tajriba = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpeg',upload_to='rahbariyat xodim')
    yutuqlari = models.TextField(null=True, blank=True)
    xodim = models.CharField(max_length=3, choices=XODIM, null=True, blank=True)
    class Meta:
        verbose_name = 'Rahbariyat xodim'
        verbose_name_plural = 'Rahbariyat xodimlari'

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super(Rahbariyt, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.width>300 and img.height>300:
                natija = (300, 300)
                img.thumbnail(natija)
                img.save(self.image.path)

class Images(models.Model):
    image = models.ImageField(upload_to='Images')
    date_added = models.DateTimeField(auto_now_add=True)

class Tadbirlar(models.Model):
    name = models.CharField(max_length=500)
    text = models.TextField()
    sanasi = models.DateField(null=True, blank=True)
    images = models.ManyToManyField(Images, null=True, blank=True)
    slug = models.SlugField(max_length=500)

    class Meta:
        verbose_name = 'Tadbir'
        verbose_name_plural = 'Tadbirlar'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Tadbirlar, self).save(*args, **kwargs)
        self.slug = slugify(self.name)

class Yutiqlar(models.Model):
    name = models.CharField(max_length=500)
    text = models.TextField()
    sanasi = models.DateField(null=True, blank=True)
    images = models.ManyToManyField(Images, null=True, blank=True)
    slug = models.SlugField(max_length=500)

    class Meta:
        verbose_name = 'Yutig`imiz'
        verbose_name_plural = 'Yutiqlarimiz'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Yutiqlar, self).save(*args, **kwargs)
        self.slug = slugify(self.name)

SINFLAR = (
    ('1', '1-sinf'),
    ('2', '2-sinf'),
    ('3', '3-sinf'),
    ('4', '4-sinf'),
    ('5', '5-sinf'),
    ('6', '6-sinf'),
    ('7', '7-sinf'),
    ('8', '8-sinf'),
    ('9', '9-sinf'),
    ('10', '10-sinf'),
    ('11', '11-sinf'),
)
class Kutubxona(models.Model):
    sinf = models.CharField(max_length=2, choices=SINFLAR)
    kitob = models.FileField(upload_to='kitoblar', null=True, blank=True)
    kitob_linki = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Kutibxona kitobi'
        verbose_name_plural = 'Kutibxona kitoblarimiz'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Kutubxona, self).save(*args, **kwargs)
        self.slug = slugify(self.name)


class Maktab(models.Model):
    image = models.ImageField(upload_to='Maktab')


class Biz_xaqimizda(models.Model):
    adresses = models.CharField(max_length=500)
    sinflar_soni = models.CharField(max_length=500)
    xodimlar_soni = models.TextField()
    maktab_tarixi = models.TextField()
    pochta_manzil = models.CharField(max_length=50)
    tel_raqami = models.CharField(max_length=20)
    kundalik_com_link = models.URLField(null=True, blank=True)
    images = models.ManyToManyField(Maktab, null=True, blank=True)

    class Meta:
        verbose_name = 'Maktab xaqida'
        verbose_name_plural = 'Maktabimiz tarixi'


class Foydalanuchi(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    baho = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Fodalanuvchilar munosabat'







