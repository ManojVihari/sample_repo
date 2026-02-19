from fastapi import APIRouter

router = APIRouter()


@router.post("/users")
def create_user(name: str, email: str):
    return {"message": f"User {name} created with email {email}"}

