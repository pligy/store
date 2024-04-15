import requests
import time

API_URL = "http://0.0.0.0:8000"

start_time = time.time()
post_time = 0
get_time = 0
put_time = 0
delete_time = 0

# Функция для отправки запроса и измерения времени выполнения
def measure_request(method, url, data=None):
    start = time.time()
    response = method(url, json=data)
    end = time.time()
    execution_time = end - start
    return response, execution_time


def test_create_product():
    global post_time
    data = {"name": "Test Product", "price": 10.0, "description": ""}
    response, execution_time = measure_request(requests.post, f"{API_URL}/product", data)
    post_time += execution_time
    print(f"Create Product: Status Code - {response.status_code}, Execution Time - {execution_time}")


def test_read_product():
    global get_time
    response, execution_time = measure_request(requests.get, f"{API_URL}/product")
    get_time += execution_time
    print(f"Read Product: Status Code - {response.status_code}, Execution Time - {execution_time}")


def test_update_product(id):
    global put_time
    data = {"name": "Updated Product", "price": 20.0,  "description": ""}
    response, execution_time = measure_request(requests.put, f"{API_URL}/product/update/{id}", data)
    put_time += execution_time
    print(f"Update Product: Status Code - {response.status_code}, Execution Time - {execution_time}")


def test_delete_product(id):
    global delete_time
    response, execution_time = measure_request(requests.delete, f"{API_URL}/product/delete/{id}")
    delete_time += execution_time
    print(f"Delete Product: Status Code - {response.status_code}, Execution Time - {execution_time}")


def main():
    times = []
    for id in range(1):
        test_create_product()
        test_read_product()
        test_update_product(id + 32466)
        test_delete_product(id + 32466)

        print("=========================================")
        total_time = time.time() - start_time
        print(id + 1, ":", total_time)
        print("total post time:", post_time)
        print("total get time:", get_time)
        print("total put time:", put_time)
        print("total delete time:", delete_time)
        if ((id + 1) % 500 == 0):
            times.append([post_time,
                          get_time,
                          put_time,
                          delete_time,
                          total_time])
            ##time.sleep(0.5)
        print("=========================================")
        #time.sleep(1)  # Пауза между запросами
    print(times)

if __name__ == "__main__":
    main()
