from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Autenticar usuario y devolver token"""
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # Aquí generarías un token JWT en una implementación real
    return {
        "access_token": "fake-token",  # Reemplazar con token real
        "token_type": "bearer",
        "user_id": user.id,
        "email": user.email
    }