from pydantic import BaseModel


class User(BaseModel):
    nickname: str
    avatar: str
    phone: bool
    email: bool
    # payMethods: dict


class AvailableVolume(BaseModel):
    tradeUSDTNum30: float


class Price(BaseModel):
    asset: str
    fiat: str
    value: str


class OrderLimitsIn(BaseModel):
    minAmount: str
    maxAmount: str


class PmEpyd(BaseModel):
    id: int
    name: str
    mainColor: str
    icon: str
    number: int
