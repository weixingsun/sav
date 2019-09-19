#perf record -F 99 -ag -- sleep 30
#perf script > out.perf
#./stackcollapse-perf.pl out.perf > out.folded
#cat out.folded | ./flamegraph.pl --cp > flame.svg
PID=`ps -ef|grep transformer_main.py|grep -v grep |awk '{print $2}'`

