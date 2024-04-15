from locust import HttpUser, task, between
import time

class MyUser(HttpUser):
    wait_time = between(0, 0)
    order_id = None

    @task(1)
    def create_order(self):
        data = {"sale_date": "2024-03-28",
                "delivery_date": "2024-04-04",
                "quantity": 1,
                "user_id": 1,
                "product_id": 2}
        start_time = time.time()
        response = self.client.post("/order", json=data)
        execution_time = time.time() - start_time
        self.environment.events.request_success.fire(request_type="POST", name="/order", response_time=execution_time, response_length=0)
        self.order_id = response.json().get("order_id")  # Assuming your API returns the ID of the newly created order

    @task(2)
    def read_order(self):
        start_time = time.time()
        response = self.client.get("/order")
        execution_time = time.time() - start_time
        self.environment.events.request_success.fire(request_type="GET", name="/order", response_time=execution_time, response_length=0)

    @task(1)
    def update_order(self):
        if self.order_id:
            data = {"sale_date": "2024-03-28",
                    "delivery_date": "2024-04-04",
                    "quantity": 1,
                    "user_id": 1,
                    "product_id": 3}
            start_time = time.time()
            response = self.client.put(f"/order/update/{self.order_id}", json=data)
            if response.status_code != 404:
                execution_time = time.time() - start_time
                self.environment.events.request_success.fire(request_type="PUT", name="/order/update", response_time=execution_time, response_length=0)

    @task(1)
    def delete_order(self):
        if self.order_id:
            start_time = time.time()
            response = self.client.delete(f"/order/delete/{self.order_id}")
            if response.status_code != 404:
                execution_time = time.time() - start_time
                self.environment.events.request_success.fire(request_type="DELETE", name="/order/delete", response_time=execution_time, response_length=0)

    def on_start(self):
        self.create_order()

class WebsiteUser(HttpUser):
    tasks = [MyUser]