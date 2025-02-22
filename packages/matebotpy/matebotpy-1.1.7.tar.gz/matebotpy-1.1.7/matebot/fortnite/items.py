from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CosmeticIconLegoElement:
    wide: str
    small: str
    large: str

@dataclass
class CosmeticIconLego:
    first: CosmeticIconLegoElement
    second: CosmeticIconLegoElement

    def __post_init__(self):
        if isinstance(self.first, dict):
            self.first = CosmeticIconLegoElement(**self.first)
        if isinstance(self.second, dict):
            self.second = CosmeticIconLegoElement(**self.second)

@dataclass
class CosmeticIcon:
    small: str
    large: str

@dataclass
class CosmeticVariantPart:
    name: str
    icon: str
    isDefault: bool
    tag: str

@dataclass
class CosmeticVariant:
    channel: str
    tag: str
    parts: List[CosmeticVariantPart]

@dataclass
class Cosmetic:
    name: str
    description: str
    shortDescription: str
    rarity: str
    lastseen: str
    variants: List[CosmeticVariant]
    tags: List[str]
    icon: CosmeticIcon

    def __post_init__(self):
        self.variants = [CosmeticVariant(**variant) for variant in self.variants]
        if isinstance(self.icon, dict):
            self.icon = CosmeticIcon(**self.icon)

@dataclass
class Character:
    name: str
    description: str
    shortDescription: str
    gender: str
    rarity: str
    lastseen: str
    variants: List[CosmeticVariant]
    tags: List[str]
    icon: CosmeticIcon
    bean: Optional[CosmeticIcon]
    lego: Optional[CosmeticIconLego]

    def __post_init__(self):
        self.variants = [CosmeticVariant(**variant) for variant in self.variants]
        if isinstance(self.icon, dict):
            self.icon = CosmeticIcon(**self.icon)
        if self.bean and isinstance(self.bean, dict):
            self.bean = CosmeticIcon(**self.bean)
        if self.lego and isinstance(self.lego, dict):
            self.lego = CosmeticIconLego(**self.lego)

@dataclass
class Juno:
    name: str
    rarity: str
    lastseen: str
    tags: List[str]
    icon: CosmeticIcon

    def __post_init__(self):
        if isinstance(self.icon, dict):
            self.icon = CosmeticIcon(**self.icon)

@dataclass
class CarCosmetic:
    name: str
    description: str
    shortDescription: str
    lastseen: str
    variants: List[CosmeticVariant]
    tags: List[str]
    icon: CosmeticIcon

    def __post_init__(self):
        self.variants = [CosmeticVariant(**variant) for variant in self.variants]
        if isinstance(self.icon, dict):
            self.icon = CosmeticIcon(**self.icon)

@dataclass
class CosmeticVariantToken:
    cosmetic: str
    channelTag: str
    nameTag: str
    name: str
    description: str
    lastseen: str
    shortDescription: str
    tags: List[str]
    icon: CosmeticIcon

    def __post_init__(self):
        if isinstance(self.icon, dict):
            self.icon = CosmeticIcon(**self.icon)

@dataclass
class CosmeticVehicleVariantAdditional:
    channelTag: str
    variantTag: str

@dataclass
class CosmeticVehicleVariant:
    cosmetic: str
    channelTag: str
    nameTag: str
    name: str
    lastseen: str
    description: str
    shortDescription: str
    rarity: str
    additional: List[CosmeticVehicleVariantAdditional]

    def __post_init__(self):
        self.additional = [CosmeticVehicleVariantAdditional(**additional) for additional in self.additional]

@dataclass
class Instrument:
    name: str
    description: str
    shortDescription: str
    rarity: str
    lastseen: str
    variants: List[CosmeticVariant]
    tags: List[str]
    icon: CosmeticIcon

    def __post_init__(self):
        self.variants = [CosmeticVariant(**variant) for variant in self.variants]
        if isinstance(self.icon, dict):
            self.icon = CosmeticIcon(**self.icon)