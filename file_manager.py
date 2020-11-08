class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        a = open(self.file_name)
        while True:
            dane = a.read(1024)
            print(dane, end="")
            if not dane:
                a.close()
                break

    def update(self, text_data):
        a = open(self.file_name, "w")
        a.write(text_data)
        a.close()








