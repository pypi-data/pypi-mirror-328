class KVKeys:

    class Health:
        @staticmethod
        def temperature_max(device_id: str):
            return f"devices/{device_id}/temperature-max"

        @staticmethod
        def temperature_mean(device_id: str):
            return f"devices/{device_id}/temperature-mean"

        @staticmethod
        def carrier_temperature(device_id: str, carrier_id: str):
            return f"devices/{device_id}/carriers/{carrier_id}/temperature"

        @staticmethod
        def block_temperature(
            device_id: str, carrier_id: str, cluster_id: str, block: str
        ):
            return f"devices/{device_id}/carriers/{carrier_id}/clusters/{cluster_id}/blocks/{block}/temperature"

    class Device:
        @staticmethod
        def partition_status(device_id: str, partition_id: str):
            return f"devices/{device_id}/partitions/{partition_id}/status"

        @staticmethod
        def partition_queue(device_id: str, partition_id: str):
            return f"devices/{device_id}/partitions/{partition_id}/queue"

        @staticmethod
        def partition_carriers(device_id: str, partition_id: str):
            return f"devices/{device_id}/partitions/{partition_id}/carriers"

        @staticmethod
        def partition_count(device_id: str):
            return f"devices/{device_id}/partitions/count"

    class JobData:
        @staticmethod
        def base(job_id: str):
            return f"jobs/{job_id}"

        @staticmethod
        def job_status(job_id: str):
            return f"jobs/{job_id}/status"

        @staticmethod
        def job_log(job_id: str):
            return f"jobs/{job_id}/log"

        @staticmethod
        def job_data(job_id: str):
            return f"jobs/{job_id}/data"

        @staticmethod
        def job_channels(job_id: str):
            return f"jobs/{job_id}/channels"

        @staticmethod
        def channel_data(job_id: str, channel_id: str):
            return f"jobs/{job_id}/channels/{channel_id}/data"
