from dataclasses import dataclass
from typing import Literal
import tyro
from pylsf.available_resources import ClusterUsageAnalyzer

def check_gpus(watch: bool = False, # Whether to watch GPU usage
               interval: float = 5.0, # Refresh interval in seconds when watching
               detailed: bool = False # Show detailed information about each GPU
               ):
    """Check GPU usage across the cluster"""
    analyzer = ClusterUsageAnalyzer()
    if watch:
        import time
        while True:
            analyzer.refresh().print_summary(detailed=detailed)
            time.sleep(interval)
    else:
        analyzer.print_summary(detailed=detailed)

def print_hello(
    name: str = "world",  # Name to greet
    times: int = 1,  # Number of times to print
    uppercase: bool = False,  # Whether to print in uppercase
):
    """Print a customizable hello message. For testing"""
    message = f"Hello, {name}!"
    if uppercase:
        message = message.upper()
    
    for _ in range(times):
        print(message)

# Create wrapper functions that apply tyro.cli
def check_gpus_cli():
    return tyro.cli(check_gpus)

def print_hello_cli():
    return tyro.cli(print_hello)