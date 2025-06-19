from ninja import NinjaAPI, Schema
from typing import List
from core.models import Course
from django.contrib.auth.models import User

api = NinjaAPI(version="2.1.0")

class CourseSchema(Schema):
    id: int
    name: str
    description: str
    price: int

class CourseCreateSchema(Schema):
    name: str
    description: str
    price: int

@api.get("/courses", response=List[CourseSchema])
def list_courses(request):
    return Course.objects.all()

@api.post("/courses", response=CourseSchema)
def create_course(request, payload: CourseCreateSchema):
    teacher = User.objects.get(username='teacher1')
    course = Course.objects.create(**payload.dict(), teacher=teacher) 
    return course
    
@api.get("/hello")
def hello(request):
    return {"message": "API OK"}

