#!/usr/bin/env python
""" This is the entrypoint to the Patient Service API.
"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from lib import (
    department_crud,
    employee_crud,
    hospital_crud,
    insurance_crud,
    medication_crud,
    patient_crud,
    physician_crud,
    prescription_crud,
    response_models,
)
from lib.database_connection import SessionLocal

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Hello World @ Root


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Patient Methods


@app.get("/patients/", response_model=List[response_models.Patient], tags=["Patient Methods"])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = patient_crud.get_patients(db, skip=skip, limit=limit)
    return patients


@app.get("/patients/{id}", response_model=response_models.Patient, tags=["Patient Methods"])
def get_patient_by_id(id: int, db: Session = Depends(get_db)):
    patient = patient_crud.get_patient(db, id)
    return patient


@app.delete("/patients/{id}", tags=["Patient Methods"])
def delete_patient_by_id(id: int, db: Session = Depends(get_db)):
    patient_response = patient_crud.delete_patient(db, id)
    return patient_response


@app.patch("/patients/{id}", tags=["Patient Methods"])
def update_patient_by_id(
    id: int, patient: response_models.PatientUpdate, db: Session = Depends(get_db)
):
    patient = patient_crud.update_patient(db, id, patient)
    return patient


@app.post("/patients/", response_model=response_models.Patient, tags=["Patient Methods"])
def create_patient(patient: response_models.PatientCreate, db: Session = Depends(get_db)):
    patient = patient_crud.create_patient(db, patient)
    return patient


# Physician Methods


@app.get("/physicians/", response_model=List[response_models.Physician], tags=["Physician Methods"])
def get_physicians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    physicians = physician_crud.get_physicians(db, skip=skip, limit=limit)
    return physicians


# Department Methods


@app.get(
    "/departments/", response_model=List[response_models.Department], tags=["Department Methods"]
)
def get_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = department_crud.get_departments(db, skip=skip, limit=limit)
    return departments


# Prescription Methods


@app.get(
    "/prescriptions/",
    response_model=List[response_models.Prescription],
    tags=["Prescription Methods"],
)
def get_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prescriptions = prescription_crud.get_prescriptions(db, skip=skip, limit=limit)
    return prescriptions


# Medication Methods


@app.get(
    "/medications/", response_model=List[response_models.Medication], tags=["Medication Methods"]
)
def get_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medications = medication_crud.get_medications(db, skip=skip, limit=limit)
    return medications


# Insurace Methods


@app.get("/insurances/", response_model=List[response_models.Insurance], tags=["Insurance Methods"])
def get_insurance(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    insurances = insurance_crud.get_insurance(db, skip=skip, limit=limit)
    return insurances


# Employee Methods


@app.get("/employees/", response_model=List[response_models.Employee], tags=["Employee Methods"])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = employee_crud.get_employees(db, skip=skip, limit=limit)
    return employees


# Hospital Methods


@app.get("/hospitals/", response_model=List[response_models.Hospital], tags=["Hospital Methods"])
def get_hospitals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = hospital_crud.get_hospitals(db, skip=skip, limit=limit)
    return employees
