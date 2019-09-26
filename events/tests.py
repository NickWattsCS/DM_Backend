from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from . models import Event
from . serializers import EventSerializer


EVENTS_URL = "/events/"

class EventsApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_events_list(self):
        #Test retrieving a list of events
        Event.objects.create(name="Fun in the sun", place="landis", points="100")
        Event.objects.create(name="Pool party", place="heritage grove", points="200")

        res = self.client.get(EVENTS_URL)

        events = Event.objects.all().order_by('time')
        serializer = EventSerializer(events, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
