from enum import Enum
from typing import Dict, List


class RepaymentMethod(str, Enum):
    EQUATED_MONTHLY_INSTALLMENT = "EQUATED_MONTHLY_INSTALLMENT"
    AMORTIZING_LOAN = "AMORTIZING_LOAN"

    @classmethod
    def list(cls):
        return list(map(lambda method: method.value, cls))


def calculate_principal_and_interest(
    amount_of_loans: int, expiration: int, interest_rate: float, repayment_method: str
) -> Dict[str, List[int]]:
    """
    입력: 대출액(amount of loans), 만기(expiration), 금리(interest rate), 상환 방식(repayment method)
    출력: 원금 리스트(principal), 이자 리스트(interest)
    """
    if not is_valid_repayment_method(repayment_method=repayment_method):
        raise AssertionError("repayment method not valid")

    calculate_function_per_repayment_method = {
        RepaymentMethod.EQUATED_MONTHLY_INSTALLMENT: calculate_equated_monthly_installment,
        RepaymentMethod.AMORTIZING_LOAN: calculate_amortizing_loan,
    }

    return calculate_function_per_repayment_method[repayment_method](
        amount_of_loans=amount_of_loans, expiration=expiration, interest_rate=interest_rate
    )


def is_valid_repayment_method(repayment_method: str) -> bool:
    return repayment_method in RepaymentMethod.list()


def calculate_equated_monthly_installment(
    amount_of_loans: int, expiration: int, interest_rate: float
) -> Dict[str, List[int]]:
    """
    원리금 균등 상환
    """
    interest_rate_per_month = interest_rate / 12 / 100

    equated_monthly_installment_amount = int(
        amount_of_loans
        * interest_rate_per_month
        * ((1 + interest_rate_per_month) ** expiration)
        / ((1 + interest_rate_per_month) ** expiration - 1)
    )

    monthly_principal = int(amount_of_loans / expiration)
    floating_point_difference = amount_of_loans - monthly_principal * expiration
    principal_list = [monthly_principal for _ in range(expiration)]
    principal_list[-1] += floating_point_difference

    interest_amount = equated_monthly_installment_amount * expiration - amount_of_loans
    monthly_interest = int(interest_amount / expiration)
    floating_point_difference = interest_amount - monthly_interest * expiration
    interest_list = [monthly_interest for _ in range(expiration)]
    interest_list[-1] += floating_point_difference

    return {
        "principal": principal_list,
        "interest": interest_list,
    }


def calculate_amortizing_loan(
    amount_of_loans: int, expiration: int, interest_rate: float
) -> Dict[str, List[int]]:
    interest_amount = int(amount_of_loans * interest_rate / 100)

    monthly_interest = int(interest_amount / expiration)
    floating_point_difference = interest_amount - monthly_interest * expiration
    interest_list = [monthly_interest for _ in range(expiration)]
    interest_list[-1] += floating_point_difference

    principal_list = [0 for _ in range(expiration)]
    principal_list[-1] += amount_of_loans

    return {
        "principal": principal_list,
        "interest": interest_list,
    }


def test_calculate_principal_and_interest():
    # amortizing test
    amortizing_loan_result = calculate_principal_and_interest(
        amount_of_loans=1_000_000,
        expiration=12,
        interest_rate=3.0,
        repayment_method=RepaymentMethod.AMORTIZING_LOAN,
    )

    amortizing_principal_and_interest = 0
    for value_list in amortizing_loan_result.values():
        amortizing_principal_and_interest += sum(value_list)
    assert amortizing_principal_and_interest == 1_030_000

    # emi test
    emi_loan_result = calculate_principal_and_interest(
        amount_of_loans=1_000_000,
        expiration=12,
        interest_rate=3.0,
        repayment_method=RepaymentMethod.EQUATED_MONTHLY_INSTALLMENT,
    )

    emi_principal_and_interest = 0
    for value_list in emi_loan_result.values():
        emi_principal_and_interest += sum(value_list)
    assert emi_principal_and_interest == 1_016_316


def test_is_valid_repayment_method():
    assert is_valid_repayment_method(repayment_method=RepaymentMethod.EQUATED_MONTHLY_INSTALLMENT)
    assert is_valid_repayment_method(repayment_method=RepaymentMethod.AMORTIZING_LOAN)
    assert not is_valid_repayment_method(repayment_method="BILL")


if __name__ == "__main__":
    amortizing_loan_principal_and_interest = calculate_principal_and_interest(
        amount_of_loans=1_000_000,
        expiration=12,
        interest_rate=3.0,
        repayment_method=RepaymentMethod.AMORTIZING_LOAN,
    )
    print(amortizing_loan_principal_and_interest)

    emi_loan_principal_and_interest = calculate_principal_and_interest(
        amount_of_loans=10_000_000,
        expiration=24,
        interest_rate=5.0,
        repayment_method=RepaymentMethod.EQUATED_MONTHLY_INSTALLMENT,
    )
    print(emi_loan_principal_and_interest)
