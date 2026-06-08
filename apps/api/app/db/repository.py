from typing import Generic, Type, TypeVar
from sqlmodel import Session, SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)

class Repository(Generic[ModelType]):
    def __init__(self, session: Session, model: Type[ModelType]):
        self.session = session
        self.model = model

    def get(self, id: int) -> ModelType | None:
        return self.session.get(self.model, id)

    def list(self, offset: int = 0, limit: int = 100) -> list[ModelType]:
        statement = select(self.model).offset(offset).limit(limit)
        return self.session.exec(statement).all()

    def add(self, item: ModelType) -> ModelType:
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def delete(self, item: ModelType) -> None:
        self.session.delete(item)
        self.session.commit()
