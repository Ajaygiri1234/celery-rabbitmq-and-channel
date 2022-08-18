{\rtf1}
run docker compose up
open rabbitmq cli add user admin using 3 command

rabbitmqctl add_user admin admin
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

rerun celery