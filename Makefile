docker_build_push:\
	docker_build \
	docker_push \

docker_build:
	docker build . -t registry.umlife.net:443/adxmi/adn/googleplayscraper:latest

docker_push:
	docker push registry.umlife.net:443/adxmi/adn/googleplayscraper:latest