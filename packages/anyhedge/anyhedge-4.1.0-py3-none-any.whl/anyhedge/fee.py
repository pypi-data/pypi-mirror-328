# Built-in imports
from dataclasses import dataclass
from types import NoneType
from typing import Sequence

# Local imports
from .bch_primitives import (
    PositiveSats,
    Sats,
)
from .role import Role

# TODO: make an aggregate "FeeAgreements" that packs them up and makes them available in parts if desired
#       or in total with full consistency between parts and total. i.e. no discrepancy between total and sum of parts


@dataclass(frozen=True)
class FeeRequirement:
    name: str
    # note that amount is positive, with direction indicated by receiving role (and paying role in FeeAgreement)
    amount_sats: PositiveSats
    receiving: Role

    def __str__(self):
        return f'FeeRequirement ({self.name}): ____ --> {self.amount_sats} Sats ({self.amount_sats.bch} BCH) --> {self.receiving}'

    def __repr__(self):
        return self.__str__()

    def make_agreement(self, paying: Role):
        return FeeAgreement(
            name=self.name,
            amount_sats=self.amount_sats,
            receiving=self.receiving,
            paying=paying,
        )


@dataclass(frozen=True)
class FeeAgreement(FeeRequirement):
    paying: Role

    def __str__(self):
        return f'FeeAgreement ({self.name}): {self.paying} --> {self.amount_sats} Sats ({self.amount_sats.bch} BCH) --> {self.receiving}'

    def __repr__(self):
        return self.__str__()


def total_fee_sats_to_and_from_role(
        fees: Sequence[FeeAgreement],
        role: Role,
        fee_name: str | NoneType = None,
) -> Sats:
    """Following the convention that positive means to the role and negative means from."""
    sats_to_role = sum(fee.amount_sats for fee in fees_to_role(fees, role, fee_name))
    sats_from_role = sum(fee.amount_sats for fee in fees_from_role(fees, role, fee_name))
    return Sats(sats_to_role - sats_from_role)


def fees_to_role(
        fees: Sequence[FeeAgreement],
        role: Role,
        fee_name: str | None = None) -> list[FeeAgreement]:
    return [
        fee for fee in fees
        if (fee.receiving == role) and ((fee_name is None) or (fee.name == fee_name))
    ]


def fees_from_role(
        fees: Sequence[FeeAgreement],
        role: Role,
        fee_name: str | None = None) -> list[FeeAgreement]:
    return [
        fee for fee in fees
        if (fee.paying == role) and ((fee_name is None) or (fee.name == fee_name))
    ]
