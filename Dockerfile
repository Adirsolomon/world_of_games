FROM python:alpine

WORKDIR /app

COPY main_score.py utils.py scores.txt requirements.txt

RUN python -m pip install -r requirements.txt

EXPOSE 5000

CMD python main_score.py