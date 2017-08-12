FROM gcr.io/tensorflow/tensorflow:1.2.1-devel-py3
RUN apt-get update && apt-get install -y git-core tmux
RUN git clone https://github.com/wagonhelm/Visualizing-Convnets.git /notebooks/cnn
WORKDIR "/notebooks"
RUN pip install -r ./cnn/requirements.txt
CMD ["/run_jupyter.sh"]
