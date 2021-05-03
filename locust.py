import random

from locust import User, task, HttpUser, between


# class MyUser(User):
#     @task
#     def my_task(self):
#         print("executing my_task")
#
#     wait_time = between(5, 15)



class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def news_feed_page(self):
        self.client.get("/post/newsfeed/")
        # self.client.get("/world")

    # @task(3)
    # def view_item(self):
    #     item_id = random.randint(1, 10000)
    #     self.client.get(f"/item?id={item_id}", name="/item")

    # def on_start(self):
    #     self.client.post("/login", {"username":"foo", "password":"bar"})