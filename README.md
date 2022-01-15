# isaac_hsr

## Requirements
 - OS: Ubuntu 18.04 or 20.04

## Setup
### Setting up Docker
```bash
curl https://get.docker.com | sh \
  && sudo systemctl --now enable docker
```
If you input the following command, even regular users will be able to execute the docker command.
```
sudo usermod -aG docker $USER
```

For more information, [see](https://docs.docker.com/engine/install/ubuntu/).

### Setting up Docker Compose
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

For more information, [see](https://docs.docker.com/compose/install/).


### Setting up NVIDIA Container Toolkit
```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
```

For more information, [see](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

### Login into NGC 
Follow the steps in [Generate Your NGC API Key](https://docs.nvidia.com/ngc/ngc-overview/index.html#generating-api-key).

```bash
docker login nvcr.io
```

For more information, [see](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/isaac-sim).

## Usage
Please input the following commands to clone this repository.
```bash
git clone https://github.com/matsuolab/isaac_hsr.git
cd isaac_hsr
```

## Starting the simulator
Please input the following command and start the simulator (it takes a minutes to launch).
```bash
docker-compose up
```
