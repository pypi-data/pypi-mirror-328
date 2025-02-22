from PIL import Image


class Picture:
    @staticmethod
    def Open(file_path):
        return Image.open(file_path)
