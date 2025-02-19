import base64
from BlobStorage.Storage import BlobStorage

class BlobFielHandler:

    def __init__(self):
        self.blob_storage = BlobStorage()

    async def get_file_base64(self, file_path:str, type:str = None, size:float = None, url:str = None, mime_type:str = None):
        extension = file_path.split('.')[-1]
        file_bytes = await self.blob_storage.get_file(file_path) 
        file_name = file_path.split('/')[-1].split('.')[0]
        return {
            'name': file_name,
            'type': type,
            'size': size,
            'ext': extension,
            'base64': base64.b64encode(file_bytes).decode('utf-8'),
            'url': url,
            'mimeType': mime_type
        }