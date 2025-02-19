class Utils:
    @staticmethod
    def get_method_name(obj, func_name: str = '') -> str:
        obj_class_name = f"{obj.__class__.__module__}.{obj.__class__.__qualname__}"
        full_name = obj_class_name + '.' + func_name if func_name else obj_class_name
        return full_name
    
    @staticmethod
    def add_attributes(obj, data: dict) -> None:
        for key, value in data.items():
            setattr(obj, key, value)
    
    @staticmethod
    def discard_empty_attributes(obj) -> None:
        obj_copy = obj.__dict__.copy()
        for key, value in obj_copy.items():
            if not value:
                delattr(obj, key)
    
    @staticmethod
    def sort_attributes(obj) -> None:
        obj.__dict__ = dict(sorted(obj.__dict__.items()))
    
    @staticmethod
    def get_error_details(errors: dict) -> list:
        return list(map(lambda error: f"{error['loc'][0]}: {error['msg']} in {error['loc'][0]}", errors))

    @staticmethod 
    async def get_instance_exception( exc : Exception):
        
        exception_class_name = type(exc).__name__

        match exception_class_name:
            case "ConnectionError":
                error_message = "Connection error occurred."
                error_info = str(exc)
            case "RetryError":
                error_message = "Retry error occurred."
                error_info = str(exc)
            case _:
                error_message = "An unexpected error occurred."
                error_info = str(exc)

        return error_message, error_info