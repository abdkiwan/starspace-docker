
FROM continuumio/anaconda3

RUN conda create -n starspace python=3.6

RUN activate starspace

RUN pip install dkpro-cassis
RUN pip install conan

RUN apt-get update && apt-get -y install unzip build-essential cmake protobuf-compiler python3-dev

RUN wget https://dl.bintray.com/boostorg/release/1.63.0/source/boost_1_63_0.zip && unzip boost_1_63_0.zip
RUN mv boost_1_63_0 /usr/local/bin

ADD publications .
ADD patents .
ADD app.py .

RUN git clone https://github.com/facebookresearch/Starspace.git
RUN make -C Starspace

# Expose the port uWSGI will listen on
EXPOSE 5000

CMD ["python", "app.py"]