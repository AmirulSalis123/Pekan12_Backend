from locust import HttpUser, task, between

class CourseUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        response = self.client.post("/api/token", json={
            "username": "teacher1",
            "password": "pass123"
        })

        if response.status_code == 200:
            token = response.json().get("access")
            self.client.headers = {
                "Authorization": f"Bearer {token}"
            }
        else:
            print("Login gagal:", response.text)

    @task(2)
    def get_courses(self):
        self.client.get("/api/courses")

    @task(1)
    def post_course(self):
        self.client.post("/api/courses", json={
            "name": "Kursus Otomatis",
            "description": "Diuji oleh Locust",
            "price": 1000
        })
