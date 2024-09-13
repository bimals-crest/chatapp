from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Subscriber
import json
from django.shortcuts import render

def chat(request):
    # Add your view logic here
    return render(request, 'chat.html')


@csrf_exempt
def optin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone_number = data.get('phone_number')

            if not phone_number or not name or not email:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            # Check if subscriber already exists
            subscriber, created = Subscriber.objects.get_or_create(phone_number=phone_number)

            subscriber.name = name
            subscriber.email = email
            subscriber.is_subscribed = True
            subscriber.save()

            return JsonResponse({'message': 'Successfully opted in!'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def optout(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone_number = data.get('phone_number')

            if not phone_number:
                return JsonResponse({'error': 'Phone number is required'}, status=400)

            # Find the subscriber
            try:
                subscriber = Subscriber.objects.get(phone_number=phone_number)
                subscriber.is_subscribed = False
                subscriber.save()
                return JsonResponse({'message': 'Successfully opted out!'})
            except Subscriber.DoesNotExist:
                return JsonResponse({'error': 'Phone number not found'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
