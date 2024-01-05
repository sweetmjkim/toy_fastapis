# --------------------------------------------------------------------
# 기본 형태
# from typing import Any, List, Optional
# from beanie import init_beanie, PydanticObjectId
# from models.users import User
# from motor.motor_asyncio import AsyncIOMotorClient
# from pydantic import BaseModel
# 변경 후 코드
# from pydantic_settings import BaseSettings
# class Settings(BaseSettings):
#     DATABASE_URL: Optional[str] = None
#     async def initialize_database(self):
#         client = AsyncIOMotorClient(self.DATABASE_URL)
#         await init_beanie(database=client.get_default_database(),
#                           document_models=[User])
# --------------------------------------------------------------------

from typing import Any, List, Optional

from beanie import init_beanie, PydanticObjectId
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
# 변경 후 코드
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None        # mongodb에 접속 + database 연결 + collection 작업 을 한번에 해준다.

    async def initialize_database(self):            # async는 펑션 앞에 둔다. 그리고 await는 같이 다닌다.(네트워크 신호를 맞추기 위해서 사용한다.)
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[User])
        
    class Config:           # IP 주소를 암호화 하기위해 따로 관리한다. 파일명 : .env
        env_file = ".env"