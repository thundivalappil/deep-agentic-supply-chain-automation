from typing import Any, Dict

import pandas as pd

from src.agents.demand_agent import evaluate_demand
from src.agents.inventory_agent import evaluate_inventory
from src.agents.procurement_agent import evaluate_procurement
from src.agents.logistics_agent import evaluate_logistics
from src.agents.finance_agent import evaluate_finance
from src.agents.risk_agent import evaluate_risk


def run_agentic_orchestration(
    forecast_df: pd.DataFrame,
    inventory_df: pd.DataFrame,
    suppliers_df: pd.DataFrame,
    plan_df: pd.DataFrame,
) -> Dict[str, Any]:
    demand_view = evaluate_demand(forecast_df)
    inventory_view = evaluate_inventory(plan_df)
    procurement_view = evaluate_procurement(plan_df)
    logistics_view = evaluate_logistics(plan_df)
    finance_view = evaluate_finance(plan_df)
    risk_view = evaluate_risk(plan_df)

    executive_action = (
        "Prioritize high-urgency SKUs, place purchase orders for critical items, "
        "watch high-risk suppliers, and review cash impact before large replenishment batches."
    )

    return {
        "demand_agent": demand_view,
        "inventory_agent": inventory_view,
        "procurement_agent": procurement_view,
        "logistics_agent": logistics_view,
        "finance_agent": finance_view,
        "risk_agent": risk_view,
        "executive_action": executive_action,
    }
