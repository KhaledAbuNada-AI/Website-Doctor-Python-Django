from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify



# Create your models here.
#
# TYPE_OF_PERSON = (
#     ('M', 'Male'),
#     ('F', 'Female'),
# )


class Profile(models.Model):

    # DOCTOR_IN={
    #     ('أسنان', 'أسنان'),
    #     ('عظام', 'عظام')
    # }

    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    name = models.CharField(max_length=30,verbose_name=_(" الاسم :"))
    subtitle = models.CharField(max_length=60, verbose_name=_(' نبذه عنك'))
    bio = models.TextField(max_length=300, verbose_name=_(" من أنا : "))
    address = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('المحافظة :'))
    address_detail = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('الهنوان بتفاصيل :'))
    number_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name=_('الهاتف :'))
    working_hours = models.CharField(max_length=3, blank=True, null=True, verbose_name=_('عدد ساعات العمل :'))
    waiting_time = models.IntegerField(verbose_name=_('مده الانتظار :'), blank=True, null=True)
    specialist_doctor = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('متخصص في :'))
    price = models.IntegerField(verbose_name=_(" سعر الكشف : "), null=True, blank=True)
    # type_of_person = models.CharField(verbose_name=_('الجنس : '), choices=TYPE_OF_PERSON, max_length=10)
    facebook = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Facebook'))
    twitter = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Twitter'))
    google = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Google'))
    # join_new = models.DateTimeField(auto_now_add=True, verbose_name=_('وقت الانضمام :'),null=True, blank=True)
    gmail = models.EmailField(max_length=100, blank=True, null=True, verbose_name=_('Gmail'))
    image = models.ImageField(upload_to='profile', verbose_name=_('الصورة الشخصية'), null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, verbose_name=_('slug'))
    # doctor = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('دكتور :'), choices=DOCTOR_IN)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' %(self.user.username)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
