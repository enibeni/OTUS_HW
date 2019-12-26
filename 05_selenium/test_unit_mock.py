import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendar(unittest.TestCase):
    @patch('my_calendar.requests.get')
    def test_get_holidays_200(self, mock_requests):
        mock_requests.return_value.status_code = 200
        response = get_holidays()
        self.assertEqual(response.status_code, 200)

    @patch('my_calendar.requests.get')
    def test_get_holidays_return_value(self, mock_requests):
        mock_requests.return_value.value = "Sunday"
        response = get_holidays()
        self.assertEqual(response.value, "Sunday")

    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()
