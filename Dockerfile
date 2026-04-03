# 1. Base image (Python ka chota version)
FROM python:3.9-slim

# 2. Project folder container ke andar banayein
WORKDIR /app

# 3. Zaroori files copy karein
COPY . /app

# 4. Libraries install karein
RUN pip install --no-cache-dir streamlit pandas matplotlib plotly

# 5. Port 8501 kholiye (Streamlit ke liye)
EXPOSE 8501

# 6. Dashboard chalane ki command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]