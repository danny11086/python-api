from pydantic import BaseModel
from typing import List, Optional

class SubImageInfoObject(BaseModel):
    ImageID: str
    EventSort: int
    DeviceID: str
    StoragePath: str
    Type: str
    FileFormat: str
    ShotTime: str
    Width: int
    Height: int

class SubImageList(BaseModel):
    SubImageInfoObject: List[SubImageInfoObject]

class DetectionObject(BaseModel):
    DetectionID: str
    DetectionType: int
    DeviceID: str
    FaultType: int
    FaultArea: str
    AlarmTime: str
    SubImageList: SubImageList
    TaskID: str
    PlateNo: str
    CrowdCount: int
    AlgModelType: str

class DetectionListObject(BaseModel):
    DetectionObject: List[DetectionObject]

class AlarmCallback(BaseModel):
    DetectionListObject: DetectionListObject
