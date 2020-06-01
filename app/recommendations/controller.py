import random
from typing import List, Dict, Union

from fastapi import APIRouter

from ..models.recommendations import Recommendations


router = APIRouter()


@router.get("/{recommend_type}/{user_id}", response_model=Recommendations)
async def get_user_rec(recommend_type: str, user_id: str) -> Recommendations:
    """Fetch user recommendation list for particular category

    Arguments:
        recommend_type -- the type of recommendation
        user_id -- id of the user
    Returns:
        recommendations -- list of recommendations
    """
    recommendations = [f"recommendation_{recommend_type}_{idx}" for idx in range(random.randint(3, 15))]
    return Recommendations(recommendations=recommendations)

