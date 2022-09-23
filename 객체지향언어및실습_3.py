def validate_summary(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if len(data["summary"]) > 40:
            raise ValueError("Length Error")
        return data
    return wrapper

@validate_summary
def fetch_customer_data():
    my_dict = {}
    temp = ''
    for i in range(3):
        keys = input("input key >> ")
        my_dict[keys] = input("input value >> ")
        temp += my_dict[keys]

    my_dict['summary'] = temp
    return my_dict

@validate_summary
def query_orders():
    order = input("Input food name >> ")
    num = int(input("select 1,2,3,4 >> "))
    sample = {1:"cold coffee", 2:"fresh orange juice", 3:"coke with ice", 4:"hot coffee latte"}
    if num in sample:
        drink = sample[num]
    else:
        drink = "no drink, just water"
    print("Your order: {}, {}".format(order,drink))
    return {"summary": order + ','+ drink + '-' + 'staff name: kore'}


class Validation:
    def __init__(self, validation_func, error_msg: str):
        self.validation_func = validation_func
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.validation_func(value):
            raise ValueError(f'{value!r} {self.error_msg}')


class Field:
    def __init__(self, *validations):
        self._name = None
        self.validations = validations

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def validate(self, value):
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value

class ClientClass:
    descriptor = Field(
        Validation(lambda x: isinstance(x, (int,float)), 'is so number!'),
        Validation(lambda x: x >= 0, 'is less than0'))

if __name__ == "__main__":
    # 1
    print(fetch_customer_data())
    print(query_orders())

    # 2
    client = ClientClass()
    client.descriptor = 20
    print(client.descriptor)