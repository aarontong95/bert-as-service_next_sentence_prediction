from bert_serving_next_sentence_prediction.server import BertServer
from bert_serving_next_sentence_prediction.server.helper import get_run_args, get_shutdown_parser
args = get_run_args(get_shutdown_parser)
BertServer.shutdown(args)