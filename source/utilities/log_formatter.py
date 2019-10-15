import logging

class LogFormatter(logging.Formatter):
    """
    Formatter for log messages.
    """
        
    def format(self, record) -> str:
        """
        Formats a log message

        @param record(str): record to format
        @return (str): formatted record
        """

        max_width = 5
        record.levelname = record.levelname.lower()[:max_width]
        levelname_len = len(record.levelname)
        
        if levelname_len <= max_width:
            record.levelname = record.levelname + (' ' * (max_width - levelname_len))

        return logging.Formatter.format(self, record)
