
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from server.apps.school.models import Course


@pytest.mark.django_db
def test_create_course():
    client = APIClient()
    url = reverse('course-list')
    data = {'title': 'Test Course', 'code': 'TEST101', 'description': 'This is a test course'}
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert Course.objects.count() == 1
    assert Course.objects.get().title == 'Test Course'

@pytest.mark.django_db
def test_list_courses():
    Course.objects.create(title='Course 1', code='C101', description='Description 1')
    Course.objects.create(title='Course 2', code='C102', description='Description 2')

    client = APIClient()
    url = reverse('course-list')
    response = client.get(url, format='json')
    assert response.status_code == 200
    assert len(response.data) == 2