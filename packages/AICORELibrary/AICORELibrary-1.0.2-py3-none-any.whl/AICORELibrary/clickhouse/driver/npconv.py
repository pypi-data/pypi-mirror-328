from AICORELibrary.clickhouse.driver.options import np

from AICORELibrary.clickhouse.driver.types import ByteSource


def read_numpy_array(source: ByteSource, np_type: str, num_rows: int):
    dtype = np.dtype(np_type)
    buffer = source.read_bytes(dtype.itemsize * num_rows)
    return np.frombuffer(buffer, dtype, num_rows)
