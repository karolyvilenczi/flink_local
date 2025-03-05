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
