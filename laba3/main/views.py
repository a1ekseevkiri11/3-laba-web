from django.shortcuts import render, redirect
from django.http import JsonResponse


def index(request):
    return render(request, 'main/index.html')

def calculator(request):
    if request.method == 'POST':
        screen = request.POST.get('screen', '')
        try:
            result = str(eval(screen))
        except Exception as e:
            result = f"Error: {str(e)}"

        return JsonResponse({'result': result})

    # В случае GET-запроса возвращаем сообщение о неверном методе
    return JsonResponse({'error': 'Invalid method'}, status=400)

