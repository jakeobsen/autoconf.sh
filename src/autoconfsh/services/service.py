from abc import ABC

class Service(ABC):
    """
    Service is an abstract class that is used to implement service specific classes. Service implements a basic set of
    functions that should be available for all inheritor.
    """

    def __init__(self, service_name: str):
        """
        Initialize class and set service name (the name used by systemd when calling systemctl).

        :param service_name: string - systemd service name.
        """
        self._service_name: str = service_name

    def status(self) -> str:
        """
        Check the current status of the system service in systemd and return the value as a string.

        :return: The function will return the current status of the service as returned by the system.
                 If the service does not exist, the function will raise an OSError because the system
                 service does not exist.
        """
        raise NotImplementedError("status() method not implemented.")

    def enable(self) -> bool:
        """
        Enable the system service in systemd and return the outcome of the operation.

        :return: The function will return true if the service already is enabled, or if it was enabled.
                 If it was not possible to enable the service, the function will return false.
                 Likewise if the service does not exist, the function will raise an OSError because the system
                 service did not exist.
        """
        raise NotImplementedError("enable() method not implemented.")

    def disable(self) -> bool:
        """
        Disable the system service in systemd and return the outcome of the operation.

        :return: The function will return true if the service already is disabled, or if it was disabled.
                 If it was not possible to disable the service, the function will return false.
                 Likewise if the service does not exist, the function will raise an OSError because the system
                 service did not exist.
        """
        raise NotImplementedError("disable() method not implemented.")

    def stop(self) -> bool:
        """
        Stop the system service in systemd and return the outcome of the operation.

        :return: The function will return true if the service already is stopped, or if it was stopped.
                 If it was not possible to stop the service, the function will return false.
                 Likewise if the service does not exist, the function will raise an OSError because the system
                 service did not exist.
        """
        raise NotImplementedError("stop() method not implemented.")

    def start(self) -> bool:
        """
        Start the system service in systemd and return the outcome of the operation.

        :return: The function will return true if the service already is started, or if it was started.
                 If it was not possible to start the service, the function will return false.
                 Likewise if the service does not exist, the function will raise an OSError because the system
                 service did not exist.
        """
        raise NotImplementedError("start() method not implemented.")

    def restart(self) -> bool:
        """
        restart the system service in systemd and return the outcome of the operation.

        :return: The function will return true if the service already was restarted.
                 If it was not possible to restart the service, the function will return false.
                 Likewise if the service does not exist, the function will raise an OSError because the system
                 service did not exist.
        """
        raise NotImplementedError("restart() method not implemented.")

    def reload(self) -> bool:
        """
        Reload the system service in systemd and return the outcome of the operation.

        :return: The function will return true if the service already was reloaded.
                 If it was not possible to reload the service, the function will return false.
                 Likewise if the service does not exist, the function will raise an OSError because the system
                 service did not exist.
        """
        raise NotImplementedError("reload() method not implemented.")
