from celery.result import AsyncResult

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from .my_tasks import create_task


# @cache_page(timeout=30)
def home(request):
    return render(request, 'long_task/home.html')


@csrf_exempt
def run_task(request):
    if request.method == 'POST':
        task_type = request.POST.get('type')
        task = create_task.delay(task_type)

        return JsonResponse({'task_id': task.id}, status=200)


def get_status(request, task_id):
    if request.method == 'GET':
        response = AsyncResult(task_id)
        result = {
            'task_id': task_id,
            'task_status': response.status,
            'task_result': '' if response.result is None else str(response.result)
        }

        return JsonResponse(result, status=200)
