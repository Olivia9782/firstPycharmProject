import logging.handlers
import time


class GetLogger:
    logger=None
    @classmethod
    def get_logger(cls):
        if cls.logger is None :
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)


            sh = logging.StreamHandler()
            # th = logging.handlers.TimedRotatingFileHandler(filename="../log/log02.txt".format(time.strftime("%Y-%m-%d %H:%M:%S")),
            #                                                 when='midnight',
            #                                                 interval=1,
            #                                                 backupCount=30,
            #                                                 encoding="utf-8")

            th = logging.handlers.TimedRotatingFileHandler(filename="../log/logtime.log",
                                                            when="S",
                                                            interval=1,
                                                            backupCount=3,
                                                            encoding="utf-8")
            fmt = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
            fm = logging.Formatter(fmt)
            sh.setFormatter(fm)
            th.setFormatter(fm)

            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)




        return cls.logger


