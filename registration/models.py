from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User, Group, Permission


class UserProfile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    logged = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

    @property
    def token(self):
        return


@receiver(models.signals.post_save, sender=User)
def post_save_user_signal_handler(sender, instance, created, **kwargs):
    if len(User.objects.filter(username='admin')) != 0:
        if created:
            UserProfile.objects.create(user=instance)
            instance.userprofile.save()
            group, created = Group.objects.get_or_create(name='users')
            instance.is_staff = True
            instance.groups.add(group)
            instance.save()
            permissions_list = ['add', 'change', 'view', 'delete']
            for permission in permissions_list:
                permission = Permission.objects.get(name=f'Can {permission} post')
                group.permissions.add(permission)

