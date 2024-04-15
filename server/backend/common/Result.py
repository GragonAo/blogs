class Result:
    def __init__(self, code=None, message=None, data=None):
        self.code = code  # 状态码，默认为None
        self.message = message  # 消息或描述，默认为None
        self.data = data  # 数据，默认为None

    def __repr__(self):
        return f"Result(code={self.code}, message='{self.message}', data={self.data})"

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message,
            'data': self.data
        }