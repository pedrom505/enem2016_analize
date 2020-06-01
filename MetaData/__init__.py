import os
import requests
import zipfile


class Enem2016:
    url_metadata = "https://s3-us-west-1.amazonaws.com/codenation-challenges/enem-ps/testfiles.zip"
    url_dictionary = "https://s3-us-west-1.amazonaws.com/acceleration-assets-highway/data-science/dicionario-de-dados.zip"

    compressed_metadata_file = "metadata.zip"
    compressed_dictionary_file = "dict.zip"

    def __init__(self, files_path: str):
        if not isinstance(files_path, str):
            raise TypeError("database_path should be a string!")
        else:
            self.files_path = os.path.normpath(files_path)
        self.__create_directory(files_path)

    def download_metadata(self):
        metadata_path = os.path.join(self.files_path, self.compressed_metadata_file)
        self.__download_file(self.url_metadata, metadata_path)
        self.__unzip_file(metadata_path, self.files_path)

    def get_train_file_path(self):
        train_file_name = "train.csv"
        return os.path.join(self.files_path, train_file_name)

    def download_dictionary(self):
        dictionary_path = os.path.join(self.files_path, self.compressed_dictionary_file)
        self.__download_file(self.url_dictionary, dictionary_path)
        self.__unzip_file(dictionary_path, self.files_path)

    @staticmethod
    def __create_directory(file_path):
        splited_path = file_path.split(os.path.sep)
        file_path = os.path.join(*splited_path)

        if not os.path.exists(file_path):
            full_path = ""
            for path_segment in splited_path:
                full_path = os.path.join(full_path, path_segment)
                if not os.path.exists(full_path):
                    os.mkdir(full_path)

    @staticmethod
    def __download_file(url, file_path):
        if not os.path.exists(file_path):
            req = requests.get(url, allow_redirects=True)
            fd = open(file_path, 'wb')
            fd.write(req.content)
            fd.close()

    @staticmethod
    def __unzip_file(file_path, output_path):
        if os.path.exists(file_path):
            zip_ref = zipfile.ZipFile(file_path, 'r')
            zip_ref.extractall(output_path)
            zip_ref.close()
            os.remove(file_path)
