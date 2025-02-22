from typing import Annotated, Callable, Awaitable, Dict, List
from faststream.rabbit import RabbitBroker, RabbitExchange

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession

from fastapi import Depends


from cattle_grid.model.extension import MethodInformationModel
from cattle_grid.config.messaging import broker, internal_exchange, exchange

from .globals import get_engine, get_transformer, get_method_information

SqlAsyncEngine = Annotated[AsyncEngine, Depends(get_engine)]
"""Returns the SqlAlchemy AsyncEngine"""

Transformer = Annotated[Callable[[Dict], Awaitable[Dict]], Depends(get_transformer)]
"""The transformer loaded from extensions"""

Broker = Annotated[RabbitBroker, Depends(broker)]
"""The RabbitMQ broker"""
InternalExchange = Annotated[RabbitExchange, Depends(internal_exchange)]

ActivityExchange = Annotated[RabbitExchange, Depends(exchange)]
"""The Activity Exchange"""


MethodInformation = Annotated[
    List[MethodInformationModel], Depends(get_method_information)
]
"""Returns the information about the methods that are a part of the exchange"""


async def with_fast_api_session(sql_engine: SqlAsyncEngine):
    async with async_sessionmaker(sql_engine)() as session:
        yield session


SqlSession = Annotated[AsyncSession, Depends(with_fast_api_session)]
"""Session annotation to be used with FastAPI"""
