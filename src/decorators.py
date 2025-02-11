from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            result = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
            with open('reports.txt', "w", encoding='utf-8') as file:
                file.write(result)
            return result
        result = f"{func(*args, **kwargs)}"
        with open('reports.txt', "w", encoding='utf-8') as file:
            file.write(result)
        return result
    return wrapper
