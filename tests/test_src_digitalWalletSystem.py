import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import digitalWalletSystem as module_0



def test_case_0():
    str_0 = "*m"
    account_status_0 = module_0.register_user(str_0, str_0, str_0, str_0)
    assert (
        f"{type(account_status_0).__module__}.{type(account_status_0).__qualname__}"
        == "src.digitalWalletSystem.AccountStatus"
    )
    assert account_status_0.success is False
    assert account_status_0.message == "Invalid registration input."
    assert module_0.users_db == {}


def test_case_1():
    str_0 = "E^G)"
    bool_0 = module_0.valid_pin(str_0)
    assert bool_0 is False
    assert module_0.users_db == {}


def test_case_2():
    str_0 = ";/35|],'"
    bool_0 = False
    float_0 = 3204.93135
    account_status_0 = module_0.register_user(bool_0, bool_0, str_0, float_0)
    assert account_status_0.success is False
    assert account_status_0.message == "Invalid registration input."
    assert module_0.users_db == {}


def test_case_3():
    str_0 = "(0["
    login_status_0 = module_0.authenticate_user(str_0, str_0)
    assert login_status_0.message == "Invalid email or PIN format."
    assert module_0.users_db == {}


def test_case_4():
    str_0 = "^"
    balance_info_0 = module_0.view_balance(str_0)
    assert (
        f"{type(balance_info_0).__module__}.{type(balance_info_0).__qualname__}"
        == "src.digitalWalletSystem.BalanceInfo"
    )
    assert balance_info_0.balance == 0
    assert balance_info_0.transactions == []
    assert balance_info_0.interest == 0
    assert balance_info_0.message == "User does not exist."
    assert module_0.users_db == {}


def test_case_5():
    str_0 = "*m"
    deposit_status_0 = module_0.deposit(str_0, str_0)
    assert (
        f"{type(deposit_status_0).__module__}.{type(deposit_status_0).__qualname__}"
        == "src.digitalWalletSystem.DepositStatus"
    )
    assert deposit_status_0.success is False
    assert deposit_status_0.message == "User does not exist."
    assert module_0.users_db == {}


def test_case_6():
    str_0 = "H"
    interest_status_0 = module_0.apply_interest(str_0, str_0)
    assert (
        f"{type(interest_status_0).__module__}.{type(interest_status_0).__qualname__}"
        == "src.digitalWalletSystem.InterestStatus"
    )
    assert interest_status_0.success is False
    assert interest_status_0.message == "User does not exist."
    assert module_0.users_db == {}


def test_case_7():
    str_0 = "*m"
    transfer_status_0 = module_0.transfer(str_0, str_0, str_0)
    assert transfer_status_0.message == "Sender or receiver does not exist."
    assert module_0.users_db == {}


def test_case_8():
    str_0 = "*m"
    withdrawal_status_0 = module_0.withdraw(str_0, str_0)
    assert (
        f"{type(withdrawal_status_0).__module__}.{type(withdrawal_status_0).__qualname__}"
        == "src.digitalWalletSystem.WithdrawalStatus"
    )
    assert withdrawal_status_0.success is False
    assert withdrawal_status_0.message == "User does not exist."
    assert module_0.users_db == {}


def test_case_9():
    str_0 = ">Z/"
    login_status_0 = module_0.authenticate_user(str_0, str_0)
    assert login_status_0.message == "Invalid email or PIN format."
    assert module_0.users_db == {}
    balance_info_0 = module_0.view_balance(str_0)
    assert (
        f"{type(balance_info_0).__module__}.{type(balance_info_0).__qualname__}"
        == "src.digitalWalletSystem.BalanceInfo"
    )
    assert balance_info_0.balance == 0
    assert balance_info_0.transactions == []
    assert balance_info_0.interest == 0
    assert balance_info_0.message == "User does not exist."


def test_case_10():
    str_0 = ""
    bool_0 = module_0.valid_pin(str_0)
    assert module_0.users_db == {}


def test_case_11():
    str_0 = ""
    login_status_0 = module_0.authenticate_user(str_0, str_0)
    assert login_status_0.message == "Invalid email or PIN format."
    assert module_0.users_db == {}


def test_case_12():
    str_0 = 'v4Q"'
    account_status_0 = module_0.register_user(str_0, str_0, str_0, str_0)
    assert (
        f"{type(account_status_0).__module__}.{type(account_status_0).__qualname__}"
        == "src.digitalWalletSystem.AccountStatus"
    )
    assert account_status_0.success is False
    assert account_status_0.message == "Invalid registration input."
    assert module_0.users_db == {}
