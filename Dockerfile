FROM jupyter/datascience-notebook:python-3.7.6

RUN pip install dash==1.10.0
RUN pip install gunicorn==20.0.4

EXPOSE 8050

ENTRYPOINT ["/bin/bash"]
