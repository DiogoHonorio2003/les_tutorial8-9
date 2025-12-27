"""
system invariants

    - No duplicate users in users_db (unique emails)
    - A user can never access the system without entering the correct PIN.
    - No unauthorized account can be created, modified, or accessed during login.
    - The number of login attempts is accurately tracked for each user.
    - Only authenticated users can access financial data.
    - The system never alters account balances during a balance view operation.
    - The displayed balance must always reflect: Base Balance; Recent Transactions; Interest.
    - The account balance never decreases as a result of a deposit operation.
    - Invalid deposits (negative or zero amounts) do not modify any stored data.
    - Financial data integrity is maintained across all transactions.
    - Interest is only applied to accounts with a positive balance.
    - The interest_rate must always remain within a valid range (0 < rate ≤ 1).
    - The account balance never decreases due to interest application.
    - Notifications must always reflect the actual outcome of the interest process.
    - The total sum of all account balances remains constant.
    - Funds are never created or destroyed during a transfer.
    - Notifications are accurate and automatic.
    - No duplicate or irrelevant notifications are produced.
    - Invalid transfer attempts do not modify any account data.
    - Withdrawals never reduce the account balance below zero.
    - Successful withdrawals decrease the balance exactly by the withdrawn amount.

"""

"""
Register User Method

register_user(name: str, email: str, pin: str, initial_balance: float) -> AccountStatus
    
Requires:    
    - name must not be empty or None
    - email must not be empty or None and must contain '@' and '.'
    - pin must be 4 numeric digits string
    - initial_balance >= 0
    - user with same email must not already exist
    
Ensures:
    - If registration is successful:
        - new user is added to users_db
        - the system returns an AccountStatus indicating success
        - stored info matches inputs
        - stored balance equals initial_balance
        - a confirmation message is displayed to the user
        
    - If registration fails:
        - no changes occur to users_db
        - the system returns an AccountStatus indicating failure
        - appropriate error message is displayed to the user
        - the user remains on the registration page to correct input
"""


"""
Login Account Method

authenticate_user(email: str, entered_pin: str) -> LoginStatus
    
Requires:    
    - email must not be empty or None and must contain '@' and '.'
    - email must exist in the users_db
    - entered_pin must be a 4-digit numeric string
    - users_db[email] must have fields: 'pin', 'locked', 'login_attempts'
    - 'login_attempts' must be >= 0
    - if user['locked'] == True, no login should be allowed
    
Ensures:
    - If entered_pin == user['pin'] and not locked:
        - access_granted = True
        - login_attempts reset to 0
        - the system returns a LoginStatus indicating success
        - user gains access to all account features
        
    - If entered_pin != user['pin'] and not locked:
        - access_granted = False
        - login_attempts increases by 1
        - the system returns a LoginStatus indicating failure
        - the user remains on the login screen to reattempt login
        
    - If login_attempts >= 5: 
        - locked = True
        - The system returns a LoginStatus indicating account locked
        - further login attempts are blocked until account is unlocked
"""


"""
Consult Balance Method

view_balance(email: str) -> BalanceInfo
    
Requires:    
    - email must not be empty or None and must contain '@' and '.'
    - user must be logged in
    - email must exist in the users_db
    - user record must contain valid numeric fields for balance, transactions, and interest
    
Ensures:
    - If user is logged in and valid:
        - returned balance equals user balance 
        - returned interest equals user interest
        - returned transactions equals list of users transactions
        - no modification occurs to the users_db
        - the user receives confirmation that their balance has been successfully retrieved
        
    - If user is not logged in or invalid:
        - access is denied
        - the system does not return any balance information
        - an error message is returned indicating the issue
        - no modification occurs to the users_db
        - the user remains on the login or home screen until authenticated
"""

"""
Deposit Funds Method

deposit(email: str, amount: float) -> DepositStatus
    
Requires:    
    - email must not be empty or None and must contain '@' and '.'
    - user must be logged in
    - email must exist in the users_db
    - amount must be a valid number (float or int) greater than 0
    - the system must have access to the users current balance
    
Ensures:
    - If amount > 0:
        - user.balance = old_balance + amount
        - the updated balance is stored securely in the database
        - the system returns a DepositStatus indicating success
        
    - If amount <= 0:
        - user.balance = old_balance
        - the system returns a DepositStatus indicating failure
        - users_db structure remains valid
        - the user remains on the deposit page and may retry with a valid amount
"""

"""
Interest Accrual Method

interest(email: str, interest_rate: float) -> InterestStatus
    
Requires:
    - email must not be empty or None and must contain '@' and '.'
    - user must be logged in
    - email must exist in the users_db
    - user record must contain valid numeric fields for balance and interest_rate
    - the interest_rate must be a valid decimal value between 0 and 1, representing the annual percentage rate
    
Ensures:
    - If balance > 0:
        - new_balance = old_balance + (old_balance * interest_rate)
        - the system returns an InterestStatus indicating success
        - returns "Interest of $X applied."
        - the users updated balance is stored in the system database
        
    - If balance <= 0:
        - new_balance = old_balance
        - the system returns an InterestStatus indicating no interest accrued
        - returns "No interest accrued."
"""

"""
Notifications Method

Requires:    
    - user_email must exist in users_db
    - user record must include 'balance' and 'notifications'
    - balance must be a non-negative float
    - transaction_performed is a boolean
    - if transaction_performed == False, balance must remain unchanged
    - notifications list must contain only strings

    
Ensures:
    - If transaction_performed == True:
        - a new notification message is created
        - notification contains confirmation text and correct balance
        - message is appended exactly once to user['notifications']
        
    - If transaction_performed == False:
        - no new notifications are appended
        - balance remains unchanged
        
    - All messages remain unique (no duplicates)
    - Notifications are only about valid transactions (no irrelevant text)
    
"""


"""
Transfer Funds Method

transfer(sender_email: str, receiver_email: str, amount: float) -> TransferStatus

Requires:    
    - sender_email and receiver_email exist in users_db
    - sender_email ≠ recipient_email
    - amount is a float and represents millicent precision
    - sender.balance ≥ amount > 0
    - both users have non-negative balances
    - both users accounts must be active and not restricted.

Ensures:
    - If transfer is valid:
        - sender.balance decreases by exactly `amount`
        - recipient.balance increases by exactly `amount`
        - total system balance remains constant
        - both users receive corresponding notifications
        - the system returns a TransferStatus indicating success.

    - If the transfer is invalid:
        - no changes are made to either the senders or recipients balances.
        - the system returns a TransferStatus indicating failure.
    
"""

"""
Withdraw Funds Method

withdraw(email: str, amount: float) -> WithdrawalStatus

Requires:    
    - user_email must exist in users_db
    - amount is a positive float
    - user.balance >= 0
    - withdrawal amount must not exceed user balance
    - the system must have access to the users current balance.
 
Ensures:
    If withdrawal amount is valid:
        - user balance decreases by the exact amount
        - the system returns a WithdrawalStatus indicating success
        - user receives a confirmation notification
        
    If withdrawal amount is invalid:
        - user.balance remains unchanged
        - the system returns a WithdrawalStatus indicating failure
        - error message is set
        - the user remains on the withdrawal page to retry
            
"""

from dataclasses import dataclass, field
from typing import List, Dict

# ------------------- Data Structures -------------------
@dataclass
class User:
    name: str
    email: str
    pin: str
    balance: float
    logged_in: bool = False
    login_attempts: int = 0
    locked: bool = False
    transactions: List[str] = field(default_factory=list)
    interest_rate: float = 0.05
    notifications: List[str] = field(default_factory=list)

# ------------------- Status Classes -------------------
@dataclass
class AccountStatus:
    success: bool
    message: str

@dataclass
class LoginStatus:
    success: bool
    message: str

@dataclass
class BalanceInfo:
    balance: float
    transactions: List[str]
    interest: float
    message: str

@dataclass
class DepositStatus:
    success: bool
    message: str

@dataclass
class InterestStatus:
    success: bool
    message: str

@dataclass
class TransferStatus:
    success: bool
    message: str

@dataclass
class WithdrawalStatus:
    success: bool
    message: str

# ------------------- Database -------------------
users_db: Dict[str, User] = {}

# ------------------- Utility Functions -------------------
def valid_email(email: str) -> bool:
    return email and '@' in email and '.' in email

def valid_pin(pin: str) -> bool:
    return pin.isdigit() and len(pin) == 4

# ------------------- Methods -------------------
def register_user(name: str, email: str, pin: str, initial_balance: float) -> AccountStatus:
    if not name or not valid_email(email) or not valid_pin(pin) or initial_balance < 0:
        return AccountStatus(False, "Invalid registration input.")
    if email in users_db:
        return AccountStatus(False, "User already exists.")
    
    users_db[email] = User(name, email, pin, initial_balance)
    return AccountStatus(True, f"User {name} registered successfully with balance ${initial_balance:.2f}")

def authenticate_user(email: str, entered_pin: str) -> LoginStatus:
    if not valid_email(email) or not valid_pin(entered_pin):
        return LoginStatus(False, "Invalid email or PIN format.")
    if email not in users_db:
        return LoginStatus(False, "User does not exist.")
    
    user = users_db[email]
    if user.locked:
        return LoginStatus(False, "Account is locked due to too many failed login attempts.")
    
    if user.pin == entered_pin:
        user.logged_in = True
        user.login_attempts = 0
        return LoginStatus(True, "Login successful.")
    else:
        user.login_attempts += 1
        if user.login_attempts >= 5:
            user.locked = True
            return LoginStatus(False, "Account locked due to multiple failed attempts.")
        return LoginStatus(False, f"Incorrect PIN. Attempts: {user.login_attempts}")

def view_balance(email: str) -> BalanceInfo:
    if email not in users_db:
        return BalanceInfo(0, [], 0, "User does not exist.")
    user = users_db[email]
    if not user.logged_in:
        return BalanceInfo(0, [], 0, "Access denied. User not logged in.")
    return BalanceInfo(user.balance, list(user.transactions), user.interest_rate, "Balance retrieved successfully.")

def deposit(email: str, amount: float) -> DepositStatus:
    if email not in users_db:
        return DepositStatus(False, "User does not exist.")
    user = users_db[email]
    if not user.logged_in:
        return DepositStatus(False, "User not logged in.")
    if amount <= 0:
        return DepositStatus(False, "Deposit amount must be positive.")
    
    user.balance += amount
    user.transactions.append(f"Deposited ${amount:.2f}")
    user.notifications.append(f"Deposit successful. New balance: ${user.balance:.2f}")
    return DepositStatus(True, f"Deposited ${amount:.2f} successfully.")

def apply_interest(email: str, interest_rate: float) -> InterestStatus:
    if email not in users_db:
        return InterestStatus(False, "User does not exist.")
    user = users_db[email]
    if not user.logged_in:
        return InterestStatus(False, "User not logged in.")
    if not (0 < interest_rate <= 1):
        return InterestStatus(False, "Invalid interest rate.")
    if user.balance <= 0:
        return InterestStatus(False, "No interest accrued on zero or negative balance.")
    
    interest_amount = user.balance * interest_rate
    user.balance += interest_amount
    user.transactions.append(f"Interest applied: ${interest_amount:.2f}")
    user.notifications.append(f"Interest of ${interest_amount:.2f} applied. New balance: ${user.balance:.2f}")
    return InterestStatus(True, f"Interest of ${interest_amount:.2f} applied.")

def transfer(sender_email: str, receiver_email: str, amount: float) -> TransferStatus:
    if sender_email not in users_db or receiver_email not in users_db:
        return TransferStatus(False, "Sender or receiver does not exist.")
    if sender_email == receiver_email:
        return TransferStatus(False, "Cannot transfer to self.")
    
    sender = users_db[sender_email]
    receiver = users_db[receiver_email]
    if not sender.logged_in or not receiver.logged_in:
        return TransferStatus(False, "Both users must be logged in.")
    if amount <= 0 or sender.balance < amount:
        return TransferStatus(False, "Insufficient funds or invalid amount.")
    
    sender.balance -= amount
    receiver.balance += amount
    sender.transactions.append(f"Transferred ${amount:.2f} to {receiver_email}")
    receiver.transactions.append(f"Received ${amount:.2f} from {sender_email}")
    sender.notifications.append(f"Transferred ${amount:.2f} to {receiver_email}. New balance: ${sender.balance:.2f}")
    receiver.notifications.append(f"Received ${amount:.2f} from {sender_email}. New balance: ${receiver.balance:.2f}")
    return TransferStatus(True, f"Transferred ${amount:.2f} successfully.")

def withdraw(email: str, amount: float) -> WithdrawalStatus:
    if email not in users_db:
        return WithdrawalStatus(False, "User does not exist.")
    user = users_db[email]
    if not user.logged_in:
        return WithdrawalStatus(False, "User not logged in.")
    if amount <= 0 or amount > user.balance:
        return WithdrawalStatus(False, "Invalid withdrawal amount.")
    
    user.balance -= amount
    user.transactions.append(f"Withdrew ${amount:.2f}")
    user.notifications.append(f"Withdrawal of ${amount:.2f} successful. New balance: ${user.balance:.2f}")
    return WithdrawalStatus(True, f"Withdrew ${amount:.2f} successfully.")

