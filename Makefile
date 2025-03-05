up:
	docker compose up

up_d:
	docker compose up -d

down:
	docker compose down

stop:
	docker compose stop

stop_down: stop down

rm_exited:
	docker rm $$(docker ps --all | grep -i exited | cut -d " " -f 1)

ps:
	docker ps --all

ps_comp:
	docker compose ps

# flink related
# need the environment to be running
flink_sql:
	docker exec -it flink-jobmanager /opt/flink/bin/sql-client.sh

flink_bash:
	docker exec -it flink-jobmanager bash
