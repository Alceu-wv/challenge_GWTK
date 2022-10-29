import pandas as pd

from main_app.tasks.fetch_data_task import fetch_data_task


def test_fetch_data_task(mocker):
    # Arrange
    mocker.patch.object(pd, "read_csv")
    mocker.patch.object(pd.DataFrame, "rename")
    mocker.patch.object(pd.DataFrame, "to_dict")

    # Act
    fetch_data_task()


def test_fetch_data_task_error(mocker):
    # Arrange
    mocker.patch.object(pd, "read_csv", side_effect=Exception("test"))

    # Act
    fetch_data_task()
