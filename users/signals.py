from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from assets.models import WebMetadata

@receiver(post_migrate)
def setup_permissions(sender, **kwargs):
    """
    Configure les permissions après chaque migration.
    """
    admin_group, _ = Group.objects.get_or_create(name="Admin")
    scanner_group, _ = Group.objects.get_or_create(name="Scanner")

    # Admin a accès à tout
    admin_perms = Permission.objects.all()
    admin_group.permissions.set(admin_perms)

    # Scanner ne peut modifier que les scan results
    content_type = ContentType.objects.get_for_model(WebMetadata)
    scanner_perms = Permission.objects.filter(content_type=content_type)
    scanner_group.permissions.set(scanner_perms)

    print("✅ Groupes et permissions mis à jour après migration")
