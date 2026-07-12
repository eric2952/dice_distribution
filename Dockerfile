FROM python:3.14.5

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends tk python3-tk && rm -rf /var/lib/apt/lists/*

COPY distribution.py .

COPY diceCalculations.py .

COPY dmgPlotter.py .

COPY diceRoller.py .

COPY Images/ ./Images/

COPY Animations/ ./Animations/

CMD ["python3", "distribution.py"]