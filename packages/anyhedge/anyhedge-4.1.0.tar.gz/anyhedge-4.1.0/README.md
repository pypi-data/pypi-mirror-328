# anyhedge

Basic components for AnyHedge contracts.

Currently, this only deals with contract execution and focuses on sats-accurate values in relation
to the reference typescript [AnyHedge Library](http://gitlab.com/generalProtocols/anyhedge/library).


## Install

`pip install anyhedge` (use venv, miniconda, etc. - don't install things on your system python)


## Requirements

- `python >= 3.10` (use venv, miniconda, etc. - don't install things on your system python)
- `requirements.txt` (`pip install -r requirements.txt` using your virtual python)


## Demo

`python demo.py`

You should see something like this:

```
ContractProposal(start_timestamp=1668818394 (2022-11-19T00:39:54+00:00),
                 maturity_timestamp=1668829194 (2022-11-19T03:39:54+00:00),
                 nominal_oracleUnits_x_satsPerBch=10000000000000,
                 start_price_oracleUnits_per_bch=10000,
                 low_liquidation_price_oracleUnits_per_bch=7143,
                 oracle_public_key='02d3c1de9d4bc77d6c3608cbe44d10138c7488e592dc2b1e10a6cf0e92c2ecb047',
                 maker_side=Hedge)
That is a $1000.0 Long Taker contract.

ContractFunding(base_proposal=...,
                fee_agreements=(FeeAgreement (maker fee): Taker --> 1000 Sats (1e-05 BCH) --> Maker,
                                FeeAgreement (settlement service fee): Taker --> 2000 Sats (2e-05 BCH) --> Settlement Service))
That is a contract funding with a total of 1e-05 BCH in fees to Maker.

ContractRedemption(base_funding=...,
                   end_price_timestamp=1668829194 (2022-11-19T03:39:54+00:00),
                   naive_end_price_oracleUnits_per_bch=11000,
                   redemption_type=Maturation)
That is a redemption paying 4.90881092 BCH to Taker versus their original 3.99972001 BCH for a gain of 22.728113661135996%.
```
