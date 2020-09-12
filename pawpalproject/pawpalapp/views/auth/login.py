import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def login(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    if request.method == 'GET':
        template = 'registration/login.html'
        context = {}

        return render(request, template, context)


    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        print("Request:", request.body)
        req_body = json.loads(request.body.decode())
        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)
        print("AUTH USER:", authenticated_user)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')

#         else:
#             # Bad login details were provided. So we can't log the user in.
#             data = json.dumps({"valid": False})
#             return HttpResponse(data, content_type='application/json')
