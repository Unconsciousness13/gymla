from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from isabella.models import Competition, Note, Temporada
from django.contrib.auth.models import User


class CompetitionTests(APITestCase):

    def test_view_competitions(self):
        url = reverse('isabella_api:competition_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
