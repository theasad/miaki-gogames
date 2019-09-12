from django.shortcuts import redirect


def redirect_to_game_list(request):
    return redirect("games")
