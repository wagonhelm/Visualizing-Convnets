# Visualizing Convnets

<img src="imageFiles/conv1.gif">

This repository has the code from my O'Reilly article [Visualizing Convolutional Neural Networks w/ TensorFlow](https://www.oreilly.com/ideas/visualizing-convolutional-neural-networks) published on September 15th, 2017.

This code contains tools for building a dataset and a jupyter notebook for implementing and visualizing a simple convolutional neural network.

## Required Packages
* [TensorFlow v1.2](http://www.tensorflow.org/)
* [Jupyter](http://jupyter.org/)
* [NumPy](http://www.numpy.org/)
* [Scipy](https://www.scipy.org/)
* [Matplotlib](http://matplotlib.org/)
* [Pillow](http://python-pillow.org/)

There are three ways you can install these packages: by using Docker, by using Anaconda Python, or installing the packages manually yourself.  Though not required if you have a NVidia graphic card with a compute capability of 3.0 or greater and atleast 3gb of memory using GPU supported TensorFlow will drasticallly improve preformance. Instructions for installing GPU supported TensorFlow can be found [here](https://github.com/wagonhelm/ML-Workstation-Installation-Guide).

### Using Docker

1. Download and install [Docker](https://www.docker.com/).  If using Ubuntu 14.04/16.04 I wrote my own instructions for installing docker [here](https://github.com/wagonhelm/ML-Workstation-Installation-Guide#install-docker).

2. Download and unzip [this entire repo from GitHub](https://github.com/wagonhelm/Visualizing-Convnets), either interactively, or by entering
    ```bash
    git clone https://github.com/wagonhelm/Visualizing-Convnets.git
    ```

3. Open your terminal and use `cd` to navigate into the directory of the repo on your machine
    ```bash
    cd Visualizing-Convnets
    ```
    
4. To build the Dockerfile, enter
    ```bash
    docker build -t cnn_dockerfile -f dockerfile .
    ```
    If you get a permissions error on running this command, you may need to run it with `sudo`:
    ```bash
    sudo docker build -t cnn_dockerfile -f dockerfile .
    ```

5. Run Docker from the Dockerfile you've just built
    ```bash
    docker run -it -p 8888:8888 -p 6006:6006 cnn_dockerfile bash
    ```
    or
    ```bash
    sudo docker run -it -p 8888:8888 -p 6006:6006 cnn_dockerfile bash
    ```
    if you run into permission problems.

6. Launch Jupyter and Tensorboard both by using tmux 
    ```bash
    tmux
    
    jupyter notebook --allow-root
    ```
    `Press CTL+B` then `C` to open a new tmux window, then
    
    ```
    tensorboard --logdir='/tmp/cnn'
    ```
    To switch windows `Press CTL+B` then `window #` 
 
    Once both jupyter and tensorboard are running, using your browser, navigate to the URLs shown in the terminal output if those don't work  try http://localhost:8888/ for Jupyter Notebook and http://localhost:6006/ for Tensorboard.
