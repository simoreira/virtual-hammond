import os
from helpers import *
from http.api_controller import ApiController

class ClientController:
    def open_file(self, filename):
        return open(abspath_from_relativepath(filename), 'rb')

    def default(self, attr):
        return self.open_file('../client/404.html')

    def index(self):
        return self.open_file('../client/index.html')

    def add(self):
        return self.open_file('../client/add.html')

    def songs(self):
        return self.open_file('../client/songs.html')

    def about(self):
        return self.open_file('../client/about.html')
