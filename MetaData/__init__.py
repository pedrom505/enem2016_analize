import os
import requests


class Enem2016:
    url = "https://s3-us-west-1.amazonaws.com/codenation-challenges/enem-ps/testfiles.zip"

    def __init__(self, metadata_path: str):
        if not isinstance(metadata_path, str):
            raise TypeError("database_path should be a string!")

        self.__create_metadata_directory(metadata_path)
        self.__download_metadata(self.url, metadata_path)

    @staticmethod
    def __download_metadata(url, path):
        metadata_file_name = "files.zip"
        metadata_path = os.path.join(path, metadata_file_name)
        if not os.path.exists(metadata_path):
            req = requests.get(url, allow_redirects=True)
            fd = open(metadata_path, 'wb')
            fd.write(req.content)
            fd.close()

    @staticmethod
    def __create_metadata_directory(metadata_path):
        if "\\" in metadata_path:
            splited_path = metadata_path.split("\\")
        elif "/" in metadata_path:
            splited_path = metadata_path.split("/")
        else:
            splited_path = metadata_path

        metadata_path = os.path.join(*splited_path)

        if not os.path.exists(metadata_path):
            full_path = ""
            for path_segment in splited_path:
                full_path = os.path.join(full_path, path_segment)
                if not os.path.exists(full_path):
                    os.mkdir(full_path)


