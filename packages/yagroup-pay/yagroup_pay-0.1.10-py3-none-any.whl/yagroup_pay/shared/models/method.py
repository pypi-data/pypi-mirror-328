#
# (c) 2025, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from typing import Optional

from sqlmodel import SQLModel

from .base import BaseDbModel
from sqlalchemy import JSON
from sqlmodel import Field, Relationship

from ..enums.method_type import MethodType
from .user import User


class Method(BaseDbModel, table=True):
    __tablename__ = 'methods'

    user_id: int = Field(foreign_key='users.id')
    user: User = Relationship(sa_relationship_kwargs={'lazy': 'joined'})

    type: MethodType
    data: dict = Field(default={}, sa_type=JSON)
    balance: float
    position: int = Field(default=0)
    tg_message_id: Optional[int]
    on_payment: bool = Field(default=False)


class RussianBankMethodData(SQLModel):
    bank_name: str
    fullname: str
    sbp: Optional[int]
    card: Optional[str] = Field(default=None)


class USDTMethodData(SQLModel):
    address: str


class ZelleMethodData(SQLModel):
    value: str
    fullname: str


METHODS = {
    MethodType.RUSSIAN_BANK: RussianBankMethodData,
    MethodType.ZELLE: ZelleMethodData,
    MethodType.USDT_TRC20: USDTMethodData,
}
