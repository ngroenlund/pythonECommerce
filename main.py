import seqlog
import logging


seqlog.log_to_seq(
   server_url="http://localhost:5341/",
   level=logging.INFO,
   batch_size=1,
   auto_flush_timeout=1,  # seconds
   override_root_logger=True
)

logging.info('1')

input()

