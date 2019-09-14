from django.shortcuts import redirect, reverse


def redirect_to_game_list(request):
    return redirect('/admin')
