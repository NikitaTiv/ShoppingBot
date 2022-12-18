from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

import settings

def has_check_on_image_return_bool(file_name: str) -> bool:
    """
    отправляет фото в Clarifai, сохранят в переменную результат
    """
    channel = ClarifaiChannel.get_grpc_channel()
    app = service_pb2_grpc.V2Stub(channel)
    metadata = (('authorization', f'Key {settings.CLARIFAI_API_KEY}'),)

    with open(file_name, 'rb') as f:
          file_data = f.read()
          image = resources_pb2.Image(base64=file_data)

    request = service_pb2.PostModelOutputsRequest(
        model_id=settings.CLARIFAI_MODEL_ID,
        inputs=[resources_pb2.Input(data=resources_pb2.Data(image=image))])

    response = app.PostModelOutputs(request, metadata=metadata)
    return check_responce_for_object_return_bool(response)


def check_responce_for_object_return_bool(response: service_pb2.MultiOutputResponse) -> bool:
    """
    Проверяет есть ли значение текст в обьекте Clarifai
    """
    if response.status.code == status_code_pb2.SUCCESS:
        for concept in response.outputs[0].data.concepts:
            if concept.name == 'text' and concept.value >= 0.80:
                return True
    else:
        print(f'Ошибка распознавания: {response.outputs[0].status.details}')  # noqa:T201

    return False
