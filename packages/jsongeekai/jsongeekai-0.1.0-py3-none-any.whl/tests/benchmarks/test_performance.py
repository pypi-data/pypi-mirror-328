"""
Performance benchmarks for JsonGeek
"""
import json
import pytest
from jsongeek import loads

# Sample JSON data of different sizes
SMALL_JSON = '{"key": "value", "numbers": [1, 2, 3]}'
MEDIUM_JSON = '[' + ','.join([SMALL_JSON] * 100) + ']'
LARGE_JSON = '[' + ','.join([MEDIUM_JSON] * 10) + ']'

@pytest.mark.benchmark(group="small")
def test_small_json_performance(benchmark):
    """Benchmark small JSON parsing"""
    def parse():
        return loads(SMALL_JSON)
    benchmark(parse)

@pytest.mark.benchmark(group="small")
def test_small_json_standard(benchmark):
    """Compare with standard json module (small)"""
    def parse():
        return json.loads(SMALL_JSON)
    benchmark(parse)

@pytest.mark.benchmark(group="medium")
def test_medium_json_performance(benchmark):
    """Benchmark medium JSON parsing"""
    def parse():
        return loads(MEDIUM_JSON)
    benchmark(parse)

@pytest.mark.benchmark(group="medium")
def test_medium_json_standard(benchmark):
    """Compare with standard json module (medium)"""
    def parse():
        return json.loads(MEDIUM_JSON)
    benchmark(parse)

@pytest.mark.benchmark(group="large")
def test_large_json_performance(benchmark):
    """Benchmark large JSON parsing"""
    def parse():
        return loads(LARGE_JSON)
    benchmark(parse)

@pytest.mark.benchmark(group="large")
def test_large_json_standard(benchmark):
    """Compare with standard json module (large)"""
    def parse():
        return json.loads(LARGE_JSON)
    benchmark(parse)
