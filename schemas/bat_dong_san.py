# from typing import List
# from pydantic import BaseModel

# class LoaiNhaDatBan(BaseModel):
#     id: str
#     ten: str
#     link: str

# class LoaiNhaDatChoThue(BaseModel):
#     id: str
#     ten: str
#     link: str

# class BatDongSan(BaseModel):
#     id: str
#     tieu_de: str
#     dia_chi_cu_the: str
#     gia: int
#     dien_tich: float
#     sdt: str
#     so_phong_ngu: int
#     mo_ta: str
#     nguoi_dang: str
#     anh: str
#     id_loai_ban: str
#     id_loai_thue: str
    
#     class Config:
#         orm_mode = True
from typing import Optional
from pydantic import BaseModel

class LoaiNhaDatBanBase(BaseModel):
    id: str
    ten: Optional[str] = None
    link: Optional[str] = None

class LoaiNhaDatBanCreate(LoaiNhaDatBanBase):
    pass

class LoaiNhaDatBan(LoaiNhaDatBanBase):
    class Config:
        orm_mode = True

class LoaiNhaDatChoThueBase(BaseModel):
    id: str
    ten: Optional[str] = None
    link: Optional[str] = None

class LoaiNhaDatChoThueCreate(LoaiNhaDatChoThueBase):
    pass

class LoaiNhaDatChoThue(LoaiNhaDatChoThueBase):
    class Config:
        orm_mode = True

class BatDongSanBase(BaseModel):
    id: str
    tieu_de: Optional[str] = None
    dia_chi_cu_the: Optional[str] = None
    gia: Optional[str] = None
    dien_tich: Optional[float] = None
    sdt: Optional[str] = None
    so_phong_ngu: Optional[int] = None
    mo_ta: Optional[str] = None
    nguoi_dang: Optional[str] = None
    anh: Optional[str] = None
    id_loai_ban: Optional[str] = None
    id_loai_thue: Optional[str] = None

class BatDongSanCreate(BatDongSanBase):
    pass

class BatDongSan(BatDongSanBase):

    class Config:
        orm_mode = True

