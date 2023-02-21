import sys

from airbyte_cdk.entrypoint import launch
from source_waba_analytics import SourceWabaAnalytics

if __name__ == "__main__":
    source = SourceWabaAnalytics()
    launch(source, sys.argv[1:])
