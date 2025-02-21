from atomict.api import get, post

COMPUTATION_TYPE_RELAXATION = 0
COMPUTATION_TYPE_SINGLE_POINT = 1

MODEL_ORB_D3_V2 = 0
MODEL_MATTERSIM_1_0_0_5M = 1


def get_mlrelax(id: str):
    """
    Get MLRelaxation
    """
    result = get(f"api/mlrelax/{id}/")
    return result


def associate_user_upload_with_mlrelaxation(user_upload_id: str, mlrelax_id: str):
    """
    Associate a user upload with a MLRelaxation
    """
    result = post(
        "api/mlrelax-file/",
        payload={"user_upload_id": user_upload_id, "mlrelax_id": mlrelax_id},
    )
    return result


def create_mlrelaxation(
    project_id: str,
    source_geometry_id: str,
    action: str,
    name: str = None,
    description: str = None,
    computation_type: int = COMPUTATION_TYPE_RELAXATION,
    f_max: float = None,
    model: int = MODEL_ORB_D3_V2,
    extra_simulation_kwargs: dict = None,
):
    """
    Create a MLRelaxation
    """

    if action not in ["DRAFT", "LAUNCH"]:
        raise ValueError("Action must be 'DRAFT' or 'LAUNCH'")

    if computation_type not in [
        COMPUTATION_TYPE_RELAXATION,
        COMPUTATION_TYPE_SINGLE_POINT,
    ]:
        raise ValueError(
            "Invalid computation type. Please use COMPUTATION_TYPE_RELAXATION (0) or COMPUTATION_TYPE_SINGLE_POINT (1)."
        )

    if model not in [MODEL_ORB_D3_V2, MODEL_MATTERSIM_1_0_0_5M]:
        raise ValueError(
            "Invalid model. Please use MODEL_ORB_D3_V2 (0) or MODEL_MATTERSIM_1_0_0_5M (1)."
        )

    payload = {
        "project": project_id,
        "source_geometry_id": source_geometry_id,
        "action": action,
        "name": name,
        "description": description,
        "computation_type": computation_type,
        "f_max": f_max,
        "model": model,
    }

    if extra_simulation_kwargs:
        payload.update(extra_simulation_kwargs)

    result = post("api/mlrelax/", payload)
    return result


def get_mlrelax_files(mlrelax_id: str):
    """
    Get the files associated with a MLRelaxation
    """
    result = get(f"api/mlrelax-file/?mlrelax__id={mlrelax_id}")
    return result
