# EasyStock

> Generado con [FastStack CLI](https://github.com/tu-usuario/faststack-cli)

![CI](https://github.com/TU_USUARIO/EasyStock/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)

## Stack

- **Backend**: FastAPI + Python 3.12
- **DB**: PostgreSQL 16 + SQLAlchemy async
- **Auth**: JWT
- **Tests**: pytest + coverage
- **CI/CD**: GitHub Actions

## Inicio rápido

```bash
# Con Docker
docker compose -f infra/docker/docker-compose.yml up -d

# Sin Docker
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Docs API

- Swagger: http://localhost:8000/api/v1/docs
- ReDoc:   http://localhost:8000/api/v1/redoc

## Tests

```bash
cd backend && pytest -v --cov=app
```

## Ramas

```
main       ← Producción
staging    ← Demo / pre-producción
develop    ← Integración
feature/*  ← Nuevas funcionalidades
fix/*      ← Correcciones
```
