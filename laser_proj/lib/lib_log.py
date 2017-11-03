import time
import os.path
class log_info(object):
    file_path = "f:\\log11.txt"
    def __init__(self):
       pass
    @classmethod  #注意这个classmethod
    def output(cls,message):
        log_hdl = open(cls.file_path, 'a')
        now_time = time.time(); 
        now_time_str = time.ctime(now_time);
        log_hdl.write(now_time_str + ": " + message + "\n")
        print(now_time_str + ": " + message)
        log_hdl.close();

# log_info.output("huang")
# log_info.output("huang")
# log_info.output("huang")
# log_info.output("huang")
# log_info.file_path =  "f:\\log.txt"

# log_info.output("huanguiere")
# log_info.output("huang")
# log_info.output("huang")
# log_info.output("huang")