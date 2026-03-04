import random

from services.service_a import handle_request as service_a
from services.service_b import handle_request as service_b

services = [
    service_a,
    service_b
]

def route_request(data):

    selected_service = random.choice(services)

    response = selected_service(data)

    return response