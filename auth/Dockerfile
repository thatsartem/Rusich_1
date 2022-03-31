# 
FROM python:3.9

# 
WORKDIR /usr/src/app

# 
COPY ./requirements.txt .

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY main.py .

# 
CMD ["uvicorn", "main:app", "--proxy-headers", "--forwarded-allow-ips='*'", "--host", "0.0.0.0", "--port", "8000"]
