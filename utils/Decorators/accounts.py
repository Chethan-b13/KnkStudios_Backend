from django.contrib.auth.decorators import user_passes_test


"""
Accounts App Decortors

"""

def isAdmin(function=None):
    actual_decorator = user_passes_test(
    lambda user: user.is_active and user.is_superuser)
    if function:
        return actual_decorator(function)
    return actual_decorator