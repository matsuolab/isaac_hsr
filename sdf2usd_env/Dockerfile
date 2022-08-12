FROM nvidia/cudagl:11.3.0-devel-ubuntu20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get -y upgrade && apt-get install -y \
    python3-dev python3 python3-pip python3-venv \
    libgl1-mesa-dev libgl1-mesa-glx libglew-dev libosmesa6-dev patchelf swig \
    xvfb libglfw3-dev libosmesa-dev python-opengl \
    wget curl unzip git zsh vim ffmpeg fzf apt-utils
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update -y
RUN  apt-get install -y git python3-pip wget lsb-release gnupg curl
RUN  sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
RUN wget http://packages.osrfoundation.org/gazebo.key -O - |  apt-key add -
RUN  apt-get update -y

RUN git clone --depth 1 -b v21.11 https://github.com/PixarAnimationStudios/USD.git

RUN apt install -y libpyside2-dev python3-opengl cmake libglu1-mesa-dev freeglut3-dev mesa-common-dev 

RUN cd /USD && python3 build_scripts/build_usd.py --build-variant release --no-tests --no-examples --no-tutorials --no-docs --no-python /root
ENV PATH /root/bin:$PATH
ENV LD_LIBRARY_PATH /root/lib:$LD_LIBRARY_PATH
ENV CMAKE_PREFIX_PATH /root:$CMAKE_PREFIX_PATH
# RUN mkdir ~/sdf_source
# RUN cd ~/sdf_source/

WORKDIR /root/sdf_source/
RUN git clone https://github.com/ignitionrobotics/sdformat
# RUN cd sdformat

WORKDIR /root/sdf_source/sdformat
RUN apt -y install $(sort -u $(find . -iname 'packages-'`lsb_release -cs`'.apt' -o -iname 'packages.apt' | grep -v '/\.git/') | tr '\n' ' ') -y
# RUN mkdir build
# RUN cd build

WORKDIR /root/sdf_source/sdformat/build
# RUN pwd
# RUN ls
RUN cmake ../ -DCMAKE_INSTALL_PREFIX=/usr
RUN make -j4
# make install will work as the root user in a docker container
# otherwise you may need to use ` make install`
RUN make install

RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
RUN wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add -
RUN apt-get update -y
RUN apt-get install -y libignition-fuel-tools7
RUN apt-get install -y libignition-fuel-tools7-dev

RUN ign fuel download --url  "https://fuel.ignitionrobotics.org/1.0/OpenRobotics/models/Panda with Ignition position controller model"

RUN echo 'alias sdf2usd="/root/sdf_source/sdformat/build/bin/sdf2usd"' >> ~/.bashrc

WORKDIR /root