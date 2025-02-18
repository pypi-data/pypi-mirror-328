# Author: Lihao Wang (lihaowang@yahoo.com)
import inspect


def view(v, k=None, indent=0, is_DC=False):
    """
    Recursively prints deep learning-related data structures in a human-friendly format.

    Args:
        v: The value to be printed, which can be a dictionary, list, tuple, ndarray, Tensor, mmcv DataContainer, etc.
        k (str): The key associated with the value.
        indent (int): The indentation level for printing, used for hierarchical structures.
        is_DC (bool): Flag to indicate if the current value is an mmcv DataContainer.

    """
    if k is None:
        frame = inspect.currentframe().f_back
        for var_name, var_value in frame.f_locals.items():
            if var_value is v:
                k = var_name  # Get the variable name
                break
        else:
            k = "root"

    DC_flag = " (DC)" if is_DC else ""

    if isinstance(v, dict):
        print(" " * indent + f"|-- {k}{DC_flag}")
        sub_indent = indent + 4
        for sub_k, sub_v in v.items():
            view(sub_v, sub_k, sub_indent)
    elif type(v).__name__ == "DataContainer":    # mmcv DataContainer
        view(v.data, k, indent, is_DC=True)
    elif isinstance(v, list) or isinstance(v, tuple):
        print(" " * indent + f"|-- {k}{DC_flag}: {type(v).__name__} of len {len(v)}")
        sub_indent = indent + 4
        for i, ele in enumerate(v):
            view(ele, str(i), sub_indent)
    elif type(v).__name__ == "ndarray" or type(v).__name__ == "Tensor":  # numpy.ndarray & torch.Tensor
        if (type(v).__name__ == "ndarray" and v.size == 0) or (type(v).__name__ == "Tensor" and v.numel() == 0):
            v_min, v_max = "N/A", "N/A"
        else:
            v_min, v_max = f"{v.min():.2f}", f"{v.max():.2f}"
        print(" " * indent + f"|-- {k}{DC_flag}: {type(v).__name__} of shape {list(v.shape)}, "
                             f"dtype {v.dtype}, min {v_min}, max {v_max}")
    else:
        print(" " * indent + f"|-- {k}{DC_flag}: {v}")

