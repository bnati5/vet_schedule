from django.http import HttpResponse
import json
import os
from django.utils import timezone
from datetime import datetime, timedelta
from vetster_schedule.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@require_POST
@csrf_exempt
def index(request):
    print(request)
    response_data = [{
                        "status":"success",
                        "message":"The datetime_start is available.",
                        "available":True
                    }]
                
    try:
        # Convert datetime_start to local time zone and calculate datetime_end (datetime_start + 1 hour)
        datetime_start = timezone.localtime(datetime.fromisoformat(request.GET.get('datetime_start')))
        datetime_end = datetime_start + timedelta(hours=1)
    except Exception as e:
        # datetime_start is not valid
        response_data = [{
                            "status":"error",
                            "message":"The datetime_start is not valid.",
                            "available":False
                        }]
        response = HttpResponse(response_data, content_type='application/json charset=utf-8')
        return response
    
    # Read data
    file_path = os.path.join(BASE_DIR, 'assets/data/blocks.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    for row in data:
        
        # Convert datetime_from and datetime_to to local time zone
        datetime_from = timezone.localtime(datetime.fromisoformat(row['datetime_from']))
        datetime_to = timezone.localtime(datetime.fromisoformat(row['datetime_to']))

        # check if datetime_start or datetime_end is in the range of datetime_start
        if (datetime_start >= datetime_from and datetime_start < datetime_to) or (datetime_end > datetime_from and datetime_end <= datetime_to) :
            
            response_data = [{
                                "status":"success",
                                "message":"The datetime_start is not available.",
                                "available":False
                            }]
            break
        
    response = HttpResponse(response_data, content_type='application/json charset=utf-8')
    return response