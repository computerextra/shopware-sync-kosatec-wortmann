import attrs


@attrs.define
class C_Uvp(object):
    Artikelnummer: str | None = None
    Brutto: float | None = None
    Netto: float | None = None


@attrs.define
class C_CustomAufschlag(object):
    Kategorie: str | None = None
    Prozent: int | None = None


@attrs.define
class C_CategoryName(object):
    name: str | None = None


@attrs.define
class C_ManualCategories(object):
    name: str | None = None
    children: list[C_CategoryName] | None = None


@attrs.define
class C_CategoryOverride(object):
    old: str | None = None
    new: str | None = None
    index: int | None = None


@attrs.define
class Config(object):
    Aufschlag: int | None = None
    CustomAufschlag: list[C_CustomAufschlag] | None = None
    IgnoredCategories: list[str] | None = None
    IgnoredProducts: list[str] | None = None
    ManualCategories: list[C_ManualCategories] | None = None
    CategoryOverride: list[C_CategoryOverride] | None = None
    Uvp: list[C_Uvp] | None = None
