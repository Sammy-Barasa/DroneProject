
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    return Response({"Message": "DataAPIEndpoint"})


# connect subscribe to influxdb stream database

# analyze data only for flights on that day 

# filter data from that day

# note late flag

# calculate compliency index

# Calculate decent and accent rate

# 