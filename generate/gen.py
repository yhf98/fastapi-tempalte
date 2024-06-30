import argparse
from string import Template
from code_template import TEMPLATE_API, TEMPLATE_CRUD, TEMPLATE_SCHEMA
from sqlalchemy import inspect
from app.models.interface_info import InterfaceInfo

def camel_to_snake(name):
    return ''.join(['_' + i.lower() if i.isupper() else i for i in name]).lstrip('_')

def get_fields(model):
    mapper = inspect(model)
    fields = {}
    for column in mapper.columns:
        fields[column.name] = column.type
    return fields

def generate_code(model):
    model_name = model.__name__
    model_name_lower = camel_to_snake(model_name)
    fields = get_fields(model)

    fields_str = "\n    ".join([f"{name}: {col.python_type.__name__}" for name, col in fields.items() if name != 'id'])

    # Update TEMPLATE_SCHEMA
    schema_template = Template(TEMPLATE_SCHEMA)
    schema_code = schema_template.substitute(ModelName=model_name, model_name_lower=model_name_lower, fields=fields_str)

    with open(f'app/schemas/{model_name_lower}.py', 'w', encoding='utf-8') as f:
        f.write(schema_code)

    # Update TEMPLATE_API
    api_template = Template(TEMPLATE_API)
    api_code = api_template.substitute(ModelName=model_name, model_name_lower=model_name_lower)

    with open(f'app/api/v1/endpoints/{model_name_lower}.py', 'w', encoding='utf-8') as f:
        f.write(api_code)

    # Update TEMPLATE_CRUD
    crud_template = Template(TEMPLATE_CRUD)
    crud_code = crud_template.substitute(ModelName=model_name, model_name_lower=model_name_lower)

    with open(f'app/crud/{model_name_lower}.py', 'w', encoding='utf-8') as f:
        f.write(crud_code)

    print(f'生成代码 {model_name} 成功！')

def main():
    print("::: 代码生成工具 :::")
    parser = argparse.ArgumentParser(description="代码生成工具")
    parser.add_argument('-m', '--model', metavar='M', type=str,
                        nargs='+', help='需要生成代码的模型名称', required=True)
    args = parser.parse_args()

    models = {
        'interface_info': InterfaceInfo
    }

    for model_name in args.model:
        model = models.get(model_name)
        if model:
            generate_code(model)
        else:
            print(f"模型 {model_name} 不存在。")

if __name__ == "__main__":
    main()
