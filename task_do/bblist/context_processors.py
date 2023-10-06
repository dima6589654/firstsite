

def user_groups(request):
    if request.user.is_authenticated:
        user_groups = request.user.groups.all()
    else:
        user_groups = []
    return {'user_groups': user_groups}
