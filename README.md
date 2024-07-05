Build and Start Services:
docker-compose up --build


Publish a Message Using Nameko Shell
nameko shell


Inside the Nameko shell:
n.rpc.publisher.publish_message("Hello, World!")


Check Listener Logs:
docker-compose logs listener
