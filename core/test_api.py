import json
from django.test import TestCase, Client
from core.models import Course
from django.contrib.auth.models import User

class APICourseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.teacher = User.objects.create_user(username='teacher1', password='pass123')
        Course.objects.create(
            name='Django Ninja',
            description='API cepat dengan Pydantic',
            price=200,
            teacher=self.teacher
        )

    def test_authenticated_access(self):
        self.client.login(username='teacher1', password='pass123')
        response = self.client.get("/api/courses")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django Ninja")

    def test_unauthenticated_access(self):
        response = self.client.get("/api/courses")
        self.assertEqual(response.status_code, 401)

    def test_create_course_authenticated(self):
        self.client.login(username="teacher1", password="pass123")
        data = {
            "name": "REST API",
            "description": "Belajar REST dengan Django",
            "price": 250
        }
        response = self.client.post("/api/courses", data=json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_create_course_unauthenticated(self):
        data = {
            "name": "REST API",
            "description": "Harusnya gagal",
            "price": 123
        }
        response = self.client.post("/api/courses", data=json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)

    def test_create_course_invalid_price(self):
        self.client.login(username="teacher1", password="pass123")
        data = {
        "name": "Course Error",
        "description": "Ini invalid",
        "price": "bukan angka"  # ❌ Salah tipe
        }
        response = self.client.post("/api/courses", data=json.dumps(data),
                                content_type="application/json")
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())
