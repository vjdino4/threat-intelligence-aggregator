from datetime import datetime

def normalize(indicator, ioc_type, source):

    return {
        "indicator": indicator.lower(),
        "type": ioc_type,
        "source": source,
        "timestamp": str(datetime.now())
    }
