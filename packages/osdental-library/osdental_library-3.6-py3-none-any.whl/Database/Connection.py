import os
from typing import Dict, Tuple, Any
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from Exception.ControlledException import DatabaseException
from Utils.Code import DB_SUCCESS

load_dotenv()

class Connection:

    __engines_cache = {}

    def __init__(self, connection_string:str) -> None:
        self.engine = None
        self.connection_string = connection_string
        
    async def get_engine(self) -> AsyncEngine:
        if self.connection_string not in self.__engines_cache: 
            self.__engines_cache[self.connection_string] = create_async_engine(
                self.connection_string, 
                pool_size=15,  
                max_overflow=10, 
                pool_timeout=30,
                pool_recycle=1800,
                echo=os.getenv('DB_DEBUG', 'False').lower() == 'true', 
                pool_pre_ping=True
            )

        return self.__engines_cache[self.connection_string]

    async def get_session(self) -> AsyncSession:
        self.engine = await self.get_engine()
        session_factory = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
        return session_factory()

    async def execute_query_return_first_value(self, query:str, params:Dict[str, Any] = None) -> Any:
        async with (await self.get_session()) as session:
            async with session.begin():
                result = await session.execute(text(query), params)
                return result.scalar()

    async def execute_query_return_data(self, query:str, params:Dict[str, Any] = None, fetchone=False) -> Tuple[Any, Any]:
        async with (await self.get_session()) as session:
            async with session.begin():
                result = await session.execute(text(query), params)
                keys = result.keys()
                if fetchone:
                    return dict(zip(keys, result.fetchone()))
                
                return [dict(zip(keys, row)) for row in result.fetchall()] 

    async def execute_query_return_message(self, query:str, params:Dict[str, Any] = None, code:str = DB_SUCCESS) -> str:
        async with (await self.get_session()) as session:
            async with session.begin():
                result = await session.execute(text(query), params)
                row = result.fetchone() 
                if row.STATUS_CODE != code:
                    raise DatabaseException(error=row.STATUS_MESSAGE, status_code=row.STATUS_CODE)

                return row.STATUS_MESSAGE
                
    async def execute_query(self, query:str, params:Dict[str, Any] = None) -> str:
        async with (await self.get_session()) as session:
            async with session.begin():
                await session.execute(text(query), params)


    async def close_engine(self) -> None:
        if self.engine:
            await self.engine.dispose()

        # Delete engine from cache if it exists
        if self.connection_string in self.__engines_cache:
            del self.__engines_cache[self.connection_string]