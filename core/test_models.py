from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Course, CourseMember

class CourseModelTest(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher1', password='pass123')
        self.student = User.objects.create_user(username='student1', password='pass123')
        self.course = Course.objects.create(
            name='Python Dasar',
            description='Belajar dari nol',
            price=150,
            teacher=self.teacher
        )

    def test_course_creation(self):
        self.assertEqual(self.course.name, 'Python Dasar')
        self.assertEqual(str(self.course), 'Python Dasar')
        self.assertFalse(self.course.is_member(self.student))

    def test_is_member_method(self):
        CourseMember.objects.create(course_id=self.course, user_id=self.student, roles='std')
        self.assertTrue(self.course.is_member(self.student))

class CourseMemberModelTest(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher1', password='pass123')
        self.student = User.objects.create_user(username='student1', password='pass123')
        self.course = Course.objects.create(
            name='Python Dasar',
            description='Belajar dari nol',
            price=150,
            teacher=self.teacher
        )
        self.course_member = CourseMember.objects.create(
            course_id=self.course,
            user_id=self.student,
            roles='std'
        )

    def test_course_member_creation(self):
        self.assertEqual(self.course_member.roles, 'std')
        self.assertEqual(str(self.course_member), 'Python Dasar : student1')
