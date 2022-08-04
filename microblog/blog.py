from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from microblog.schemas import PostCreate, PostList
from microblog.service import get_post_list, create_post
from src.app.db.db import get_db

router = APIRouter()

@router.get('/', response_model=List[PostList])
def post_list(db: Session = Depends(get_db)):
    return get_post_list(db)



@router.post('/add-post')
def add_post(item: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, item)

