cd ../
docker build -t re_build .
docker run re_build
rm -r main.dist
CONTAINER_ID=$(docker ps -alq)
docker cp $CONTAINER_ID:app/main.dist main.dist
docker stop $CONTAINER_ID
