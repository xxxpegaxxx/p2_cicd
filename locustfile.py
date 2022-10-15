from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("https://cjvp2cicdapp.azurewebsites.net/")
        self.client.get("https://cjvp2cicdapp.azurewebsites.net/")
