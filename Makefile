IMAGE_PATH="Your/image/path"

docker_build_push:\
	docker_build \
	docker_push \

docker_build:
	docker build . -t $(IMAGE_PATH)/googleplayscraper:latest

docker_push:
	docker push $(IMAGE_PATH)/googleplayscraper:latest