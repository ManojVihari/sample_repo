from fastapi import APIRouter

router = APIRouter()


from fastapi import APIRouter, HTTPException
from typing import Optional

router = APIRouter()


@router.post("/create_users")
def create_user(name: str, email: str):
    """
    Creates a new user with name and email.
    """

    try:
        # Basic validation
        if not name:
            raise ValueError("Name cannot be empty")

        if "@" not in email:
            raise ValueError("Invalid email format")

        # Simulated business logic
        user = {
            "name": name,
            "email": email
        }

        return {
            "status": "success",
            "data": user
        }

    except ValueError as ve:
        raise HTTPException(
            status_code=400,
            detail=str(ve)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

