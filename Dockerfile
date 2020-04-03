FROM jupyter/datascience-notebook:python-3.7.6

RUN pip install dash==1.10.0

EXPOSE 8050

ENTRYPOINT ["/bin/bash"]
