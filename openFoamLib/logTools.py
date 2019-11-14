class LogFile:
    """Encapsulates the log file and allows parsing and modification.

    Instantiate with the log file name.
    """

    def __init__(self, log_file_handle_):
        self.log_file_handle = log_file_handle_

    def readLogFileKey(self, key_):
        """Read a specific key from the log.
        """
        record = []

        log_file = open(self.log_file_handle, 'r')

        for line in log_file:
            if key_ in line:
                record.append(line)

        return (record)

    def parseRunTime(self):

        time_entries = self.readLogFileKey('Time')

        print (time_entries)
