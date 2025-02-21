import numpy as np


class Caster:

    def __init__(self, input_vector: np.ndarray) -> None:
        self._castable_type = input_vector.dtype
        self._uncastable_type = np.float32

    def cast(self, vector: np.ndarray) -> np.ndarray:  # A → B 변환
        assert (
            vector.dtype == self._castable_type
        ), f"ERROR, The vector's type must be {self._castable_type}"
        return vector.astype(self._uncastable_type)

    def uncast(self, vector: np.ndarray) -> np.ndarray:  # B → A 복구
        assert (
            vector.dtype == self._uncastable_type
        ), f"ERROR, The vector's type must be {self._uncastable_type}"
        return np.clip(
            vector,
            np.iinfo(self._castable_type).min,
            np.iinfo(self._castable_type).max,
        ).astype(self._castable_type)
