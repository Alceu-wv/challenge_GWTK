import pandas as pd
import pytest

from main_app.models import OrderDetails
from main_app.parsers.order_detail_parser import fetch_order_details

pytestmark = pytest.mark.django_db


def test_fetch_order_details_creates_objects(mocker, df_order_details):
    # Arrange
    mocker.patch.object(pd, "read_csv", return_value=df_order_details)

    # Act
    fetch_order_details()

    # Assert
    assert OrderDetails.objects.all().count() == 11


def test_fetch_order_details_ignore_registered_objects(mocker, df_order_details_repeated_element):
    # Arrange
    mocker.patch.object(pd, "read_csv", return_value=df_order_details_repeated_element)

    # Act
    fetch_order_details()

    # Assert
    assert OrderDetails.objects.all().count() == 1
