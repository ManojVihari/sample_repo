from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/users")
def create_user(name: str, email: str, role: str):
    """
    Creates a new user with name, email, and role.

    Raises:
        HTTPException(400): If validation fails.
        HTTPException(409): If user already exists.
        HTTPException(500): If unexpected error occurs.
    """

    try:
        # --- Validation ---
        if not name or name.strip() == "":
            raise ValueError("Name cannot be empty")

        if "@" not in email:
            raise ValueError("Invalid email format")

        if role not in ["admin", "user"]:
            raise ValueError("Role must be either 'admin' or 'user'")

        # --- Simulated duplicate check ---
        if email.lower() == "existing@example.com":
            raise HTTPException(
                status_code=409,
                detail="User with this email already exists"
            )

        # --- Business logic ---
        user = {
            "name": name.strip(),
            "email": email.lower(),  # normalize email
            "role": role
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

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
