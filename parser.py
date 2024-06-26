
import sys

for f in os.listdir(sys.argv[1]):
    fpath = os.path.join(sys.argv[1], f)
    os.system("tshark -nn -T fields -E separator=/t  -e frame.time_epoch"
              " -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport"
              " -e ip.proto -e ip.len -e ip.hdr_len -e tcp.hdr_len -e data.len"
              " -e tcp.flags -e tcp.options.timestamp.tsval"
              " -e tcp.options.timestamp.tsecr -e tcp.seq  -e tcp.ack"
              " -e tcp.window_size_value -e _ws.expert.message "
              " -r  {0} > {0}.tshark".format(fpath))

