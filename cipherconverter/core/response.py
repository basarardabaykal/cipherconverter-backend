from rest_framework.response import Response

class DetailedResponse(Response):
    def __init__(self, status, status_message=None, message=None, content=None, *args, **kwargs):
        data = {
            "status_message": status_message,
            "message": message,
            "content": content,
        }
        Response()
        super().__init__(data=data, status=status, *args, **kwargs)