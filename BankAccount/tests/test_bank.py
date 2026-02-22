import pytest
from banks.bank import BankAccount

############################################################################################
#Tests for BankAccount.__init__

def test_init_ok():
    a = BankAccount("Sasha", 100)
    assert a.owner == "Sasha"
    assert a.balance == 100
    assert a.history == []

def test_init_owner_not_type_raises_int():
    with pytest.raises(TypeError, match="Owner must be a string"):
        BankAccount(1, 100)

def test_init_owner_not_type_raises_bool():
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

def test_deposit_ok():
    a = BankAccount("Sasha", 100)
    a.deposit(50)
    assert a.balance == 150
    assert a.history == ["DEPOSIT +50"] 

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

def test_withdraw_ok():
    a = BankAccount("Sasha", 100)
    a.withdraw(20)
    assert a.balance == 80
    assert a.history == ["WITHDRAW -20"]

def test_withdraw_negative_amount_raises():
    a = BankAccount("Sasha", 100)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        a.withdraw(-10)

def test_withdraw_zero_amount_raises():
    a = BankAccount("Sasha", 100)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        a.withdraw(0)

def test_withdraw_insufficient_funds_raises():
    a = BankAccount("Sasha", 10)
    with pytest.raises(ValueError, match="Not enough money"):
        a.withdraw(20)