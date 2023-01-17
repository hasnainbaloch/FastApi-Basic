from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.utils.hashing import Hash
from app.models import User as UserModel
from app.schema import ShowUser, User
from app.database import get_db
from app.utils import oAuth2

router = APIRouter(prefix="/auth", tags=["Auth"])


def assignId(role):
    if role == "Developer":
        return 1
    elif role == "Manager":
        return 2
    else:
        return 3


# Create user
@router.post("/signup", response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = UserModel(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=Hash.bcrypt(request.password),
        role_id=assignId(request.role),
        roles=request.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Login user
@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(UserModel).filter(UserModel.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials"
        )

    token_body = {
        "email": user.email,
        "id": user.id,
        "token_type": "bearer",
        "roles": [user.roles],
    }
    token = oAuth2.create_access_token(data=token_body)
    return {"access_token": token}
