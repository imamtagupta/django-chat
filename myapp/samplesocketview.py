from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User  # Assuming you want to track changes in User model
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Signal handler for post_save (triggered on create and update)
@receiver(post_save, sender=User)  # You can change `User` to any other model
def user_saved(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()

    # Prepare the message based on whether it's an update or a new user
    if created:
        message = f"New user created: {instance.username}"
    else:
        message = f"User updated: {instance.username}"

    # Send the message to WebSocket group
    async_to_sync(channel_layer.group_send)(
        'data_updates',  # The group name
        {
            'type': 'data_update',
            'message': message,
        }
    )

# Signal handler for post_delete (triggered on delete)
@receiver(post_delete, sender=User)
def user_deleted(sender, instance, **kwargs):
    channel_layer = get_channel_layer()

    message = f"User deleted: {instance.username}"

    # Send the message to WebSocket group
    async_to_sync(channel_layer.group_send)(
        'data_updates',
        {
            'type': 'data_update',
            'message': message,
        }
    )
