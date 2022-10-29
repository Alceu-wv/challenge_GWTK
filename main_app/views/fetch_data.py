from drf_spectacular.utils import extend_schema
from loguru import logger
from rest_framework import viewsets
from rest_framework.response import Response

from main_app.tasks.fetch_data_task import fetch_data_task


class FetchPizzasViewSet(viewsets.ViewSet):

    authentication_classes = []

    @extend_schema(
        summary="fetch CSV data",
        description="This request triguers this API to fetch data from the folder 'data' in root directory",
    )
    def fetch_data(self, request, *args, **kwargs):
        logger.info("'fetch_data' request received")

        task = fetch_data_task.delay()
        logger.info(task.id)

        return Response({"status": "OK", "task_id": task.id}, status=200)
