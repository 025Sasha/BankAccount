import pytest
from bank.bank import BankAccount

@pytest.fixture
def sasha():
    return BankAccount("Sasha", 100)

@pytest.fixture
def masha():
    return BankAccount("Masha", 10)

############################################################################################
#Tests for BankAccount.__init__

def test_init_ok(sasha):
    assert sasha.owner == "Sasha"
    assert sasha.balance == 100
    assert sasha.history == []

def test_init_owner_not_type_raises_int():
    with pytest.raises(TypeError, match="Owner must be a string"):
        BankAccount(1, 100)

def test_init_balance_not_type_raises_bool():
    with pytest.raises(TypeError, match="Balance must be an integer or float"):
        BankAccount("Sasha", True)

def test_init_balance_not_type_raises_str():
    with pytest.raises(TypeError, match="Balance must be an integer or float"):
        BankAccount("Sasha", "1")

def test_init_negative_balance_raises():
    with pytest.raises(ValueError, match="Balance can't be negative"):
        BankAccount("Sasha", -1)

##########################################################################################
#Tests for BankAccount.deposit

def test_deposit_ok(sasha):
    sasha.deposit(50)
    assert sasha.balance == 150
    assert sasha.history == ["DEPOSIT +50"] 

def test_deposit_negative_amount_raises():
    a = BankAccount("Sasha", 100)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        a.deposit(-10)

def test_deposit_zero_amount_raises():
    a = BankAccount("Sasha", 100)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        a.deposit(0)

##########################################################################################
#Tests for BankAccount.withdraw

def test_withdraw_ok(sasha):
    sasha.withdraw(20)
    assert sasha.balance == 80
    assert sasha.history == ["WITHDRAW -20"]

def test_withdraw_negative_amount_raises(sasha):
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        sasha.withdraw(-10)

def test_withdraw_zero_amount_raises(sasha):
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        sasha.withdraw(0)

def test_withdraw_insufficient_funds_raises(sasha):
    with pytest.raises(ValueError, match="Not enough money"):
        sasha.withdraw(101)

##########################################################################################
#Tests for BankAccount.transfer_to

def test_transfer_to_ok(sasha, masha):
    S_balance = sasha.balance
    M_balance = masha.balance
    tmp = 1

    sasha.transfer_to(masha, tmp)

    assert sasha.balance == S_balance - tmp
    assert masha.balance == M_balance + tmp
    assert sasha.history[-1] == f"TRANSFER_OUT -{tmp} to {masha.owner}"
    assert masha.history[-1] == f"TRANSFER_IN +{tmp} from {sasha.owner}"

def test_transfer_to_not_enough_money_raises_value_error(sasha, masha):
    with pytest.raises(ValueError, match = "Not enough money"):
        sasha.transfer_to(masha, sasha.balance + 1)

def test_transfer_to_none_raises(sasha):
    with pytest.raises(ValueError, match="Target account is missing"):
        sasha.transfer_to(None, 10)

def test_transfer_to_wrong_type_raises(sasha):
    with pytest.raises(TypeError, match="Target must be a BankAccount"):
        sasha.transfer_to("not account", 10)   