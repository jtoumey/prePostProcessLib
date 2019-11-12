
class OfDict():

    def __init__(self, file_handle_):
        self.file_handle = file_handle_

        # Open and close the file to delete the contents
        of_dict = open(self.file_handle, 'w')
        of_dict.close()

    def writeBuffer(self, buffer_):
        of_dict = open(self.file_handle, 'a')
        for key in buffer_:
            of_dict.write(key)
        of_dict.close()


    def clearLine(self):
        of_dict = open(self.file_handle, 'a')
        of_dict.write('\n')
        of_dict.close()
