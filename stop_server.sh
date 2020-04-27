uwsgi --stop /home/leishuo/Code/PersonalPage/uwsgi.pid
for kid in `ps -aux | egrep 'PersonalPage.wsgi' | awk -F' ' '{print $2}'`
do
  kill -9 $kid
  #echo $kid
done

