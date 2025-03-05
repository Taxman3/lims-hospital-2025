
# Backend Setup
FROM python:3.9
WORKDIR /app
COPY backend/ .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# Frontend Setup
FROM node:14
WORKDIR /frontend
COPY frontend/ .
RUN npm install
CMD ["npm", "start"]
