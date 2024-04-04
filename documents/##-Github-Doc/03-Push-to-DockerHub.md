## 3.1 Publish the docker image to Docker Hub

### 3.1.1 Prerequisites

You need to have a Docker Hub account. If you don't have one, you can create one at https://hub.docker.com/. You also need to have Docker installed on your machine. Once you have Docker installed, you can log in to your Docker Hub account by running the following command:

```docker
docker login
```

### 3.1.2 Tag the docker image

To publish the docker image `docker-hoppy-brew-app-container` to Docker Hub, you need to tag the image with your Docker Hub username. You can do this by running the following command:

- Usage:  docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

```docker
docker tag docker-hoppy-brew-app-image asbjornbordoy/docker-hoppy-brew-app-image
```

This will tag the image `docker-hoppy-brew-app-image` with the username `asbjornbordoy` and the image name `docker-hoppy-brew-app-image`. You can verify that the image has been tagged correctly by running the following command:

```docker
docker images
```

You should see the tagged image in the list of images. If you have tagged the image incorrectly, you can remove the tag by running the following command:

```docker
docker rmi asbor/docker-hoppy-brew-app-image
```

once you have tagged the image correctly, you can push the image to Docker Hub by running the following command:

```docker
docker push asbjornbordoy/docker-hoppy-brew-app-image
```

This will push the image to Docker Hub. You can verify that the image has been pushed successfully by logging in to your Docker Hub account and navigating to the repository.

