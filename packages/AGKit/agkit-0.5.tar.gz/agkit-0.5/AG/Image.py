from PIL import Image


class Image:
    @staticmethod
    def Open(file_path):
        return Image.open(file_path)
