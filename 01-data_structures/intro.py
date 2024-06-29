import redis

r = redis.Redis(
    host='localhost',
    port=6378,
    db=0,
    decode_responses=True
)

def add_data():
    res = r.set(name="bike:1", value="Pixie123")
    print(res)

def del_data():
    res = r.delete("bikes:1")
    print(res)

def get_data():
    res = r.get(name="bike:1")
    print(res)
    

def add_hdata():
    res = r.hset(name="bikes:1", mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    })
    print(res)
    
def get_hdata():
    res = r.hget(name="bikes:1", key="model")
    print(res)

def get_hdata_all():
    res = r.hgetall(name="bikes:1")
    print(res)
    

add_hdata()
get_hdata()
get_hdata_all()
# del_data()
    
