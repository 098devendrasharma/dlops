# this is help to store log formate 
import os 
import sys 
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# logging_str = "[%(asctime)s --> give current time 
#                 :%(levelname)s--> info 
#                 :%(module)s--> comes from which folder  
#                 :%(message)s]"

log_dir = "logs" 
log_filepath = os.path.join(log_dir, "running_logs.log") 
os.makedirs(log_dir , exist_ok=True)  # make log dir

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
) 

logger = logging.getLogger("cnnClassifierLogger") 