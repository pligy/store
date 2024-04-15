import redis
import json

from database.schemas.schemas import Users

redis_master = redis.Redis(host='redis_master', port=6379, db=0)
redis_slave = redis.Redis(host='redis_slave', port=6379, db=0)

def create_user_redis(user: Users):
    user_data = json.dumps(user.dict())
    redis_master.set(f"user_{user.user_id}", user_data)

def update_user_redis(user_id: int, user: Users):
    user_data = json.dumps(user.dict())
    redis_master.set(f"user_{user_id}", user_data)

def delete_user_redis(user_id: int):
    redis_master.delete(f"user_{user_id}")

def get_user_redis(user_id: int):
    user_data = redis_slave.get(f"user_{user_id}")
    if user_data:
        return json.loads(user_data)
    else:
        return None