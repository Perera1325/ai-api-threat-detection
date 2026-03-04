metrics = {
    "allowed":0,
    "blocked":0
}

def record(status):

    metrics[status] += 1

def get_metrics():

    return metrics