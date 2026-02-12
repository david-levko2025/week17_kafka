from fastapi import APIRouter
import dal


router = APIRouter(prefix="/analytics",tags=["Customers"])


@router.get("top-customers")
def get_10_client_with_max_orders():
    return dal.get_10_client_with_max_orders()

@router.get("customers-without-orders")
def get_client_withnt_ordres():
    return dal.get_client_withnt_ordres()

@router.get("zero-credit-active-customers")
def get_client_withnt_credit_limit():
    return dal.get_client_withnt_credit_limit()