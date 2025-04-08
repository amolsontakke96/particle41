To start this container there some prerequisites like docker should be installed

#Installation setup of docker

step-1: sudo apt-get update

step-2: sudo apt-get install ca-certificates curl

step-3: sudo install -m 0755 -d /etc/apt/keyrings

step-4: sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

step-5: sudo chmod a+r /etc/apt/keyrings/docker.asc

step-6: echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

step-7: sudo apt-get update

step-8: sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

step-9: sudo usermod -aG docker $USER

#Command to run container 

Docker login --> to login in dockerhub provide your dockerhub credentials

docker build -t <your-image-name>:latest . --> this command will build the docker image

docker run -d -p 80:80 <image-name> --> this command will run container

docker tag <local-image>:<tag> <dockerhub-username>/<repository-name>:tag --> this command will tag new name to image with dockerhub repository name

docker push <dockerhub-username>/<repository-name>:tag --> this command will push the docker image to dockerhub


