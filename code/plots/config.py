"""Common configs for plots"""


class Base():
    font = {
            'family': 'Times New Roman',
            'size': 16,
            }


class Legend(Base):
    font = {**Base.font, 'weight': 'bold'}


class Tick(Base):
    font = {**Base.font, 'size': 12}
