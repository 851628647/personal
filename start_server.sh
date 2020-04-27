:<<!
#端口号
PORT=8002
#多进程个数
PROCESSES=1
#线程个数
THREADS=1
#log文件地址
STD_LOG="Log/std_log"
ERROR_LOG="Log/err_log"

uwsgi --http :$PORT --module PersonalPage.wsgi --master --processes $PROCESSES --threads $THREADS  1>$STD_LOG 2>$ERROR_LOG & 
!
uwsgi --ini /home/leishuo/Code/PersonalPage/uwsgi.ini
